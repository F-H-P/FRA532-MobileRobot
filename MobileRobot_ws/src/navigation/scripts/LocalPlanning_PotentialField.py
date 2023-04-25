#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from msg_interfaces.srv import GoalPath
from std_msgs.msg import Float64MultiArray
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

from nav2_msgs.srv import GetCostmap
from nav_msgs.srv import GetMap

import math
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener 

show_animation = True
dp = 0.3

class LocalPlanning(Node):
    def __init__(self):
        super().__init__('local_planning')
        self.goal_path_response = self.create_service(GoalPath,"/goal_path",self.goal_path_callback)
        self.timer = self.create_timer(0.1,self.timer_callback)
        self.costmap_client = self.create_client(GetCostmap,"/local_costmap/get_costmap")

        self.path_x = Float64MultiArray()
        self.path_y = Float64MultiArray()
        self.costmap_req = GetCostmap.Request()
        self.costmap_response = GetCostmap.Response()
        self.map_req = GetMap.Request()
        self.map_response = GetMap.Response()

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.path_req = False
        self.costmap_res = False
        self.arrive = False

        self.costmap_response = self.send_request_costmap()
        self.costmap = self.costmap_response.map.data

        self.resolution = self.costmap_response.map.metadata.resolution
        self.size_x = self.costmap_response.map.metadata.size_x #expect in grid
        self.size_y = self.costmap_response.map.metadata.size_y #expect in grid
        self.min_x = self.costmap_response.map.metadata.origin.position.x #expect in position
        self.min_y = self.costmap_response.map.metadata.origin.position.y #expect in position

        self.tx = None
        self.ty = None
        self.cx = 0.0
        self.cy = 0.0
        self.theta = 0.0
        self.ind = 0

        self.AREA_WIDTH = 30.0
        self.KP = 5.0
        self.ETA = 100.0
        # self.OSCILLATIONS_DETECTION_LENGTH = 3

        self.ox = []
        self.oy = []

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

    def goal_path_callback(self, request, response):
        self.path_x = request.x_path.data
        self.path_y = request.y_path.data
        print("request success!!!!")
        self.path_req = True
        return response

    def send_request_costmap(self):
        self.future = self.costmap_client.call_async(self.costmap_req)
        rclpy.spin_until_future_complete(self, self.future)
        print("get costmap response success!!!!")
        self.costmap_res = True
        return self.future.result()
    
    def process(self):
        if self.tx is None and self.ty is None:
            self.ind = 0
            self.tx = self.path_x[self.ind]
            self.ty = self.path_y[self.ind]
        else:
            d = self.calc_distance(self.tx,self.ty,self.cx,self.cy)
            if np.linalg.norm(d) < dp:
                if self.ind < len(self.path_x)-1:
                    self.ind += 1
                    self.tx = self.path_x[self.ind]
                    self.ty = self.path_y[self.ind]
                else:
                    self.arrive = True
                    self.tx = None
                    self.ty = None
                    print("arrive!!!")
            else:
                self.costmap_response = self.send_request_costmap()
                self.costmap = self.costmap_response.map.data

                if self.costmap_res is True:
                    i = 0
                    for i in range(len(self.costmap)-1):
                        if self.costmap[i] > 0.0:
                            px,py = self.calc_grid2position(i)
                            self.ox.append(px)
                            self.oy.append(py)
                            print(px,py)
                        i +=1
                    self.potential_field_planning(self.cx, self.cy, self.tx,self.ty, 0.01)
                    self.costmap_res = False
                else:
                    print("No costmap response!!")

    def calc_grid2position(self, index):
        px = ((index%self.size_x)*self.resolution)+self.min_x
        py = ((index//self.size_x)*self.resolution)+self.min_y
        return px,py
    
    def calc_potential_field(self, gx, gy, rr): 
        # minx = min(min(self.ox), sx, gx) - self.AREA_WIDTH / 2.0
        # miny = min(min(self.oy), sy, gy) - self.AREA_WIDTH / 2.0
        # maxx = max(max(self.ox), sx, gx) + self.AREA_WIDTH / 2.0
        # maxy = max(max(self.oy), sy, gy) + self.AREA_WIDTH / 2.0 
        # xw = int(round((maxx - minx) / self.resolution))
        # yw = int(round((maxy - miny) / self.resolution))

        size_x,size_y = self.calc_grid2position(len(self.costmap))
        size_x = size_x-self.min_x
        size_y = size_y-self.min_y
        # calc each potential
        pmap = [[0.0 for i in range(size_x)] for i in range(size_y)]

        for ix in range(size_x):
            x = ix * self.resolution + self.min_x

            for iy in range(size_y):
                y = iy * self.resolution + self.min_y
                ug = self.calc_attractive_potential(x, y, gx, gy)
                uo = self.calc_repulsive_potential(x, y, rr)
                uf = ug + uo
                pmap[ix][iy] = uf

        return pmap


    def calc_attractive_potential(self, x, y, gx, gy):
        return 0.5 * self.KP * np.hypot(x - gx, y - gy)


    def calc_repulsive_potential(self, ox, oy, rr):
        # search nearest obstacle
        minid = -1
        dmin = float("inf")
        for i, _ in enumerate(self.ox):
            d = np.hypot(ox - self.ox[i], oy - self.oy[i])
            if dmin >= d:
                dmin = d
                minid = i

        # calc repulsive potential
        dq = np.hypot(ox - self.ox[minid], oy - self.oy[minid])

        if dq <= rr:
            if dq <= 0.1:
                dq = 0.1

            return 0.5 * self.ETA * (1.0 / dq - 1.0 / rr) ** 2
        else:
            return 0.0


    def get_motion_model(self):
        # dx, dy
        motion = [[1, 0],
                [0, 1],
                [-1, 0],
                [0, -1],
                [-1, -1],
                [-1, 1],
                [1, -1],
                [1, 1]]

        return motion


    # def oscillations_detection(self, previous_ids, ix, iy):
    #     previous_ids.append((ix, iy))

    #     if (len(previous_ids) > self.OSCILLATIONS_DETECTION_LENGTH):
    #         previous_ids.popleft()

    #     # check if contains any duplicates by copying into a set
    #     previous_ids_set = set()
    #     for index in previous_ids:
    #         if index in previous_ids_set:
    #             return True
    #         else:
    #             previous_ids_set.add(index)
    #     return False


    def potential_field_planning(self, sx, sy, gx, gy, rr):
        # calc potential field
        pmap = self.calc_potential_field(gx, gy, rr)

        # search path
        d = np.hypot(sx - gx, sy - gy)
        ix = round((sx - self.min_x) / self.resolution)
        iy = round((sy - self.min_y) / self.resolution)
        gix = round((gx - self.min_x) / self.resolution)
        giy = round((gy - self.min_y) / self.resolution)

        if show_animation:
            self.draw_heatmap(pmap)
            # for stopping simulation with the esc key.
            plt.gcf().canvas.mpl_connect('key_release_event',
                    lambda event: [exit(0) if event.key == 'escape' else None])
            plt.plot(ix, iy, "*k")
            plt.plot(gix, giy, "*m")

        rx, ry = [sx], [sy]
        motion = self.get_motion_model()
        previous_ids = deque()

        if d <= dp:
            minp = float("inf")
            minix, miniy = -1, -1
            for i, _ in enumerate(motion):
                inx = int(ix + motion[i][0])
                iny = int(iy + motion[i][1])
                if inx >= len(pmap) or iny >= len(pmap[0]) or inx < 0 or iny < 0:
                    p = float("inf")  # outside area
                    print("outside potential!")
                else:
                    p = pmap[inx][iny]
                if minp > p:
                    minp = p
                    minix = inx
                    miniy = iny
            next_x = minix * self.resolution + self.min_x
            next_y = miniy * self.resolution + self.min_y
            print(next_x,next_y)
            # d = np.hypot(gx - xp, gy - yp)
            # rx.append(xp)
            # ry.append(yp)

            # if (self.oscillations_detection(previous_ids, ix, iy)):
            #     print("Oscillation detected at ({},{})!".format(ix, iy))

            if show_animation:
                plt.plot(ix, iy, ".r")
                plt.pause(0.01)

        print("Goal!!")

        return rx, ry


    def draw_heatmap(self, data):
        data = np.array(data).T
        plt.pcolor(data, vmax=100.0, cmap=plt.cm.Blues)

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
