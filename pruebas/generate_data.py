import os
import time
import random
import json

sensor_data = {
    "adsb": {
    "module" :"adsb",
    "identification": "ABC123",
    "location": {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude": 5000
    },
    "detection_time": 100323232
    },
    "transponder_s_advanced": {
    "module" :"transponder_s_advanced",
    "identification": "ABC123",
    "location": {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude": 5000
    },
    "detection_time": 100323232
    },
    "transponder_s_elemental": {
    "module" :"transponder_s_elemental",
    "identification": "ABC123",
    "location": {
    "altitude": 5000
    },
    "detection_time": 100323232
    },
    "remote_id": {
    "module" :"remote_id",
    "identification": "ABC123",
    "location": {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude": 5000
    },
    "detection_time": 100323232,
    },
    "array_rf": {
    "module" :"array_rf",
    "azimuth": 45,
    "freq": 2.4e9,
    "power": -70,
    "detection_time": 100323232
    },    
    "camara": {
    "module" :"camera",
    "identification": "ABC123",
    "location": {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "altitude": 5000
    },
    "detection_time": 100323232
    }
    # Agrega más sensores según sea necesario
}

def generate_fake_data(sensor_data,sensor):
    # Genera datos ficticios para el sensor especificado
    # Aquí puedes aplicar la lógica de generación de datos según tus necesidades
    # Por simplicidad, se generará un valor aleatorio entre 0 y 100
    print ("generate fake_data")
    fake_data = sensor_data
    print (fake_data)
    # Ruta del directorio donde se almacenarán los archivos JSON del sensor
    sensor_directory = f"../datos_sensores/{sensor}"
    
    # Crea el directorio si no existe
    if not os.path.exists(sensor_directory):
        os.makedirs(sensor_directory)
    
    # Genera un nombre de archivo único basado en la fecha y hora actual
    timestamp = time.strftime("%Y%m%d%H%M%S")
    file_name = f"data_{timestamp}.json"
    
    # Ruta completa del archivo JSON
    file_path = os.path.join(sensor_directory, file_name)
    
    # Guarda los datos generados en el archivo JSON
    with open(file_path, "w") as json_file:
        json.dump(fake_data, json_file)
    
    return fake_data

def count_new_json_files():
    while True:
        new_file_count = 0
        # for sensor, data in sensor_data.items():
        #     # Ruta del directorio donde se encuentran los archivos JSON del sensor
        #     sensor_directory = f"../datos_sensores/{sensor}"
            
        #     # Obtiene la lista de archivos JSON en el directorio del sensor
        #     json_files = os.listdir(sensor_directory)
            
        #     for json_file in json_files:
        #         file_path = os.path.join(sensor_directory, json_file)
        #         # Verifica si el archivo fue generado después del último registro
        #         # if os.path.getmtime(file_path) > data["last_generated"]:
        #         #     new_file_count += 1
        
        # Genera datos ficticios para cada sensor y actualiza el contador y la marca de tiempo
        for sensor in sensor_data:
            fake_data = generate_fake_data(sensor_data[sensor],sensor)
            # sensor_data[sensor]["last_generated"] = time.time()
            # Puedes hacer algo con los datos ficticios generados, como almacenarlos en un archivo JSON
            
        # Imprime el recuento de nuevos archivos JSON y los datos ficticios generados para cada sensor
        print("Recuento de nuevos archivos JSON:")
        for sensor, data in sensor_data.items():
            # print(f"Sensor {sensor}: {data['count']}")
            print(f"Dato ficticio generado para {sensor}: {fake_data}")
        
        time.sleep(1)  # Espera un segundo antes de la siguiente verificación

count_new_json_files()
