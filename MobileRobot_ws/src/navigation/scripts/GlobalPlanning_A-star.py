#!/usr/bin/env python3

import math

import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node
from nav2_msgs.srv import GetCostmap
from nav_msgs.srv import GetMap

from std_msgs.msg import Float64MultiArray,Float64

from msg_interfaces.srv import GoalPath
from msg_interfaces.srv import SendPoint
 
show_animation = False


class AStarPlanner(Node):

    def __init__(self):
        super().__init__('a_star_planner')
        self.costmap_client = self.create_client(GetCostmap, '/global_costmap/get_costmap')
        self.timer = self.create_timer(0.11,self.timer_callback)
        self.map_client = self.create_client(GetMap,"/map_server/map")
        self.goal_path_cilent = self.create_client(GoalPath,"/goal_path")
        self.set_point_server = self.create_service(SendPoint,"/set_point",self.set_point_callback)
        
        self.costmap_req = GetCostmap.Request()
        self.costmap_response = GetCostmap.Response()
        self.map_req = GetMap.Request()
        self.map_response = GetMap.Response()
        self.goal_path_req = GoalPath.Request()
        self.x_path = Float64MultiArray()
        self.y_path = Float64MultiArray()

        self.sx = Float64
        self.sy = Float64
        self.gx = Float64
        self.gy = Float64

        self.get_behavior_request = False
        
        self.costmap_response = self.send_request_costmap()
        self.costmap = self.costmap_response.map.data
        self.map_response = self.send_request_map()
        self.map = self.map_response.map.data

        # self.resolution = self.map_response.map.info.resolution
        self.resolution = 1.0
        self.rr = 0.1
        self.x_width = self.map_response.map.info.width
        self.y_width = self.map_response.map.info.height
        # self.min_x = self.map_response.map.info.origin.position.x
        # self.min_y = self.map_response.map.info.origin.position.y
        self.min_x = 0
        self.min_y = 0
        self.max_x = self.min_x + self.x_width - 1
        self.max_y = self.min_y + self.y_width - 1
        self.obstacle_map = None
        self.motion = self.get_motion_model()
        self.calc_obstacle_map()

    def timer_callback(self):
        if self.get_behavior_request == True:
            rx, ry = self.planning(self.sx, self.sy, self.gx, self.gy)
            if show_animation:
                plt.plot(rx, ry, "-r")
                plt.pause(0.001)
                plt.show()
        

    def send_request_costmap(self):
        self.future = self.costmap_client.call_async(self.costmap_req)
        rclpy.spin_until_future_complete(self, self.future)
        print("get costmap response success!!!!")
        return self.future.result()
    
    def send_request_map(self):
        self.future_map = self.map_client.call_async(self.map_req)
        rclpy.spin_until_future_complete(self, self.future_map)
        print("get map response success!!!!")
        return self.future_map.result()
    
    def send_request_goal_path(self):
        self.goal_path_req.x_path = self.x_path
        self.goal_path_req.y_path = self.y_path
        self.goal_path_cilent.call_async(self.goal_path_req)
        print("send request success!!!!")
        return None
    
    def set_point_callback(self,request,response):
        self.sx = ((request.start_x.data)+3.95)/0.05000000074505806
        self.sy = ((request.start_y.data)+3.8)/0.05000000074505806
        self.gx = ((request.goal_x.data)+3.95)/0.05000000074505806
        self.gy = ((request.goal_y.data)+3.8)/0.05000000074505806

        print("set_point request success!!!!")
        if show_animation:  # pragma: no cover
            plt.plot((self.sx*0.05000000074505806)-3.95, (self.sy*0.05000000074505806)-3.8, "og")
            plt.plot((self.gx*0.05000000074505806)-3.95, (self.gy*0.05000000074505806)-3.8, "xb")
            plt.grid(True)
            plt.axis("equal")
        # rx, ry = self.planning(self.sx, self.sy, self.gx, self.gy)

        # if show_animation:
        #     plt.plot(rx, ry, "-r")
        #     plt.pause(0.001)
        #     plt.show()

        self.get_behavior_request = True
        return response

    class Node:
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):
        """
        A star path search
        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]
        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(start_node.x,start_node.y)] = start_node

        while True:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(goal_node,open_set[o])) #!c_id is ... that be minimum value of sum of cost and distance to goal position 
            
            current = open_set[c_id] #!current is the choosed position
################################################################################################################
            # show graph
            if show_animation:  # pragma: no cover
                plt.plot((self.calc_grid_position(current.x, self.min_x)*0.05000000074505806)-3.95, 
                         (self.calc_grid_position(current.y, self.min_y)*0.05000000074505806)-3.8, "xc")
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None]) #!Draw the positon on 
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)
################################################################################################################

            if current.x == goal_node.x and current.y == goal_node.y:
                print("Find goal")
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]
            # Add it to the closed set
            closed_set[c_id] = current

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion): #!to move to another point
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost, 
                                 c_id)
################################################################################################################
                n_id = self.calc_grid_index(node.x,node.y)
                node.cost = self.costmap[n_id]
################################################################################################################
                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node


        rx, ry = self.calc_final_path(goal_node, closed_set)
        self.get_behavior_request = False
        return rx, ry
################################################################################################################
    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [(self.calc_grid_position(goal_node.x, self.min_x)*0.05000000074505806)-3.95], [
            (self.calc_grid_position(goal_node.y, self.min_y)*0.05000000074505806)-3.8]
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append((self.calc_grid_position(n.x, self.min_x)*0.05000000074505806)-3.95)
            ry.append((self.calc_grid_position(n.y, self.min_y)*0.05000000074505806)-3.8)
            parent_index = n.parent_index
        rx.reverse()
        ry.reverse()

        self.x_path.data = rx
        self.y_path.data = ry
        rx = []
        ry = []

        print(self.x_path.data)
        print(self.y_path.data)      
        self.send_request_goal_path()

        return self.x_path.data, self.y_path.data
################################################################################################################
    @staticmethod
    def calc_heuristic(n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y) #! d = distance between n1 and n2 [math.hypot(x,y) is sqar(x*x+y*y)]
        return d
################################################################################################################
    def calc_grid_position(self, index, min_position):
        """
        calc grid position
        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos
################################################################################################################

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, x,y):
        return (y - self.min_y) * self.x_width + (x - self.min_x)
################################################################################################################
    def verify_node(self, node): #!To check the point is in map and not the obstacle
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True
################################################################################################################

    def calc_obstacle_map(self):
        self.obstacle_map = [[False for _ in range(self.y_width)]
                        for _ in range(self.x_width)]
        for y in range(self.y_width):
            for x in range(self.x_width):
                idx = self.calc_grid_index(x,y)
                if self.map[idx] == 100:
                    self.obstacle_map[x][y] = True
################################################################################################################

    @staticmethod
    def get_motion_model():
        motion = [[1, 0],
                  [0, 1],
                  [-1, 0],
                  [0, -1],
                  [-1, -1],
                  [-1, 1],
                  [1, -1],
                  [1, 1]]

        return motion

################################################################################################################
def main(args=None):
    print(__file__ + " start!!")
    rclpy.init(args=args)
    a_star = AStarPlanner()
    rclpy.spin(a_star)
    a_star.destroy_node()
    rclpy.shutdown()
################################################################################################################

if __name__ == '__main__':
    main()