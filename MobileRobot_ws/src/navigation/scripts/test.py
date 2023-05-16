#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
import numpy as np
from geometry_msgs.msg import PoseStamped
from rclpy.clock import Clock

rx = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
ry = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
class TestTopic(Node):
    def __init__(self):
        super().__init__('test_topic')
        self.timer = self.create_timer(0.1,self.timer_callback)
        self.path_pub = self.create_publisher(Path,"/local_path_new2",10)
        self.local_path = Path()
        # self.local_path.header.frame_id = "map"
        self.pose = PoseStamped()

    def timer_callback(self):
        self.publish_path()
        self.path_pub.publish(self.local_path)

    def publish_path(self):
        time_stamp = Clock().now()
        self.local_path.header.frame_id = "base_link"
        self.local_path.header.stamp = time_stamp.to_msg()
        i = 0
        # print("len(rx):",len(rx))
        for i in range(len(rx)):
            self.pose = PoseStamped()
            self.pose.pose.position.x = rx[i]
            self.pose.pose.position.y = ry[i]
            self.pose.pose.orientation.x = 0.0
            self.pose.pose.orientation.y = 0.0
            self.pose.pose.orientation.z = 0.0
            self.pose.pose.orientation.w = 1.0
            self.pose.header.frame_id = "map"
            self.pose.header.stamp = time_stamp.to_msg()
            self.local_path.poses.append(self.pose)
        


def main(args=None):
    print("start!!")
    rclpy.init(args=args)
    test_topic = TestTopic()
    rclpy.spin(test_topic)
    test_topic.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# from std_msgs.msg import Float64MultiArray
# import numpy as np

# # array = np.zeros((2,4,3))

# # array[0][0][0] = 1
# # array[0][0][1] = 2
# # array[0][0][2] = 3
# # # array.data[0][1] = 2
# # # array.data[0][2] = 2

# # print(array)

# size_x = 10
# resolution = 0.1
# min_y = -0.1
# min_x = -0.1

# local_path_x = [-0.3,0.0,0.3,0.7,0.11]
# local_path_y = [-0.3,0.1,0.5,0.3,-0.1]
# costmap_old = [10,10,10,10,10]
# costmap_new = np.zeros(100)

# def check_costmap():
#     '''
#     Check costmap of point in set of current local path
#     Check py -> if has will check px in range py
#                 -> else stop search and look for next point

#     input: current local costmap
#     output: True/False
#     '''     
#     # print("Do check costmap!")
#     result = False
#     i = len(local_path_y)-1
#     print(i)
#     for i in range(len(local_path_y)-1,-1,-1):
#         print(i)
#         j = 0
#         for j in range(size_x):
#             print("local_path_y:",(j*resolution) + min_y)
#             if np.abs(local_path_y[i]-((j*resolution) + min_y)) < 0.0001: # if position y is in current local costmap
#                 k = 0
#                 for k in range(size_x):
#                     print("local_path_x",(k*resolution) + min_x)
#                     if np.abs(local_path_x[i]-((k*resolution) + min_x)) < 0.0001:
#                         ind = (j*size_x) + k
#                         if costmap_old[i] != costmap_new[ind]:
#                             result = True
#                             break
#                     k += 1
#                 break
#             j += 1
#         print("-----------------------------")
#         # i -= 1
#     return result

# changing = check_costmap()
# print(changing)
