#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from msg_interfaces.srv import SendPoint
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from msg_interfaces.srv import CommandGUI
from std_msgs.msg import String,Int64

class BehaviorServer(Node):
    def __init__(self):
        super().__init__('behavior_server')
        self.timer = self.create_timer(0.1,self.timer_callback)
        self.set_point_client = self.create_client(SendPoint,"/set_point")
        self.set_point_req = SendPoint.Request()

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.cx = 0.0
        self.cy = 0.0
        self.gx = 3.0
        self.gy = 1.0

        self.init = False
        self.send_toggle = True
        
    #     self.command_server = self.create_service(CommandGUI,"/command_state",self.command_callback)
    #     # self.command_client = self.create_client(CommandGUI,"/command_state")
    #     self.receive_command = String()

    #     self.command_client = self.create_client(CommandGUI,"/command_finnish")        
    #     # self.command_server = self.create_service(CommandGUI,"/command_finnish",self.command_callback)
    #     self.send_command = String()
    #     self.send_command_res = Int64()
    #     self.send_command_res = self.command_req()
    #     if self.send_command_res.data == 1:
    #         pass

    #     self.send_command.data = "start"

    # def command_callback(self,request,response):
    #     self.receive_command = request.command
    #     response.res.data = 1

    # def command_req(self):
    #     future_command = self.command_client.call_async(self.send_command)
    #     rclpy.spin_until_future_complete(self, future_command)
    #     print("command_finish response success!!!!")
    #     return self.future_command.result()
    
    # def command2navigate(self):
    #     i = False
    #     if i == True:
    #         self.send_command.data = "start"
    #         self.send_command_res = self.command_req()
    #     elif False:
    #         self.send_command.data = "pause"

    def timer_callback(self):
        self.send_point()

    def listener_post(self):
        try:
            self.tf_listener = self.tf_buffer.lookup_transform('map','base_link',rclpy.time.Time())
            return True
        except TransformException as ex:
            return False

    def send_request_point(self):
        self.set_point_req.start_x.data = self.cx
        self.set_point_req.start_y.data = self.cy
        self.set_point_req.goal_x.data = self.gx
        self.set_point_req.goal_y.data = self.gy

        print("send point request success!!!!")

        future = self.set_point_client.call_async(self.set_point_req)
        rclpy.spin_until_future_complete(self, future)

    def send_point(self):
        if self.send_toggle:
            toggle = self.listener_post()
            if toggle is True:
                self.cx = self.tf_listener.transform.translation.x
                self.cy = self.tf_listener.transform.translation.y
                self.send_request_point() 
                self.send_toggle = False
        else:
            pass

def main(args=None):
    print("start!!")
    rclpy.init(args=args)
    behavior_server = BehaviorServer()
    rclpy.spin(behavior_server)
    behavior_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()