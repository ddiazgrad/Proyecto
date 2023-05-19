import numpy as np
import matplotlib.pyplot as plt

class KalmanFilterClass():
    def __init__(self, dt, acceleration, sd_acceleration, sd_measurement):
        self.dt = dt
        self.a = acceleration
        self.sd_a = sd_acceleration
        
        self.A = np.matrix([[1, dt, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, dt],
                            [0, 0, 0, 1]])
        
        self.B = np.matrix([[(dt**2)/2],
                            [dt],
                            [(dt**2)/2],
                            [dt]])
        
        self.H = np.matrix([[1, 0, 0, 0],
                            [0, 0, 1, 0]])
        
        self.Q = np.matrix([[((dt**4)/4) * self.sd_a**2, ((dt**3)/2) * self.sd_a**2, 0, 0],
                            [((dt**3)/2) * self.sd_a**2, (dt**2) * self.sd_a**2, 0, 0],
                            [0, 0, ((dt**4)/4) * self.sd_a**2, ((dt**3)/2) * self.sd_a**2],
                            [0, 0, ((dt**3)/2) * self.sd_a**2, (dt**2) * self.sd_a**2]])
        
        self.R = sd_measurement**2
        
        self.P = np.eye(self.A.shape[1])
        
        self.x = np.matrix([[0], [0], [0], [0]])
    
    def predict(self):
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.a)
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        return self.x
    
    def update(self, z):
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, (z - np.dot(self.H, self.x)))
        I = np.eye(self.H.shape[1])
        self.P = np.dot((I - np.dot(K, self.H)), self.P)

def main():
    dt = 0.10
    t = np.arange(0, 100, dt)
    
    waypoints_x = 0.01 * (3 * t - 4 * t**2)
    waypoints_y = 0.02 * (2 * t**2 - 3 * t + 1)
    
    a = 0.08
    sd_a = 0.1
    sd_m = 1.2
    
    kf = KalmanFilterClass(dt, a, sd_a, sd_m)
    
    prediction_points_x = []
    prediction_points_y = []
    
    measurement_points_x = []
    measurement_points_y = []
    
    for x, y in zip(waypoints_x, waypoints_y):
        z_x = kf.H[0, 0] * x + np.random.normal(0, 0.5)
        z_y = kf.H[1, 2] * y + np.random.normal(0, 0.5)
        
        measurement_points_x.append(z_x.item(0))
        measurement_points_y.append(z_y.item(0))


        z = np.matrix([[z_x], [z_y]])
        
        prediction = kf.predict()
        
        prediction_points_x.append(prediction[0, 0])
        prediction_points_y.append(prediction[2, 0])
        
        kf.update(z)
    
    fig = plt.figure()
    fig.suptitle('Waypoints', fontsize=20)
    plt.plot(t, waypoints_x, label='waypoints_x')
    plt.plot(t, waypoints_y, label='waypoints_y')
    plt.xlabel('T', fontsize=20)
    plt.ylabel('Position', fontsize=20)
    plt.legend()
    plt.show()

    fig = plt.figure()
    fig.suptitle('Measurements', fontsize=20)
    plt.plot(t, measurement_points_x, label='Measurements_x')
    plt.plot(t, measurement_points_y, label='Measurements_y')
    plt.xlabel('T', fontsize=20)
    plt.ylabel('Position', fontsize=20)
    plt.legend()
    plt.show()

    fig = plt.figure()
    fig.suptitle('Kalman Filter Prediction', fontsize=20)
    plt.plot(t, prediction_points_x, label='Kalman Filter_x')
    plt.plot(t, prediction_points_y, label='Kalman Filter_y')
    plt.xlabel('T', fontsize=20)
    plt.ylabel('Position', fontsize=20)
    plt.legend()
    plt.show()

    fig = plt.figure()
    fig.suptitle('Comparison', fontsize=20)
    plt.plot(t, waypoints_x, label='waypoints_x')
    plt.plot(t, waypoints_y, label='waypoints_y')
    plt.plot(t, measurement_points_x, label='Measurements_x')
    plt.plot(t, measurement_points_y, label='Measurements_y')
    plt.plot(t, prediction_points_x, label='Kalman Filter_x')
    plt.plot(t, prediction_points_y, label='Kalman Filter_y')
    plt.xlabel('T', fontsize=20)
    plt.ylabel('Position', fontsize=20)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()