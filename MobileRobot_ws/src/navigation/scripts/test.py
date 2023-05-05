#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from msg_interfaces.srv import CommandGUI
from std_msgs.msg import String,Int64

class CommandServer(Node):
    def __init__(self):
        super().__init__('command_server')
        self.command_server = self.create_service(CommandGUI,"/command_state",self.command_callback)
        # self.command_client = self.create_client(CommandGUI,"/command_state")
        self.get_command = String()
        self.timer = self.create_timer(0.1,self.timer_callback)
        self.request_toggle = False

    def timer_callback(self):
        if self.request_toggle is True:
            print("check response")
            send_able = self.command2navigate()
            if send_able:
                self.toggle()
            else:
                self.request_toggle = False

    def command_callback(self,request,response):
        self.get_command = request.command
        response.res.data = 1
        self.request_toggle = True
        print("sended!")
        return response
    
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
        
    def toggle(self):
        self.request_toggle = False

def main(args=None):
    print("start!!")
    rclpy.init(args=args)
    command_server = CommandServer()
    rclpy.spin(command_server)
    command_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()