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
        self.gx = 0.0
        self.gy = 0.0

        self.init = False
        self.send_toggle = True
        self.request_toggle = False
        
        self.command_server = self.create_service(CommandGUI,"/command_state",self.command_callback)
        # self.command_client = self.create_client(CommandGUI,"/command_state")
        self.get_command = String()

        self.command_client = self.create_client(CommandGUI,"/command_finnish")        
        # self.command_server = self.create_service(CommandGUI,"/command_finnish",self.command_callback)
        self.send_command = String()
        self.send_command_res = Int64()
        # self.send_command_res = self.command_req()

    def command_callback(self,request,response):
        self.get_command = request.command
        response.res.data = 1
        self.request_toggle = True
        self.send_toggle = True
        print("get command requset success!!!!")
        return response

    def command_req(self):
        future_command = self.command_client.call_async(self.send_command)
        rclpy.spin_until_future_complete(self, future_command)
        print("command_finish response success!!!!")
        return self.future_command.result()
    
    def command2navigate(self):
        if self.get_command.data == "start":
            self.gx = 1.0
            self.gy = 1.0
            return True
        elif self.get_command.data == "pause":
            self.gx = 0.0
            self.gy = 0.0
            return True
        elif self.get_command.data == "resume":
            self.gx = 2.0
            self.gy = 1.0
            return True
        elif self.get_command.data == "end":
            # go to start position
            self.gx = 1.0
            self.gy = 2.0
            return True
        elif self.get_command.data == "charge":
            # set charge position
            self.gx = 3.0
            self.gy = 1.0
            return True
        elif self.get_command.data == "level1_success":
            # change goal to be level2's goal
            self.gx = 3.0
            self.gy = 1.0
            return True
        elif self.get_command.data == "level2_success":
            # send request finnish to GUI
            self.gx = 3.0
            self.gy = 1.0
            self.send_command.data = "finnish_level2"
            return False
        
    def timer_callback(self):
        if self.request_toggle is True:
            send_able = self.command2navigate()
            if send_able:
                self.send_point()
            # else:
            #     # self.send_command_res = self.command_req()
            #     # self.request_toggle = False
            self.request_toggle = False

    def listener_post(self):
        print("Do listener_post")
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

        self.set_point_client.call_async(self.set_point_req)
        # rclpy.spin_until_future_complete(self, future)

    def send_point(self):
        print("Do send_point!!")
        print(self.send_toggle)
        if self.send_toggle:
            toggle = self.listener_post()
            if toggle is True:
                self.cx = self.tf_listener.transform.translation.x
                self.cy = self.tf_listener.transform.translation.y
                print("Do this!!")
                self.send_request_point() 
                self.send_toggle = False
                print("Do send_point")
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