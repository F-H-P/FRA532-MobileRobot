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

        self.local_costmap_store = dict()
        self.min_x = -3.95
        self.min_y = -3.4
        self.x_width = 169

        self.init_flag = False
        self.costmap_old = Float64MultiArray()
    #------------------------------------------------------------#
    # set global path    
    def goal_path_callback(self, request, response):
        self.path_x.data = request.x_path.data
        self.path_y.data = request.y_path.data
        print("global path request success!!!!")
        self.path_req = True
        self.init_flag = True
        return response
    #------------------------------------------------------------#
    # send local path      
    def send_request_local_path(self):
        self.local_path_request.x_path = self.local_path_x
        self.local_path_request.y_path = self.local_path_y
        self.local_path_client.call_async(self.local_path_request)
        print("send local path request success!!!!")
        return None
    #------------------------------------------------------------#
    # set current position
    def timer_callback(self):
        toggle = self.listener_post()
        if toggle is True:
            self.cx = self.tf_listener.transform.translation.x
            self.cy = self.tf_listener.transform.translation.y
            self.theta = self.euler_from_quaternion(self.tf_listener.transform.rotation.x,
                                                    self.tf_listener.transform.rotation.y,
                                                    self.tf_listener.transform.rotation.z,
                                                    self.tf_listener.transform.rotation.w)
            # find local path
            if self.path_req is True:
                self.find_local_path()
            
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
    # update target
    def set_target(self):
        self.change_target = False
        if self.tx or self.ty is None:
            self.ind = 0
            self.tx = self.path_x[self.ind]
            self.ty = self.path_y[self.ind]
        else:
            d = self.calc_distance(self.tx,self.ty,self.cx,self.cy)
            if np.linalg.norm(d) < self.dp:
                if self.ind < len(self.path_x)-1:
                    self.ind += 1
                    self.tx = self.path_x[self.ind]
                    self.ty = self.path_y[self.ind]
                    self.change_target = True
                else:
                    self.tx = None
                    self.ty = None
                    self.path_req = False
                    print("arrive!!!")

    def calc_distance(self,tx,ty,cx,cy):
        d = np.hypot(tx-cx, ty-cy)
        return d
    #------------------------------------------------------------#
    # get local costmap 
    def send_request_costmap(self):
        self.future = self.costmap_client.call_async(self.costmap_req)
        rclpy.spin_until_future_complete(self, self.future)
        print("get costmap response success!!!!")
        return self.future.result()
    #------------------------------------------------------------#
    # find local path
    def find_local_path(self):
        print("Do find local path!!")
        self.set_target()
        self.costmap_response = self.send_request_costmap()
        local_costmap_change = False
        local_costmap_change = self.check_costmap()
        if local_costmap_change or self.change_target is True:
            # self.potential_field()
            # self.send_request_local_path()
            print("local costmap is change")
    #------------------------------------------------------------#
    def potential_field(self):
        # find local path and store in self.local_path_x and self.local_path_y
        pass
    #------------------------------------------------------------#
    class Node:
        def __init__(self, x, y, cost):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost

    def check_costmap(self):
        # check costmap of point in set of current local path
        # return True/False
        if self.init_flag is True:
            j = 0
            for j in range(len(self.costmap_response.map.data)):
                px, py = self.calc_grid2position(j)
                node = self.Node(px,py,self.costmap_response.map.data[j])
                node.cost = self.costmap[j]
                self.local_costmap_store[j] = node

                self.costmap_old[j] = self.costmap_response.map.data[j]
                self.init_flag = False
        else:
            i = 0
            for i in range(len(self.costmap_response.map.data)):
                if self.costmap_old[i] != self.costmap_response.map.data[i]:
                    return True
                # ind = self.calc_grid_index(self.path_x.data[i],self.path_y.data[i])
                # if ind in self.local_costmap_store:
                #     return True
                # else:
                #     return False

    def calc_grid2position(self, index):
        px = ((index%self.size_x)*self.resolution)+self.min_x
        py = ((index//self.size_x)*self.resolution)+self.min_y
        return px,py
    
    def calc_grid_index(self, x,y):
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