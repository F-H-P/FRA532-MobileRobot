#!/usr/bin/python3

import rclpy
from rclpy.node import Node

import time
import numpy as np
from localization import pf as PF
from localization import ekf as EKF

from std_msgs.msg import Float64MultiArray
from msg_interfaces.srv import CommandGUI
from std_msgs.msg import Bool
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Imu
from turtlebot3_msgs.msg import SensorState

class LocalizationNode(Node):
    def __init__(self):
        super().__init__('localization_node')
        self.execution_rate = 20 #Hz
        self.dt = 1/self.execution_rate
        self.timer = self.create_timer(self.dt, self.timer_callback)
        # self.state_client = self.create_client(Float64MultiArray, '/robot_state', self.state_sending_callback)
        # self.update_client = self.create_client(Bool, '/update_req', self.update_req_callback)
        # self.lidar_data = self.create_subscription(LaserScan, '/scan', self.lidar_data_callback, 10)
        self.imu_data = self.create_subscription(Imu, '/imu', self.imu_callback, 10)
        self.encoder_data = self.create_subscription(SensorState, '/sensor_state', self.encoder_callback, 10)

        map_pgm = '/home/tian/mobilerobot_ws/src/localization/map/mbs_map.pgm'
        map_yaml = '/home/tian/mobilerobot_ws/src/localization/map/map.yaml'
        number_of_particles = 30
        self.pf = PF.ParticleFilter(map_pgm, map_yaml, number_of_particles)

        #state initilization
        self.pf.robot_state[0] = 0.0
        self.pf.robot_state[1] = 0.0
        self.pf.robot_state[2] = 0.0
        #generate random sample
        self.pf.generate_random_sample_with_known_state(self.pf.robot_state, 0.2, 0.175)

        self.lidar_raw_data = []
        self.dState = np.array([0.0, 0.0, 0.0])

        #buffer for previos iteration variable
        self.prev_wheel_position = np.array([0, 0])
        self.prev_encoder_ts = 0

        #imu calibration
        self.calibrate_flag = 1
        self.imu_buffer = []
        self.imu_calibration()

        self.ekf = EKF.EKFNode(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0001, self.dt)
        self.ekf.R = self.imu_calibration()
    
    def timer_callback(self):
        # self.pf.convert_rawLidarData_to_pointCloud()
        # self.pf.localize()
        # self.pf.resampling()
        # self.pf.update_state(self.dState)
        estimate_output = self.ekf.estimate(self.ekf.robot_state, self.ekf.robot_prev_state, self.ekf.z, self.ekf.u)
        
        #check input
        x_dot = (self.ekf.d/4)*(self.ekf.u[0] + self.ekf.u[1])
        print("x_dot: ", x_dot)
        
        self.ekf.robot_prev_state = self.ekf.robot_state
        self.ekf.robot_state = estimate_output[0]
        self.ekf.P = estimate_output[1]

        print("state: ", estimate_output[0])
        print("-----------------------------------------------")


    def update_req_callback(self, request, response):
        #update dState
        pass

    def state_sending_callback(self, request, response):
        pass

    def lidar_data_callback(self, msg):
        #update lidar_raw_data
        pass

    def imu_callback(self, msg):
        if self.calibrate_flag == 1:
            self.imu_buffer.append([msg.linear_acceleration.x, msg.linear_acceleration.y, msg.angular_velocity.z])
            if len(self.imu_buffer) == 100:
                self.imu_calibration()
                self.calibrate_flag = 0

        self.ekf.z[0] = msg.linear_acceleration.x
        self.ekf.z[1] = msg.linear_acceleration.y
        self.ekf.z[2] = msg.angular_velocity.z
        # print("imu: ", self.ekf.z)

    def encoder_callback(self, msg):
        current_encoder_ts = msg.header.stamp.nanosec
        dt = (current_encoder_ts - self.prev_encoder_ts)/(10**9)
        self.prev_encoder_ts = current_encoder_ts
        # print(dt)

        self.ekf.u[0] = ((msg.left_encoder - self.prev_wheel_position[0]) * 2*np.pi/4096)/dt
        self.ekf.u[1] = ((msg.right_encoder - self.prev_wheel_position[1]) * 2*np.pi/4096)/dt

        self.prev_wheel_position[0] = msg.left_encoder
        self.prev_wheel_position[1] = msg.right_encoder

        # print("encoder: ", self.ekf.u)

    def imu_calibration(self):
        imu_mean_arr = sum(np.array(self.imu_buffer))/len(self.imu_buffer)
        diag_imu_cov = sum(np.array([(self.imu_buffer[i,:] - imu_mean_arr)**2 for i in range(len(self.imu_buffer))]))/(len(self.imu_buffer) - 1)
        return np.array([diag_imu_cov[0], 0, 0],
                        [0, diag_imu_cov[1], 0],
                        [0, 0, diag_imu_cov[2]])

def main(args=None):
    rclpy.init(args=args)
    node = LocalizationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()