import numpy as np

class KalmanFilter:
    def __init__(self, initial_state, initial_covariance, transition_matrix, observation_matrix, process_noise, measurement_noise):
        self.state = initial_state
        self.covariance = initial_covariance
        self.transition_matrix = transition_matrix
        self.observation_matrix = observation_matrix
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise

    def predict(self):
        self.state = np.dot(self.transition_matrix, self.state)
        self.covariance = np.dot(np.dot(self.transition_matrix, self.covariance), self.transition_matrix.T) + self.process_noise

    def update(self, measurement):
        innovation = measurement - np.dot(self.observation_matrix, self.state)
        innovation_covariance = np.dot(np.dot(self.observation_matrix, self.covariance), self.observation_matrix.T) + self.measurement_noise
        kalman_gain = np.dot(np.dot(self.covariance, self.observation_matrix.T), np.linalg.inv(innovation_covariance))

        self.state = self.state + np.dot(kalman_gain, innovation)
        self.covariance = np.dot((np.eye(self.state.shape[0]) - np.dot(kalman_gain, self.observation_matrix)), self.covariance)



initial_lat = 37.7749
initial_lon = -122.4194
initial_velocity = 100.0
process_noise_variance = 0.01
measurement_noise_variance = 0.1
measurement = np.array([37.775, -122.420])


# Parámetros del filtro de Kalman
initial_state = np.array([initial_lat, initial_lon, initial_velocity])  # Estado inicial (latitud, longitud, velocidad)
initial_covariance = np.eye(3)  # Covarianza inicial
transition_matrix = np.eye(3)  # Matriz de transición (en este caso, no hay cambios en el estado)
observation_matrix = np.array([[1, 0, 0], [0, 1, 0]])  # Matriz de observación (solo se observan latitud y longitud)
process_noise = np.eye(3) * process_noise_variance  # Ruido de proceso (varianza de la velocidad)
measurement_noise = np.eye(2) * measurement_noise_variance  # Ruido de medición (varianza de la posición)

# Inicializar el filtro de Kalman
kalman_filter = KalmanFilter(initial_state, initial_covariance, transition_matrix, observation_matrix, process_noise, measurement_noise)

# Actualizar el filtro con nuevas mediciones
kalman_filter.update(measurement)

# Predecir la posición futura utilizando el filtro de Kalman
kalman_filter.predict()
predicted_state = kalman_filter.state

# Obtener las estimaciones de latitud y longitud de la posición futura
predicted_lat = predicted_state[0]
predicted_lon = predicted_state[1]


print (predicted_lat,predicted_lon)