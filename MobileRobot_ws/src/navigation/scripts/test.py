#!/usr/bin/env python3

# import rclpy
# from rclpy.node import Node
# from nav_msgs.msg import OccupancyGrid
# from std_msgs.msg import Int8MultiArray

# class TestTopic(Node):
#     def __init__(self):
#         super().__init__('test_topic')
#         self.timer = self.create_timer(0.1,self.timer_callback)
#         self.local_costmap_sub = self.create_subscription(OccupancyGrid,"/local_costmap/costmap",self.local_costmap_callback,10)
#         self.local_cosmap_msg = OccupancyGrid()
#         self.local_costmap = Int8MultiArray()
#         self.init_toggle = True

#     def timer_callback(self):
#         if self.init_toggle is True:
#             # print(self.local_costmap.data)
#             self.init_toggle = False

#     def local_costmap_callback(self,msg):
#         self.local_cosmap_msg = msg
#         print(self.local_cosmap_msg.info.width)
#         print(self.local_cosmap_msg.info.height)
#         print(self.local_cosmap_msg.info.origin.position.x)
#         print(self.local_cosmap_msg.info.origin.position.y)
#         print(self.local_cosmap_msg.info.resolution)

#     def sub_costmap(self):
#         self.local_costmap = self.local_cosmap_msg.data

# def main(args=None):
#     print("start!!")
#     rclpy.init(args=args)
#     test_topic = TestTopic()
#     rclpy.spin(test_topic)
#     test_topic.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

# from std_msgs.msg import Float64MultiArray
import numpy as np

# array = np.zeros((2,4,3))

# array[0][0][0] = 1
# array[0][0][1] = 2
# array[0][0][2] = 3
# # array.data[0][1] = 2
# # array.data[0][2] = 2

# print(array)

size_x = 10
resolution = 0.1
min_y = -0.1
min_x = -0.1

local_path_x = [-0.3,0.0,0.3,0.7,0.11]
local_path_y = [-0.3,0.1,0.5,0.3,-0.1]
costmap_old = [10,10,10,10,10]
costmap_new = np.zeros(100)

def check_costmap():
    '''
    Check costmap of point in set of current local path
    Check py -> if has will check px in range py
                -> else stop search and look for next point

    input: current local costmap
    output: True/False
    '''     
    # print("Do check costmap!")
    result = False
    i = 0
    for i in range(len(local_path_y)):
        j = 0
        for j in range(size_x):
            print("local_path_y:",(j*resolution) + min_y)
            if np.abs(local_path_y[i]-((j*resolution) + min_y)) < 0.0001: # if position y is in current local costmap
                k = 0
                for k in range(size_x):
                    print("local_path_x",(k*resolution) + min_x)
                    if np.abs(local_path_x[i]-((k*resolution) + min_x)) < 0.0001:
                        ind = (j*size_x) + k
                        if costmap_old[i] != costmap_new[ind]:
                            result = True
                            break
                    k += 1
                break
            j += 1
        print("-----------------------------")
        i += 1
    return result

changing = check_costmap()
print(changing)
