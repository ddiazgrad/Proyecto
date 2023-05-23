import numpy as np
import matplotlib.pyplot as plt

class KalmanFilterClass():
    def __init__(self, dt, acceleration, sd_acceleration , sd_measurement):
        
        self.dt = dt
        
        # The acceleration which is essentially u from the state update equation 
        self.a =  acceleration
        
        # The standard deviation of the acceleration variable in order get t
        self.sd_a = sd_acceleration
        
        # The state transition matrix 
        self.A = np.matrix([ [1 , self.dt],
                             [0 ,   1    ]] )
        
        
        # The control input transition matrix 
        self.B = np.matrix([ [(self.dt**2)/2],
                             [    self.dt   ]]) 
        
        # The matrix that maps x to measurement 
        self.H = np.matrix( [[1,0]] )
        
        
        
        # Processs Covariance that for our case depends solely on the acceleration 
        self.Q = np.matrix([[(self.dt**4)/4, (self.dt**3)/2],
                            [(self.dt**3)/2, self.dt**2]]) * self.sd_a**2
        
        
        # Measurement Covariance. It's a scalar in this case because only position is measured
        self.R = sd_measurement**2
        
        # The error covariance matrix that is Identity for now. It's get updated based on Q, A and R.
        self.P = np.eye(self.A.shape[1])
        
        
        # Finally the vector in consideration it's [ position ; velocity ]
        self.x = np.matrix([[0],[0]])
        
    def predict(self):
        
        # The state update : X_t = A*X_t-1 + B*u 
        # here u is acceleration,a 
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.a)
        
        # Updation of the error covariance matrix 
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        
        return self.x
    
    def update(self, z):
        
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  
        
        self.x = np.round(self.x + np.dot(K, (z - np.dot(self.H, self.x))))  
        
        I = np.eye(self.H.shape[1])
        
        self.P = (I - (K * self.H)) * self.P  

def main():
    dt = 0.10
    t =np.arange(0, 100, dt)
    
    # create Waypoints for two objects
    waypoints1 = 0.01*(3*t - 4*t**2)
    waypoints2 = 0.02*(3*t - 4*t**2)  # Change the function as needed
    
    # acceleration is set to 0.08 m/s^2 for both objects
    a1 = 0.08
    a2 = 0.08  # Change as needed
    
    # we assume that the standard deviation of the acceleration is 1.9 (m/s^2) for both objects
    sd_a1 = 0.1   
    sd_a2 = 0.1  # Change as needed
    
    # and standard deviation of the measurement is 1.2 (m) for both objects
    sd_m1 = 1.2  
    sd_m2 = 1.2  # Change as needed
    
    # create KalmanFilter objects for each object
    kf1 = KalmanFilterClass(dt, a1, sd_a1, sd_m1)
    kf2 = KalmanFilterClass(dt, a2, sd_a2, sd_m2)
    
    prediction_points1 = []
    prediction_points2 = []
    
    measurement_points1 = []
    measurement_points2 = []
    
    for x1, x2 in zip(waypoints1, waypoints2):
        
        # Measurements for both objects
        z1 = kf1.H * x1 + np.random.normal(0, 25)
        z2 = kf2.H * x2 + np.random.normal(0, 25)
        
        # Append measurements
        measurement_points1.append(z1.item(0))
        measurement_points2.append(z2.item(0))
        
        # Predict and append the output for both objects
        prediction_points1.append(kf1.predict()[0])
        prediction_points2.append(kf2.predict()[0])
        
        # Update to take in the measurement to update the parameters for both objects
        kf1.update(z1.item(0))
        kf2.update(z2.item(0))
        
    # You can now plot the waypoints, measurements, and Kalman filter predictions for each object
    # ...


    # # Plotting for object 1
    # fig = plt.figure()
    # fig.suptitle('Object 1', fontsize=20)
    # plt.plot(t, np.array(waypoints1), label='Waypoints')
    # plt.plot(t, measurement_points1, label='Measurements')
    # plt.plot(t, np.squeeze(prediction_points1), label='Kalman Filter')
    # plt.xlabel('Time', fontsize=20)
    # plt.ylabel('X', fontsize=20)
    # plt.legend()
    # plt.show()

    # # Plotting for object 2
    # fig = plt.figure()
    # fig.suptitle('Object 2', fontsize=20)
    # plt.plot(t, np.array(waypoints2), label='Waypoints')
    # plt.plot(t, measurement_points2, label='Measurements')
    # plt.plot(t, np.squeeze(prediction_points2), label='Kalman Filter')
    # plt.xlabel('Time', fontsize=20)
    # plt.ylabel('X', fontsize=20)
    # plt.legend()
    # plt.show()

    fig = plt.figure()
    fig.suptitle('Object 1 and Object 2', fontsize=20)

    # Plotting for object 1
    plt.plot(t, np.array(waypoints1), label='Waypoints 1')
    plt.plot(t, measurement_points1, label='Measurements 1')
    plt.plot(t, np.squeeze(prediction_points1), label='Kalman Filter 1')

    # Plotting for object 2
    plt.plot(t, np.array(waypoints2), label='Waypoints 2')
    plt.plot(t, measurement_points2, label='Measurements 2')
    plt.plot(t, np.squeeze(prediction_points2), label='Kalman Filter 2')

    plt.xlabel('Time', fontsize=20)
    plt.ylabel('X', fontsize=20)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
