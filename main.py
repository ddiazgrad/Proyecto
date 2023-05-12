import json

def process_message(message):
    # Procesar el mensaje JSON recibido
    try:
        data = json.loads(message)
        # Realizar las operaciones o lógica requerida con los datos del mensaje
        # Por ejemplo, imprimir la identificación de la aeronave y la ubicación
        print("Aircraft Identification:", data["identification"])
        print("Location:", data["location"])
        print()
    except:
        print("Error: Mensaje JSON inválido")
        print()

# Simulación de envío y recepción de mensajes
# Supongamos que tenemos una lista de mensajes en formato JSON
messages = [
    '{"identification": "ABC123", "location": {"latitude": 37.7749, "longitude": -122.4194, "altitude": 5000}}',
    '{"identification": "DEF456", "location": {"latitude": 40.7128, "longitude": -74.0060, "altitude": 3000}}',
    '{"identification": "GHI789", "location": {"latitude": 51.5074, "longitude": -0.1278, "altitude": 7000}}'
]

# Procesar cada mensaje de la lista
for message in messages:
    process_message(message)
