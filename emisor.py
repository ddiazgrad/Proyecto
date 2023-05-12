import json
import socket

# Configuración del receptor
HOST = 'localhost'  # Dirección IP del receptor
PORT = 12345  # Puerto del receptor

# Ruta del archivo JSON
json_file = 'data/rf.json'

# Cargar el mensaje JSON desde el archivo
with open(json_file, 'r') as file:
    message = json.load(file)

# Convertir el mensaje a JSON
json_message = json.dumps(message)

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print("Conexión establecida con el receptor")

# Enviar el mensaje al receptor
sock.sendall(json_message.encode('utf-8'))

# Cerrar la conexión
sock.close()
