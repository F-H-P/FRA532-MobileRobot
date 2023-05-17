#!/usr/bin/python3

import rclpy
from rclpy.node import Node

import numpy as np
from sensor_msgs.msg import LaserScan
import time

class LaserSub(Node):
    def __init__(self):
        super().__init__('laser_sub')

        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.laserScan_callback, 10)
        self.start_angle = 0.0
        self.end_angle = 0.0
        self.data = 0.0
        self.timestamp = 0.0


    def laserScan_callback(self, msg):
        execution_time = time.time()- self.timestamp
        self.timestamp = time.time()
        self.get_logger().info(str(execution_time))
        self.get_logger().info(str("------------------------------------------------------------"))
        self.start_angle = msg.angle_min
        self.end_angle = msg.angle_max
        self.data = np.array(msg.ranges)
        self.get_logger().info(str(self.data))
        self.get_logger().info(str("------------------------------------------------------------"))

def main(args=None):
    rclpy.init(args=args)
    node = LaserSub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()