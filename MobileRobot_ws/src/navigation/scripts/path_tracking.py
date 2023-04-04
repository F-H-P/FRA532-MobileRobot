#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from msg_interfaces.srv import GoalPath
from geometry_msgs.msg import Twist

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener



show_animation = False
cmd_vel = Twist()
cmd_vel.linear.x = 0.0
cmd_vel.angular.z = 0.0

dp = 0.3 # [m]
velo_max = 0.25
omega_max = 1.0

class PathTracking(Node):
    def __init__(self):
        super().__init__('path_tracking')
        self.timer = self.create_timer(0.1,self.timer_callback)
        self.goal_path_response = self.create_service(GoalPath,"/goal_path",self.goal_path_callback)
        self.cmd_vel_pub = self.create_publisher(Twist,"/cmd_vel",10)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.path_x = Float64MultiArray()
        self.path_y = Float64MultiArray()
        self.tx = None
        self.ty = None
        self.cx = 0.0
        self.cy = 0.0
        self.theta = 0.0
        self.ind = 0

        self.arrive = False
        self.path_req = False

        self.d_theta = 0.0

    def timer_callback(self):
        toggle = self.listener_post()
        if toggle is True:
            self.cx = self.tf_listener.transform.translation.x
            self.cy = self.tf_listener.transform.translation.y
            self.theta = self.euler_from_quaternion(self.tf_listener.transform.rotation.x,
                                                    self.tf_listener.transform.rotation.y,
                                                    self.tf_listener.transform.rotation.z,
                                                    self.tf_listener.transform.rotation.w)

            if self.arrive is False and self.path_req is True:
                self.process()
                if show_animation: 
                    plt.cla()
                    plt.gcf().canvas.mpl_connect(
                        'key_release_event',
                        lambda event: [exit(0) if event.key == 'escape' else None])
                    self.plot_arrow(self.cx, self.cy, self.theta)
                    plt.plot(self.path_x, self.path_y, "-r", label="course")
                    plt.plot(self.tx, self.ty, "-b", label="trajectory")
                    plt.plot(self.path_x[self.ind], self.path_y[self.ind], "xg", label="target")
                    plt.axis("equal")
                    plt.grid(True)
                    plt.title("delta theta[rad]:" + str(self.d_theta)[:4])
                    plt.pause(0.001)
            elif self.arrive:
                print("arrive!!!")

            self.cmd_vel_pub.publish(cmd_vel)

    def listener_post(self):
        try:
            self.tf_listener = self.tf_buffer.lookup_transform('map','base_link',rclpy.time.Time())
            return True
        except TransformException as ex:
            return False

    def goal_path_callback(self, request, response):
        self.path_x = request.x_path.data
        self.path_y = request.y_path.data
        print("request success!!!!")
        self.path_req = True
        return response
    

    def euler_from_quaternion(self,x, y, z, w):
            t1 = +2.0 * (w * z + x * y)
            t2 = +1.0 - 2.0 * (y * y + z * z)
            yaw_z = math.atan2(t1, t2)
        
            return yaw_z # in radians
    
    def calc_distance(self,tx,ty,cx,cy):
        d = np.hypot(tx-cx, ty-cy)
        return d
    
    def calc_theta_new(self,tx,ty,cx,cy):
        dx = tx-cx
        dy = ty-cy
        theta_new = math.atan(dy/dx)
        return theta_new
    
    def plot_arrow(self,x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
        """
        Plot arrow
        """

        if not isinstance(x, float):
            for ix, iy, iyaw in zip(x, y, yaw):
                self.plot_arrow(ix, iy, iyaw)
        else:
            plt.arrow(x, y, length * math.cos(yaw), length * math.sin(yaw),
                    fc=fc, ec=ec, head_width=width, head_length=width)
            plt.plot(x, y)

    
    def process(self):
        if self.tx is None and self.ty is None:
            self.ind = 0
            self.tx = self.path_x[self.ind]
            self.ty = self.path_y[self.ind]
        else:
            d = self.calc_distance(self.tx,self.ty,self.cx,self.cy)
            if d < dp:
                print("Update target!!")
                if self.ind < len(self.path_x)-1:
                    self.ind += 1
                    self.tx = self.path_x[self.ind]
                    self.ty = self.path_y[self.ind]
                else:
                    cmd_vel.linear.x = 0.0
                    cmd_vel.angular.z = 0.0
                    self.arrive = True
                    self.tx = None
                    self.ty = None
            else:
                cmd_vel.linear.x = velo_max

        if self.arrive is False:
            theta_new = self.calc_theta_new(self.tx,self.ty,self.cx,self.cy)
            if theta_new - self.theta > 0.001:
                cmd_vel.angular.z = omega_max
            elif theta_new - self.theta < -0.001:
                cmd_vel.angular.z = -omega_max
            else:
                cmd_vel.angular.z = 0.0
        elif self.arrive is True:
            cmd_vel.angular.z = 0.0
    
def main(args=None):
    print(__file__ + " start tracking!!")
    rclpy.init(args=args)
    path_tracking = PathTracking()
    rclpy.spin(path_tracking)
    path_tracking.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    print("Pure pursuit path tracking simulation start")
    main()