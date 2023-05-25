import numpy as np

class EKFNode():
    def __init__(self, x0, y0, x_dot0, y_dot0, theta_dot0, theta, w, v, dt):
        self.dt = dt
        
        #EKF variable
        #robot geomatric parameters
        # #turtlebot 3 burger
        self.d = 0.066 #wheel diameter
        self.l = 0.160 #wheel separation

        #EKF parameter initilization
        self.robot_state = np.array([0, 0, 0, 0 ,0 ,0], dtype=float).T
        self.robot_prev_state = np.array([0, 0, 0, 0 ,0 ,0], dtype=float).T
        self.Q = np.identity(6)
        self.R = np.identity(3)

        self.A = np.identity(6)
        self.B = np.array([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], dtype=float)
        self.C = np.array([[0, 0, 0, 0, 0, 0] ,[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], dtype=float)
        self.D = np.array([[0, 0], [0, 0], [0, 0]], dtype=float)
        self.u = np.array([0, 0], dtype=float).T
        self.P = np.identity(6)
        self.z = np.array([0.0, 0.0, 0.0]).T

        self.stateInit(x0, y0, x_dot0, y_dot0, theta_dot0, theta, w, v)
    
    """
    Extended Kalman Filter Function
    input:  x (current state)
            y (measurement)
            u (sysyem input)
    output: x_e (estimated next state)
    """
    def estimate(self, x, x_1, y, u):
        #predict
        x_p = self.DiffdriveStateTransition(x, u)
        y_p = self.IMUmeasurement(x_1, u)
        P_p = self.A @ self.P @ self.A.T + self.Q

        # #update
        K = P_p @ self.C.T @ np.linalg.inv(self.C @ P_p @ self.C.T + self.R)
        x_e = x_p + K @ (y - y_p)

        print("measurement_error: ", y - y_p)
        
        P_e = (np.identity(6) - K @ self.C) @ P_p

        return x_e, P_e

        # return x_p, np.identity(6)

    """
    Differential drive state transition function
    input:  x (current state)
            u (sysyem input) 
    output: x_p (predicted next state)   
    """
    def DiffdriveStateTransition(self, x, u):
        self.A[0] = [1, 0, 0, 0, 0, 0]
        self.A[1] = [0, 0, 0, 0, 0, 0]
        self.A[2] = [0, 0, 1, 0, 0, 0]
        self.A[3] = [0, 0, 0, 0, 0, 0]
        self.A[4] = [0, 0, 0, 0, 1, 0]
        self.A[5] = [0, 0, 0, 0, 0, 0]
        
        self.B[1] = [(self.d * np.cos(x[4])/4), (self.d * np.cos(x[4])/4)]
        self.B[0] = [self.B[1][0] * self.dt, self.B[1][1] * self.dt]
        self.B[3] = [(self.d * np.sin(x[4])/4), (self.d * np.sin(x[4])/4)]
        self.B[2] = [self.B[3][0] * self.dt, self.B[3][1] * self.dt]
        self.B[5] = [-1 * self.d / (2*self.l), self.d / (2*self.l)]
        self.B[4] = [self.B[5][0] * self.dt, self.B[5][1] * self.dt]

        return self.A @ x + self.B @ u

    """
    Differential drive IMU measurement function
    input:  x (current state)
            u (sysyem input) 
    output: y_p (predicted IMU measurement value)   
    """
    def IMUmeasurement(self, x_1, u):
        self.C[0] = [0, -1 * np.cos(x_1[4])/self.dt, 0, -1 * np.sin(x_1[4])/self.dt, 0, 0]
        self.C[1] = [0, 0, 0, 0, 0, 0]
        self.C[2] = [0, 0, 0, 0, 0, 0]

        self.D[0] = [self.d / (4*self.dt), self.d / (4*self.dt)]
        self.D[1] = [0, 0]
        self.D[2] = [-1 * self.d / (2*self.l), self.d / (2*self.l)]

        return self.C @ x_1 + self.D @ u 

    """
    State initialization function
    input: initilization value of each state
    """
    def stateInit(self, x0, y0, x_dot0, y_dot0, theta_dot0, theta, w, v):
        self.robot_state[0] = x0
        self.robot_state[1] = x_dot0
        self.robot_state[2] = y0
        self.robot_state[3] = y_dot0
        self.robot_state[4] = theta
        self.robot_state[5] = theta_dot0
        self.Q = w*np.identity(6)
        self.R = v*np.identity(3)
