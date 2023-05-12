import json
import socket
from parameters.identification import TrackId
# Configuración del receptor
HOST = 'localhost'  # Dirección IP del receptor
PORT = 12345  # Puerto del receptor

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)


myTrackId = TrackId()

print("Esperando conexiones entrantes...")

while True:
    # Esperar la conexión entrante
    conn, addr = sock.accept()
    print("Conexión establecida desde:", addr)

    data = conn.recv(1024)  # Tamaño máximo de datos a recibir (en bytes)

    # Procesar el mensaje JSON recibido
    try:
        message = data.decode('utf-8')
        json_data = json.loads(message)
        myTrackId.id(json_data)
        # Asignar valores predeterminados a los parámetros faltantes
        identification = json_data.get("identification", None)
        location = json_data.get("location", None)
        distancia = json_data.get("distancia", None)
        azimuth = json_data.get("azimuth", None)
        elevation = json_data.get("elevation", None)
        frequency = json_data.get("frequency", None)
        aircraft_type = json_data.get("aircraft_type", None)
        detection_time = json_data.get("detection_time", None)
        speed = json_data.get("speed", None)

        # Crear un nuevo JSON con la estructura solicitada
        new_json = {
            "identification": identification,
            "location": location,
            "distancia": distancia,
            "azimuth": azimuth,
            "elevation": elevation,
            "frequency": frequency,
            "aircraft_type": aircraft_type,
            "detection_time": detection_time,
            "speed": speed
        }

        # Convertir el nuevo JSON a una cadena
        new_json_string = json.dumps(new_json)

        # Imprimir el nuevo JSON
        print("Nuevo JSON:")
        print(new_json_string)
        print()

    except json.JSONDecodeError:
        print("Error: Mensaje JSON inválido")
        print()

    # Cerrar la conexión actual
    conn.close()
