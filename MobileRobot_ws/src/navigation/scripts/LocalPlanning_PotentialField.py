#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from msg_interfaces.srv import GoalPath
from std_msgs.msg import Float64MultiArray

import math
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener 

import numpy as np
from nav2_msgs.srv import GetCostmap

from msg_interfaces.srv import LocalPath

from nav_msgs.msg import OccupancyGrid, Path
from rclpy.clock import Clock
from geometry_msgs.msg import PoseStamped

KP = 5.0
show_animation = True

class LocalPlanning(Node):
    def __init__(self):
        super().__init__('local_planning')
        self.get_logger().info('Potential Field Local Planner start')
        
        self.timer = self.create_timer(0.1,self.timer_callback)
        self.goal_path_response = self.create_service(GoalPath,"/goal_path",self.goal_path_callback)
        self.path_x = Float64MultiArray()
        self.path_y = Float64MultiArray()
        self.path_req = False

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.cx = 0.0
        self.cy = 0.0
        self.theta = 0.0

        self.dp = 1.0
        self.tx = None
        self.ty = None
        self.ind = 0
        self.change_target = False

        self.costmap_client = self.create_client(GetCostmap,"/local_costmap/get_costmap")
        self.costmap_req = GetCostmap.Request()
        self.costmap_response = GetCostmap.Response()

        self.local_path_client = self.create_client(LocalPath,"/local_path")
        self.local_path_request = LocalPath.Request()
        self.local_path_x = Float64MultiArray()
        self.local_path_y = Float64MultiArray()
        # self.local_path_x.data  = None
        # self.local_path_y.data = None

        ## local cosstmap topic
        self.local_costmap_sub = self.create_subscription(OccupancyGrid,"/local_costmap/costmap",self.local_costmap_callback,10)
        self.local_cosmap_msg = OccupancyGrid()
        self.costmap_old = None
        self.size_x = 0
        self.size_y = 0
        self.min_x = 0.0
        self.min_y = 0.0 
        self.resolution = 0.0

        self.arrive = False
        self.local_costmap_change = False

        self.path_pub = self.create_publisher(Path,"/local_path_new",10)
        self.local_path = Path()
        # self.local_path.header.frame_id = "map"
        self.pose = PoseStamped()
       
        ## local cosstmap service
        '''
        self.init_flag = False
        request_success = False
        while request_success is False:
            request_success,self.costmap_response = self.send_request_costmap()
        
        self.costmap_old = self.costmap_response.map.data
        self.size_x = self.costmap_response.map.metadata.size_x
        self.size_y = self.costmap_response.map.metadata.size_y 
        self.min_x = self.costmap_response.map.metadata.origin.position.x
        self.min_y = self.costmap_response.map.metadata.origin.position.y 
        self.resolution = self.costmap_response.map.metadata.resolution
        '''
    #------------------------------------------------------------#
    # set global path    
    def goal_path_callback(self, request, response):
        self.path_x = request.x_path.data
        self.path_y = request.y_path.data
        self.path_req = True
        self.init_flag = True
        self.local_costmap_change = True
        self.get_logger().info('global path request success!!!!')
        # self.local_path_y.data = [self.path_y[0],self.path_y[1]]
        return response
    #------------------------------------------------------------#
    # send local path      
    def send_request_local_path(self):
        self.local_path_request.x_path = self.local_path_x
        self.local_path_request.y_path = self.local_path_y
        self.local_path_client.call_async(self.local_path_request)
        self.get_logger().info('send local path request success!!!!')
    #------------------------------------------------------------#
        # get local costmap 
    def send_request_costmap(self):
        self.get_logger().info('Do send request')
        future = self.costmap_client.call_async(self.costmap_req)
        try:
            print("trying")
            rclpy.spin_until_future_complete(self, future)
            print(future.result())
            return True,future.result()
        except TransformException as ex:
            return False,None
        
    def local_costmap_callback(self,msg):
        self.local_cosmap_msg = msg
        self.size_x = self.local_cosmap_msg.info.width
        self.size_y = self.local_cosmap_msg.info.height
        self.min_x = self.local_cosmap_msg.info.origin.position.x
        self.min_y = self.local_cosmap_msg.info.origin.position.y
        self.resolution = self.local_cosmap_msg.info.resolution
    #------------------------------------------------------------#
    def timer_callback(self):
        '''
        set current position and do find_local_path function when have request from goal path server in every 3 second
        '''
        toggle = self.listener_post()
        if toggle is True:
            self.cx = self.tf_listener.transform.translation.x
            self.cy = self.tf_listener.transform.translation.y
            self.theta = self.euler_from_quaternion(self.tf_listener.transform.rotation.x,
                                                    self.tf_listener.transform.rotation.y,
                                                    self.tf_listener.transform.rotation.z,
                                                    self.tf_listener.transform.rotation.w)
            if self.path_req is True:
                self.arrive = False
                self.find_local_path()
                self.path_pub.publish(self.local_path)
                self.local_path.poses.clear()
            
    def listener_post(self):
        try:
            self.tf_listener = self.tf_buffer.lookup_transform('map','base_link',rclpy.time.Time())
            return True
        except TransformException as ex:
            return False

    def euler_from_quaternion(self,x, y, z, w):
            t1 = +2.0 * (w * z + x * y)
            t2 = +1.0 - 2.0 * (y * y + z * z)
            yaw_z = math.atan2(t1, t2)
            return yaw_z # in radians
    #------------------------------------------------------------#
    def set_target(self):
        '''
        Update target -> self.tx, self.ty
        '''
        self.change_target = False
        if self.tx is None or self.ty is None:
            self.ind = 0
            self.tx = self.path_x[self.ind]
            self.ty = self.path_y[self.ind]
            self.ind += 1
            self.get_logger().info('Do init set target')
        else:
            d = np.hypot(self.tx-self.cx, self.ty-self.cy)
            while np.abs(d)-self.dp <= 0.2 : #np.linalg.norm(d) or self.ind != len(self.path_x)-1
                self.tx = self.path_x[self.ind]
                self.ty = self.path_y[self.ind]
                self.change_target = True
                d = np.hypot(self.tx-self.cx, self.ty-self.cy)

                if self.ind == len(self.path_x)-1:
                    break
                else:
                    self.ind += 1
                # else:
                #     self.get_logger().info('arrive!!!')
        print("tx:",self.tx,", ty:",self.ty)
        print("len path:",len(self.path_x)-1,", ind:",self.ind)
    #------------------------------------------------------------#
    def find_local_path(self):
        '''
        1. Do set_target function to update target
        2. Send local costmap request
        3. Find local path when target point or local costmap are changed -> self.local_path_x, self.local_path_y
        4. Send local path request 
        '''
        if self.arrive is False:
            self.set_target()
            self.get_logger().info('set target success')
            self.get_logger().info('*-----------------------------------*')

            if self.local_costmap_change is False:
                self.local_costmap_change,not_exist = self.check_costmap()
                self.get_logger().info('check_costmap success')
                if not_exist is True:
                    self.find_closest_free_space()

            # print(self.local_costmap_change,self.change_target)
            self.get_logger().info(str(self.local_costmap_change)+str(self.change_target))

            if self.change_target is True or self.local_costmap_change is True:
                self.local_path_x.data,self.local_path_y.data = self.potential_field(self.tx, self.ty, self.min_x, self.min_y, self.size_x, self.size_y)
                self.get_logger().info('local costmap is change')
                self.send_request_local_path()
                self.publish_localpath(self.local_path_x.data, self.local_path_y.data)
                self.local_costmap_change = False
            else:
                self.get_logger().info('not change!')

    #------------------------------------------------------------#
    def potential_field(self, tx, ty, min_x, min_y, size_x, size_y):
        ''' 
        Find local path from potential field algorithm and store point of path

        input: target position, x_min, y_min, size_y
        output: set of point in local path -> rx, ry
        '''
        pmap,px,py = self.calc_potential_field(tx, ty, min_x, min_y, size_x, size_y)
        print("Do this")
        d = np.hypot(self.cx-tx, self.cy-ty)

        motion = self.get_motion_model()
        rx, ry = [self.cx], [self.cy]
        self.costmap_old = []
        ix_old = -1
        iy_old = -1
        while d > self.resolution: 
            print("d:",d)
            minp = 10000.0
            i = 0
            for i in range(7):
                inx = int(px + motion[i][0])
                iny = int(py + motion[i][1])
                # print("inx:",inx,", iny:",iny)
                if inx < 0 or inx > (size_x-1) or iny < 0 or iny > (size_y-1):
                    pass
                else:
                    if minp > pmap[inx][iny][2]:
                        minp = pmap[inx][iny][2]
                        min_px = pmap[inx][iny][1]
                        min_py = pmap[inx][iny][0]
                        min_cost = pmap[inx][iny][3]
                i = i+1
            px = min_px
            py = min_py
            ix = (px*self.resolution)+min_x
            iy = (py*self.resolution)+min_y
            d = np.hypot(tx-ix, ty-iy)
            # print("ix:",ix,", iy:",iy)
            if ix_old == ix and iy_old == iy:
                break
            ix_old = ix
            iy_old = iy
            rx.append(ix)
            ry.append(iy)
            self.costmap_old.append(min_cost)
        self.get_logger().info("find path success")

        if tx == self.path_x[len(self.path_x)-2] and ty == self.path_y[len(self.path_y)-2]:
            self.arrive = True
            self.tx = None
            self.ty = None
            self.path_req = False
            self.get_logger().info('arrive!!!')
        return rx,ry
        
    def calc_potential_field(self, tx, ty, min_x, min_y, size_x, size_y):
        '''
        This function used to calculate potential cost of each grid in local area

        input: target position, x_min, y_min, size_y
        return: potential cost of each grid in local costmap window
        '''
        pmap = np.zeros((size_x,size_y,4))
        i = 0
        min_dx = 10.0
        min_dy = 10.0
        # self.get_logger().info("min_x:",min_x,", min_y:",min_y)
        for i in range(len(self.local_cosmap_msg.data)):
            px = i%size_y
            py = i//size_y
            ug = self.calc_attractive_potential((px*self.resolution)+min_x,(py*self.resolution)+min_y,tx,ty)
            uf = ug + self.local_cosmap_msg.data[i]
            pmap[px][py][0] = px
            pmap[px][py][1] = py
            pmap[px][py][2] = uf
            pmap[px][py][3] = self.local_cosmap_msg.data[i]

            dx = np.abs(self.cx - ((px*self.resolution)+min_x))
            dy = np.abs(self.cy - ((py*self.resolution)+min_y))
            if dx <= min_dx and dy <= min_dy:
                min_dx = dx
                min_dy = dy
                ind_cx = px
                ind_cy = py   

            i = i+1
        return pmap,ind_cx,ind_cy
        
    def calc_attractive_potential(self, x, y, tx, ty):
        return 0.5 * KP * np.hypot(x - tx, y - ty)
    def get_motion_model(self):
        '''
        Generate motion of searching
        '''
        motion = [[1, 0],
                [0, 1],
                [-1, 0],
                [0, -1],
                [-1, -1],
                [-1, 1],
                [1, -1],
                [1, 1]]
        return motion
    #------------------------------------------------------------#
    def check_costmap(self):
        '''
        Check costmap of point in set of current local path
        Check py -> if has will check px in range py
                 -> else stop search and look for next point

        input: current local costmap
        output: True/False
        '''     
        result = False
        not_exist = False
        # print(self.size_x,self.size_y)

        i = len(self.local_path_y.data)-2
        print(i)
        for i in range(len(self.local_path_y.data)-2,-1,-1):
            j = 0
            for j in range(self.size_x):
                if np.abs(self.local_path_y.data[i]-((j*self.resolution) + self.min_y)) < 0.0001: # if position y is in current local costmap
                    k = 0
                    for k in range(self.size_x):
                        if np.abs(self.local_path_x.data[i]-((k*self.resolution) + self.min_x)) < 0.0001:
                            ind = (j*self.size_x) + k
                            # print("i:",i,", ind:",ind)
                            # print("self.costmap_old[i]:",self.costmap_old[i])
                            if self.costmap_old[i] != self.local_cosmap_msg.data[ind]:
                                if i == len(self.local_path_y.data)-1:
                                    not_exist = True
                                result = True
                                break
                    break
        return result,not_exist
    
    def find_closest_free_space(self,size_y):
        i = 0
        min_dp = 1000
        for i in range(len(self.local_cosmap_msg.data)-1):
            if self.local_cosmap_msg.data[i] <= 100:
                px = i%size_y
                py = i//size_y
                dp = np.hypot(self.tx- px, self.ty - py)
                if dp <= min_dp:
                    closest_px = px
                    closest_py = py
                    min_dp = dp
        self.tx = closest_px
        self.ty = closest_py

    def publish_localpath(self,rx,ry):
        time_stamp = Clock().now()
        self.local_path.header.frame_id = "base_link"
        self.local_path.header.stamp = time_stamp.to_msg()
        i = 0
        print("len(rx):",len(rx))
        for i in range(len(rx)-1):
            self.pose.pose.position.x = rx[i]
            self.pose.pose.position.y = ry[i]
            self.pose.pose.orientation.x = 0.0
            self.pose.pose.orientation.y = 0.0
            self.pose.pose.orientation.z = 0.0
            self.pose.pose.orientation.w = 1.0
            self.pose.header.frame_id = "base_link"
            self.pose.header.stamp = time_stamp.to_msg()
            self.local_path.poses.append(self.pose)


def main(args=None):
    print(__file__ + " start!!")
    rclpy.init(args=args)
    local_planning = LocalPlanning()
    rclpy.spin(local_planning)
    local_planning.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()