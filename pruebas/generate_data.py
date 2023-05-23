import os
import time
import random
import json

sensor_data = {
    "adsb": {
    "module" :"adsb",
    "identification": "ABC123",
    "location": {
    "x": 37.7749,
    "y": -122.4194,
    "altitude": 5000
    },
    "timestamp": 100323232
    },
    "transponder_s_advanced": {
    "module" :"transponder_s_advanced",
    "identification": "ABC123",
    "location": {
    "x": 37.7749,
    "y": -122.4194,
    "altitude": 5000
    },
    "timestamp": 100323232
    },
    "transponder_s_elemental": {
    "module" :"transponder_s_elemental",
    "identification": "ABC123",
    "location": {
    "altitude": 5000
    },
    "timestamp": 100323232
    },
    "remoteid": {
    "module" :"remoteid",
    "identification": "ABC123",
    "location": {
    "x": 37.7749,
    "y": -122.4194,
    "altitude": 5000
    },
    "timestamp": 100323232,
    },
    "array_rf": {
    "module" :"array_rf",
    "azimuth": 45,
    "freq": 2.4e9,
    "power": -70,
    "timestamp": 100323232
    },    
    "camara": {
    "module" :"camera",
    "flight_type": "drone",
    "identification": "ABC123",
    "location": {
    "x": 37.7749,
    "y": -122.4194,
    "altitude": 5000
    },
    "timestamp": 100323232
    }
    # Agrega más sensores según sea necesario
}

def generate_fake_data(sensor_data,sensor):

    fake_data = sensor_data
    sensor_directory = f"../datos_sensores/{sensor}"
    
    # Crea el directorio si no existe
    if not os.path.exists(sensor_directory):
        os.makedirs(sensor_directory)
    
    # Genera un nombre de archivo único basado en la fecha y hora actual
    # timestamp = time.strftime("%Y%m%d%H%M%S")
    timestamp = time.time()
    file_name = f"data_{timestamp}.json"
    fake_data ["timestamp"] = timestamp
    # Ruta completa del archivo JSON
    file_path = os.path.join(sensor_directory, file_name)
    
    # Guarda los datos generados en el archivo JSON
    with open(file_path, "w") as json_file:
        json.dump(fake_data, json_file)
    
    return fake_data


def process_camara(data):
    print ("Processing camera...")
    final_data = {
        "sensor": "camera",
        "identification": data ["identification"],
        "location": {
            "x": data["location"]["x"],
            "y": data["location"]["y"],
            "altitude": data["location"]["altitude"]
        },
        "distance": None,
        "azimuth": None,
        "frequency": None,
        "flight_type": data["flight_type"] ,
        "timestamp": data["timestamp"],
        "speed": None
    }

    print (final_data)


def process_adsb(data):
    print ("Processing ads-b...")
    final_data = {
        "sensor": "ads-b",
        "identification": data ["identification"],
        "location": {
            "x": data["location"]["x"],
            "y": data["location"]["y"],
            "altitude": data["location"]["altitude"]
        },
        "distance": None,
        "azimuth": None,
        "frequency": None,
        "flight_type": "heavyplane" ,
        "timestamp": data["timestamp"],
        "speed": None
    }

    print (final_data)

def process_remoteid(data):
    print ("Processing remoteid...")
    final_data = {
        "sensor": "remtoteid",
        "identification": data ["identification"],
        "location": {
            "x": data["location"]["x"],
            "y": data["location"]["y"],
            "altitude": data["location"]["altitude"]
        },
        "distance": None,
        "azimuth": None,
        "frequency": None,
        "flight_type": "heavyplane" ,
        "timestamp": data["timestamp"],
        "speed": None
    }

    print (final_data)

def process_final_jsons():
    print ("Processing final jsons")
    output_directory = "../datos_sensores/json_final"
    for sensor in sensor_data:
        sensor_directory = f"../datos_sensores/{sensor}"
        json_files = os.listdir(sensor_directory)
        for json_file in json_files:
            file_path = os.path.join(sensor_directory, json_file)
            
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
                # Extrae los datos necesarios del JSON
                # y construye el JSON final

                if sensor == "camara":
                    process_camara(data)
                elif sensor == "adsb":
                    process_adsb(data)
                elif sensor == "remoteid":
                    process_remoteid(data)
                final_data = {
                    "sensor": sensor
                    # "module": ["module"],
                    # "identification": data["identification"],
                    # "location": data["location"],
                    # "timestamp": data["timestamp"]
                }
            timestamp = data["timestamp"]

            output_file_name = f"../datos_sensores/json_final/{sensor}_{timestamp}"
            # output_file_path = os.path.join(output_directory, output_file_name)
            # print (output_file_path)
            # Guarda el JSON final en el directorio de salida
            with open(output_file_name, "w") as output_json_file:
                json.dump(final_data, output_json_file)
                
        # Elimina el archivo JSON procesado
        os.remove(file_path)



def create_sensors_data():
    for i in range (1):
        for sensor in sensor_data:
            fake_data = generate_fake_data(sensor_data[sensor],sensor)


        # for sensor, data in sensor_data.items():        
        # time.sleep(1)

    process_final_jsons() 

def clear_sensor_data():
    for sensor in sensor_data:
        # Ruta del directorio donde se encuentran los archivos JSON del sensor
        sensor_directory = f"../datos_sensores/{sensor}"
        
        # Elimina todos los archivos JSON en el directorio del sensor
        file_list = os.listdir(sensor_directory)
        for file_name in file_list:
            file_path = os.path.join(sensor_directory, file_name)
            os.remove(file_path)
    directory = f"../datos_sensores/json_final"
    file_list = os.listdir(directory)
    for file_name in file_list:
        file_path = os.path.join(directory,file_name)
        os.remove(file_path)
clear_sensor_data()
create_sensors_data()
