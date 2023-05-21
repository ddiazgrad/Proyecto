import os
import time
import random
import json
from object_track import create_track
from tracker import Tracker
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

def generate_fake_data(sensor_data,sensor,lineas,i):
    fake_data = sensor_data
    final_data  = None
    # sensor_directory = f"../datos_sensores/{sensor}"
    
    # # Crea el directorio si no existe
    # if not os.path.exists(sensor_directory):
    #     os.makedirs(sensor_directory)
    
    # # Genera un nombre de archivo único basado en la fecha y hora actual
    # # timestamp = time.strftime("%Y%m%d%H%M%S")
    timestamp = time.time()
    # file_name = f"data_{timestamp}.json"
    fake_data ["timestamp"] = timestamp
    # Ruta completa del archivo JSON
    # file_path = os.path.join(sensor_directory, file_name)
    
    # Guarda los datos generados en el archivo JSON
    # with open(file_path, "w") as json_file:
    #     json.dump(fake_data, json_file)
    print (i)
    if sensor == "camara":
        final_data = process_camara(fake_data,lineas[0],i)
    elif sensor == "adsb":
        final_data = process_adsb(fake_data,lineas[1],i)
    elif sensor == "remoteid" and i<50:
        final_data = process_remoteid(fake_data,lineas[2],i)
    elif sensor == "remoteid" and i>100:
        final_data = process_remoteid(fake_data,lineas[2],i)

    return final_data


def process_camara(data,line,i):
    # print ("Processing camera...")
    final_data = {
        "sensor": "camera",
        "identification": data ["identification"],
        "location": {
            "x": line[2*i],
            "y": line[(2*i)+1],
            "altitude": data["location"]["altitude"]
        },
        "distance": None,
        "azimuth": None,
        "frequency": None,
        "flight_type": data["flight_type"] ,
        "timestamp": data["timestamp"],
        "speed": None
    }

    return final_data


def process_adsb(data,line,i):
    # print ("Processing ads-b...")
    final_data = {
        "sensor": "ads-b",
        "identification": data ["identification"],
        "location": {
            "x": line[2*i],
            "y": line[(2*i)+1],
            "altitude": data["location"]["altitude"]
        },
        "distance": None,
        "azimuth": None,
        "frequency": None,
        "flight_type": "heavyplane" ,
        "timestamp": data["timestamp"],
        "speed": None
    }

    return final_data

def process_remoteid(data,line,i):
    # print ("Processing remoteid...")
    final_data = {
        "sensor": "remtoteid",
        "identification": data ["identification"],
        "location": {
            "x": line[2*i],
            "y": line[(2*i)+1],
            "altitude": data["location"]["altitude"]
        },
        "distance": None,
        "azimuth": None,
        "frequency": None,
        "flight_type": "heavyplane" ,
        "timestamp": data["timestamp"],
        "speed": None
    }

    return final_data

# def process_final_jsons():
#     print ("Processing final jsons")
#     output_directory = "../datos_sensores/json_final"
#     for sensor in sensor_data:
#         sensor_directory = f"../datos_sensores/{sensor}"
#         json_files = os.listdir(sensor_directory)
#         for json_file in json_files:
#             file_path = os.path.join(sensor_directory, json_file)
            
#             with open(file_path, "r") as json_file:
#                 data = json.load(json_file)
#                 # Extrae los datos necesarios del JSON
#                 # y construye el JSON final

#                 if sensor == "camara":
#                     process_camara(data,lineas[0])
#                 elif sensor == "adsb":
#                     process_adsb(data,lineas[1])
#                 elif sensor == "remoteid":
#                     process_remoteid(data,lineas[2])
#                 final_data = {
#                     "sensor": sensor
#                     # "module": ["module"],
#                     # "identification": data["identification"],
#                     # "location": data["location"],
#                     # "timestamp": data["timestamp"]
#                 }
#             timestamp = data["timestamp"]

#             output_file_name = f"../datos_sensores/json_final/{sensor}_{timestamp}"
#             # output_file_path = os.path.join(output_directory, output_file_name)
#             # print (output_file_path)
#             # Guarda el JSON final en el directorio de salida
#             with open(output_file_name, "w") as output_json_file:
#                 json.dump(final_data, output_json_file)
                
#         # Elimina el archivo JSON procesado
        # os.remove(file_path)



def create_sensors_data(lineas):
    tracker = Tracker(150, 30, 5)
    for i in range (150):
        coordinates = []
        x_y = []
        for sensor in sensor_data:
            final_data = generate_fake_data(sensor_data[sensor],sensor,lineas,i)
            if final_data != None:
                coordinates.append(final_data)
        try:
            combinar_cercanas(coordinates, 50)
        except:
            pass
        # print (coordinates)
        create_track (coordinates,tracker)


import random
from scipy.spatial import KDTree

def combinar_cercanas(coordenadas, distancia_umbral):
    puntos = [(coord["location"]["x"], coord["location"]["y"]) for coord in coordenadas[1:]]  # Excluir el primer elemento

    kdtree = KDTree(puntos)
    posiciones_a_borrar = []

    for i, punto in enumerate(puntos, start=1):  # Comenzar en 1 en lugar de 0
        i += 1  # Ajustar el índice para mantenerlo alineado con el array original
        puntos_cercanos = kdtree.query_ball_point(punto, distancia_umbral)
        if len(puntos_cercanos) > 1:
            for cercano in puntos_cercanos:
                if (coordenadas[cercano+1]["sensor"] == "remtoteid"):
                    pass
                else:
                    posiciones_a_borrar.append(cercano+1)

    for posicion in sorted(posiciones_a_borrar, reverse=True):
        try:
            del coordenadas[posicion]
        except:
            pass    
    # print (coordenadas)






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

def leer_archivo():
    lineas = []
    with open("centers.txt", 'r') as archivo:
        for linea in archivo:
            coordenadas_str = linea.strip().replace("(","").replace(")","")
            coordenadas = tuple(map(float, [valor.strip() for valor in coordenadas_str.split(',')]))
            lineas.append(coordenadas)
    return lineas


lineas = leer_archivo()
clear_sensor_data()
create_sensors_data(lineas)
