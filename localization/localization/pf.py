#!/usr/bin/python3

import numpy as np
import yaml
from yaml.loader import SafeLoader
import matplotlib.pyplot as plt
from localization.icp import iterative_closest_point
from localization.icp import fit_p_to_q
import bisect

'''
Particle() 
parameters: None

description: A particle object storing particle's data which consists of 
- state: 1X3 numpy array
    state of a robot which are X, Y, and theta w.r.t global coordinate frame reference global cooradinate frame
- weight: float
'''
class Particle():
    def __init__(self):
        self.state = np.array([0.0, 0.0, 0.0])
        self.weight = 0.0

'''
Lidar() 
parameters: None

description: A laser scan object storing sensor's configuration which consists of
- max, min: float
    maximum, minimum detection range of the sensors (changing depends on a sensor)
- total_sample: int
    total sample that laser scan collect in 1 revolution
- N_sample: int
    Number of sample that use for point cloud matching algorithm
- sample_per_angle: int
    Number of sample that use for simulate 1 iteration of laser scan data simulation (linear interpolation)
- detection_range: float
    range of detection (between 0 to 2 pi rad)
'''
class Lidar():
    def __init__(self):
        self.max_range = 3.5 #[m]
        self.min_range = 0.0
        self.total_sample = 360
        self.N_sample = 180
        self.sample_per_angle = 50
        self.detection_range = 2*np.pi

'''
Map()
parameters:
- raw_data: a raw pgm data without any processing before
- actual map width [m]
- actual map height [m]

description: A map object storing map information and configurations which consists of
- raw_pgm_data: list
    raw .pgm image data. In .pgm structure there are Magicnumber, image size, max grey value, and img data respectively.
- map width, height: int
    map width and height in pixels
- origin: numpy array
    reference map origin position in row, col of the image array data
- odom_in_map_scale_ref_map_origin: numpy array
    global frame position w.r.t map origin reference with map frame (map frame is map scale frame at map origin)
- actual width, height: int
    map width and height in meters
'''
class Map():
    def __init__(self, raw_data, yaml_path):
        self.raw_pgm_data = raw_data
        self.width = 0
        self.height = 0
        self.max_val = 0
        self.norm_pgm_data = 0
        
        self.map_origin = np.array([0, 0])
        self.odom_in_map_scale_ref_map_origin = np.array([0.0, 0.0])
        self.map_origin_to_odom = np.array([2.02*20, 0.51*20])
        
        self.scale = 0.0
        self.actual_width = 0.0
        self.actual_height = 0.0
        
        self.mapInit()
        self.read_config(yaml_path)
        
    def read_config(self, path):
        with open(path) as f:
            data = yaml.load(f, Loader=SafeLoader)
            self.scale = 1/data["resolution"]
            self.actual_width = self.width/self.scale
            self.actual_height = self.height/self.scale
            self.map_origin[0] = -1 * data["origin"][0] * self.scale
            self.map_origin[1] = self.height + data["origin"][1] * self.scale

            self.odom_in_map_scale_ref_map_origin[0] = self.map_origin[0] + self.map_origin_to_odom[0]
            self.odom_in_map_scale_ref_map_origin[1] = self.map_origin[1] - self.map_origin_to_odom[1]

    def mapInit(self):
        if(len(self.raw_pgm_data) == 4):
            self.width = self.raw_pgm_data[0]
            self.height = self.raw_pgm_data[1]
            self.max_val = self.raw_pgm_data[2]
            self.norm_pgm_data = self.raw_pgm_data[3]/self.raw_pgm_data[2]
            # self.scale = self.width/self.actual_width

'''
ParticleFilter()
parameters:
- map_file_paht: file paht
- particleNum: number of particle (int)
- initial_state (default None): initial state of the robot

description: A particle filter object storing particle filter configurations and function of the particle filter.
'''
class ParticleFilter():
    def __init__(self, map_file_path, map_yaml_path, particleNum, initial_state=None):
        #reading pgm file and initialize map parameters
        self.map_raw_data = self.pgmMap_read(map_file_path)
        self.map = Map(
            self.map_raw_data,
            map_yaml_path
        )

        print(self.map.map_origin)
        print(self.map.width)
        print(self.map.height)

        #initilize sample
        self.samples = [Particle() for i in range(int(particleNum))]
        
        #set normalized weight treshold
        self.kill_tresh = 0.5

        #initilize lidar information
        self.lidar = Lidar()
        self.raw_lidar_data = np.zeros([self.lidar.N_sample])
        self.target_point_clouds = np.zeros([self.lidar.N_sample, 2])
        
        #initilize robot state
        self.robot_state = np.zeros(3, dtype=float)
        if initial_state != None:
            self.robot_state = initial_state

    '''
    localize() function
    parameters: None

    prequisity: 
    1. the target point cloud need to be updated before execute localize()
    2. the state of the robot must be update before execute localize()
    
    description: A localize function is a function for localize the robot in 4 steps
    1. simulate the data of each particle by using linear interpolation and loop through detection range
    2. match the simulated point cloud with target point could [**every point could is respect to to robot frame with reference of global coodinate frame in map scale**]
    3. update the weight of particle from the distance that get from iterative_closest_pint() function
    4. resampling
    '''
    def localize(self):
        for n in range(len(self.samples)):
            print("sample {}".format(n))
            # robot position w.r.t. global frame
            robotPosition = np.array([self.samples[n].state[0], self.samples[n].state[1]])
            print(robotPosition)
            # change from real scale to map scale 
            robotPosition_in_mapScale = robotPosition*self.map.scale
            print(robotPosition_in_mapScale)
            # change the reference frame from global frame to map frame
            robotPosition_in_mapScale_ref_map_frame = self.map.odom_in_map_scale_ref_map_origin + robotPosition_in_mapScale
            print(robotPosition_in_mapScale_ref_map_frame)
            
            #simulate the data of the lidar
            data = []
            x1, y1 = robotPosition_in_mapScale_ref_map_frame[0], robotPosition_in_mapScale_ref_map_frame[1]
            for angle in np.linspace(0, self.lidar.detection_range, self.lidar.N_sample, False):
                x2, y2 = (x1 + self.lidar.max_range*np.cos(self.samples[n].state[2] + angle)*self.map.scale), (y1 - self.lidar.max_range*np.sin(self.samples[n].state[2] + angle)*self.map.scale)
                for k in range(0, self.lidar.sample_per_angle):
                    i = k/self.lidar.sample_per_angle
                    x = int(x2 * i + x1 * (1 - i)) #column
                    y = int(y2 * i + y1 * (1 - i)) #row
                    if 0 < x < self.map.width and 0 < y < self.map.height:
                        if self.map.norm_pgm_data[y][x] < 0.65: ## y is row and x is col
                            data.append([x - x1, y - y1])
                            break

            #test first
            lidar_data = np.array(data).T
            print(lidar_data.shape)
            # plt.imshow(self.map.norm_pgm_data, cmap="gray")
            plt.plot(0, 0, "go", markersize = 10)
            plt.scatter(lidar_data[0], lidar_data[1])
            plt.show()

            low_x = np.min(lidar_data[0])
            low_y = np.min(lidar_data[1])
            high_x = np.max(lidar_data[0])
            high_y = np.max(lidar_data[1])
            #lidar point matching
            T, distance, p_new = iterative_closest_point(np.array(data), self.target_point_clouds, low_x, high_x, low_y, high_y, 5, 0.001)
            
            #update particle's weight
            self.samples[n].weight = round(np.mean(distance), 2)

        #resampling the partinew_sample
    def pgmMap_read(self, filename):
        """  This function reads Portable GrayMap (PGM) image files and returns
        a numpy array. Image needs to have P2 or P5 header number.
        Line1 : MagicNum
        Line2 : Width Height
        Line3 : Max Gray level
        Lines starting with # are ignored """
        with open(filename, 'rb') as f:
            #header reading
            pgm_magic_num = f.readline()
            pgm_raw_size = f.readline().split()
            width = int(pgm_raw_size[0])
            height = int(pgm_raw_size[1])
            max_val = int(f.readline())

            # Read the image data
            pgm_img = np.fromfile(f, dtype=np.uint8).reshape((height, width))

        return (width, height, max_val, pgm_img)

    '''
    generate_random_sample() function
    paramters: None

    description: generate uniform random sample by numpy.ramdom.uniform and assign to each particle
    '''
    def generate_random_sample(self):
        rand_num_w = np.random.uniform(0 - (self.map.odom_in_map_scale_ref_map_origin[0]/self.map.scale), self.map.actual_width - (self.map.odom_in_map_scale_ref_map_origin[0]/self.map.scale), len(self.samples))
        rand_num_h = np.random.uniform(0 - (self.map.odom_in_map_scale_ref_map_origin[1]/self.map.scale), self.map.actual_height - (self.map.odom_in_map_scale_ref_map_origin[1]/self.map.scale), len(self.samples))
        print(self.map.odom_in_map_scale_ref_map_origin[0]/self.map.scale)
        print(self.map.actual_width)
        
        for n in range(0,len(self.samples)):
            self.samples[n].state[0] = rand_num_w[n]
            self.samples[n].state[1] = rand_num_h[n]


    def convert_rawLidarData_to_pointCloud(self):
        ref = np.linspace(0, self.lidar.detection_range, self.lidar.N_sample, False)
        idx = 0
        im = len(self.raw_lidar_data)/self.lidar.N_sample #iteration multiplier
        for idx in range(len(ref)):
            # self.target_point_clouds[idx][0] =(-1 * self.raw_lidar_data[int(im)*idx] * np.sin(self.robot_state[2] - ref[idx]))*self.map.scale
            # self.target_point_clouds[idx][1] =(self.raw_lidar_data[int(im)*idx] * np.cos(self.robot_state[2] - ref[idx]))*self.map.scale
            self.target_point_clouds[idx][0] =(self.raw_lidar_data[int(im)*idx] * np.cos(self.robot_state[2] + ref[idx]))*self.map.scale
            self.target_point_clouds[idx][1] =(self.raw_lidar_data[int(im)*idx] * np.sin(self.robot_state[2] + ref[idx]))*self.map.scale

    '''
    resampling() function
    parameters: None

    description: resampling() helps resampling the samples (particles) by kill the low weight particle and add n particles that left from killing by
    reference the state of the sample from exsist samples. To reference the state, cumulative weight distribution is constuct. Then we random a number 
    in range of that cumulative weight. Finally, we use that number as a index to choose the exsist sample in cumulative weight array state and random
    the orientation then added as a new sample.
    '''
    def resampling(self):
        weight = [self.samples[n].weight for n in range(len(self.samples))]
        total_weight = sum(weight)
        norm_weight = np.array(weight)/total_weight
        print(norm_weight)

        current_sample = [self.samples[n] for n in range(len(self.samples)) if norm_weight[n] < 0.03]
        print([self.samples[n].weight for n in range(len(self.samples)) if norm_weight[n] > 0.01])
        print("n sample:", len(current_sample))
        buffer = 0.0
        cumulative_weight = []

        for sample in current_sample:
            buffer += sample.weight
            cumulative_weight.append(buffer)
        
        print("cumulative weight: ", cumulative_weight)

        for n in range(len(self.samples) - len(current_sample)):
            idx = bisect.bisect_left(cumulative_weight, np.random.uniform(0, max(cumulative_weight)))
            new_sample = Particle()
            print("idx: ", idx)
            new_sample.state[0] = current_sample[idx].state[0]
            new_sample.state[1] = current_sample[idx].state[1]
            new_sample.state[2] = self.robot_state[2]

            current_sample.append(new_sample)

        self.samples = current_sample


    def update_state(self, update_val):
        for n in range(len(self.samples)):
            self.samples[n].state += update_val

