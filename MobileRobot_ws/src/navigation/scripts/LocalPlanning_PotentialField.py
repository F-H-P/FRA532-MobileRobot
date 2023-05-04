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
import time

KP = 5.0

class LocalPlanning(Node):
    def __init__(self):
        super().__init__('local_planning')
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

        self.dp = 3.0
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
        print(self.costmap_old)
    #------------------------------------------------------------#
    # set global path    
    def goal_path_callback(self, request, response):
        self.path_x = request.x_path.data
        self.path_y = request.y_path.data
        self.path_req = True
        self.init_flag = True
        print("global path request success!!!!")
        return response
    #------------------------------------------------------------#
    # send local path      
    def send_request_local_path(self):
        self.local_path_request.x_path = self.local_path_x
        self.local_path_request.y_path = self.local_path_y
        self.local_path_client.call_async(self.local_path_request)
        print("send local path request success!!!!")
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
                self.find_local_path()
            time.sleep(3)
            
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
            print("Do init set target")
        else:
            d = np.hypot(self.tx-self.cx, self.ty-self.cy)
            if np.linalg.norm(d) < self.dp:
                if self.ind < len(self.path_x)-1:
                    self.ind += 1
                    self.tx = self.path_x[self.ind]
                    self.ty = self.path_y[self.ind]
                    self.change_target = True
                    print("change target")
                else:
                    self.tx = None
                    self.ty = None
                    self.path_req = False
                    print("arrive!!!")
    #------------------------------------------------------------#
    # get local costmap 
    def send_request_costmap(self):
        print("Do send request")
        future = self.costmap_client.call_async(self.costmap_req)
        try:
            print("trying")
            rclpy.spin_until_future_complete(self, future)
            print(future.result())
            return True,future.result()
        except TransformException as ex:
            return False,None
    #------------------------------------------------------------#
    def find_local_path(self):
        '''
        1. Do set_target function to update target
        2. Send local costmap request
        3. Find local path when target point or local costmap are changed -> self.local_path_x, self.local_path_y
        4. Send local path request 
        '''
        self.set_target()
        print("set target success")
        request_success = False
        while request_success is False:
            print(request_success)
            request_success,self.costmap_response = self.send_request_costmap()

        print("request success")
        local_costmap_change = False
        local_costmap_change = self.check_costmap()
        if local_costmap_change or self.change_target is True:
            self.local_path_x,self.local_path_y = self.potential_field(self.tx, self.ty, self.min_x, self.min_y, self.size_x, self.size_y)
            self.send_request_local_path()
            print("local costmap is change")
        else:
            print("not change!")

    #------------------------------------------------------------#
    class Node:
        def __init__(self, x, y, uf):
            self.x = x
            self.y = y
            self.uf = uf

    def potential_field(self, tx, ty, min_x, min_y, size_x, size_y):
        ''' 
        Find local path from potential field algorithm and store point of path

        input: target position, x_min, y_min, size_y
        output: set of point in local path -> rx, ry
        '''
        
        pmap = self.calc_potential_field(tx, ty, min_x, min_y, size_x, size_y)
        d = np.hypot(self.cx-tx, self.cy-ty)
        motion = self.get_motion_model()
        ix = self.cx-min_x
        iy = self.cy-min_y
        rx, ry = [self.cx], [self.cy]
        while d >= self.resolution:
            minp = float("inf")
            px, py = -1, -1
            i = 0
            for i,_ in enumerate(motion):
                inx = int(ix + motion[i][0])
                iny = int(iy + motion[i][1])
                node = pmap[inx][iny]
                if minp > node.uf:
                    minp = node.uf
                    px = node.x
                    py = node.y
            ix = px-min_x
            iy = py-min_y
            d = np.hypot(tx-px, ty-py)
            rx.append(px)
            ry.append(py)
        return rx,ry
        
    def calc_potential_field(self, tx, ty, min_x, min_y, size_x, size_y):
        '''
        This function used to calculate potential cost of each grid in local area

        input: target position, x_min, y_min, size_y
        return: potential cost of each grid in local costmap window
        '''
        pmap = np.zeros((size_x,size_y))
        i = 0
        for i in range(len(self.costmap_response.map.data)):
            px,py = self.calc_index2position(i,1.0,min_x,min_y,size_y)
            ug = self.calc_attractive_potential(px,py,tx,ty)
            uf = ug + self.costmap_response.map.data[i]
            node = self.Node(px,py,uf)
            pmap[px-min_x][py-min_y] = node
        return pmap
        
    def calc_attractive_potential(x, y, tx, ty):
        return 0.5 * KP * np.hypot(x - tx, y - ty)
    def get_motion_model():
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

        input: current local costmap
        output: True/False
        '''     
        i = 0
        result = False
        for i in range(len(self.costmap_response.map.data)):
            if self.costmap_old[i] != self.costmap_response.map.data[i]:
                result = True
        return result

    def calc_index2position(self, index, resolution, min_x, min_y,size_y):
        px = ((index%size_y)*resolution)+min_x
        py = ((index//size_y)*resolution)+min_y
        return px,py
    
    def calc_grid2index(self, x,y):
        return (y - self.min_y) * self.x_width + (x - self.min_x)


def main(args=None):
    print(__file__ + " start!!")
    rclpy.init(args=args)
    local_planning = LocalPlanning()
    rclpy.spin(local_planning)
    local_planning.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    print("Potential Field Local Planner start")
    main()