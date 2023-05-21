
## 1 objeto solo en diagonal
# import numpy as np

# # Parámetros del recuadro
# width = 512
# height = 512

# # Parámetros del movimiento
# num_frames = 150
# velocity = 3  # Velocidad de movimiento

# # Generar puntos que se mueven a lo largo del recuadro
# centers = np.zeros((1, num_frames, 2))  # Inicializar los centros

# for i in range(num_frames):
#     x = velocity * i % width  # Coordenada x que se mueve de 0 a width-1
#     y = velocity * i % height  # Coordenada y que se mueve de 0 a height-1
#     centers[0, i, :] = [x, y]  # Asignar el centro al frame actual

# # Guardar los datos en un archivo
# np.save('centers.npy', centers)
# print (centers)


# import numpy as np

# # Parámetros del recuadro
# width = 1300
# height = 700

# # Parámetros del movimiento
# num_frames = 150
# velocity = 1  # Velocidad de movimiento

# # Número de objetos
# num_objects = 5

# # Generar puntos que se mueven a lo largo del recuadro
# centers = np.zeros((num_objects, num_frames, 2))  # Inicializar los centros

# for j in range(num_objects):
#     start_x = np.random.randint(width)  # Coordenada x inicial aleatoria
#     start_y = np.random.randint(height)  # Coordenada y inicial aleatoria
#     direction_x = np.random.choice([-1, 1])  # Dirección x aleatoria (izquierda o derecha)
#     direction_y = np.random.choice([-1, 1])  # Dirección y aleatoria (arriba o abajo)

#     for i in range(num_frames):
#         x = (start_x + velocity * i * direction_x) % width  # Coordenada x actual
#         y = (start_y + velocity * i * direction_y) % height  # Coordenada y actual

#         centers[j, i, 0] = x if 0 <= x < width else width - 1 if x >= width else 0  # Ajustar la coordenada x dentro del recuadro
#         centers[j, i, 1] = y if 0 <= y < height else height - 1 if y >= height else 0  # Ajustar la coordenada y dentro del recuadro

# # Guardar los datos en un archivo
# np.save('centers.npy', centers)
# print(centers)


# import numpy as np
# import cv2

# # Parámetros del recuadro
# width = 1300
# height = 700

# # Parámetros del movimiento
# num_frames = 150
# velocity = 1  # Velocidad de movimiento

# # Número de objetos
# num_objects = 5

# # Generar puntos que se mueven a lo largo del recuadro
# centers = np.zeros((num_objects, num_frames, 2))  # Inicializar los centros

# for j in range(num_objects):
#     start_x = np.random.randint(width)  # Coordenada x inicial aleatoria
#     start_y = np.random.randint(height)  # Coordenada y inicial aleatoria
#     direction_x = np.random.choice([-1, 1])  # Dirección x aleatoria (izquierda o derecha)
#     direction_y = np.random.choice([-1, 1])  # Dirección y aleatoria (arriba o abajo)

#     for i in range(num_frames):
#         x = (start_x + velocity * i * direction_x) % width  # Coordenada x actual
#         y = (start_y + velocity * i * direction_y) % height  # Coordenada y actual

#         centers[j, i, 0] = x if 0 <= x < width else width - 1 if x >= width else 0  # Ajustar la coordenada x dentro del recuadro
#         centers[j, i, 1] = y if 0 <= y < height else height - 1 if y >= height else 0  # Ajustar la coordenada y dentro del recuadro

# # Obtener las coordenadas mínimas y máximas de todos los objetos
# min_x = np.min(centers[:, :, 0])
# max_x = np.max(centers[:, :, 0])
# min_y = np.min(centers[:, :, 1])
# max_y = np.max(centers[:, :, 1])

# # Ajustar las dimensiones del recuadro para contener todos los objetos
# width = max_x - min_x + 1
# height = max_y - min_y + 1

# # Ajustar las coordenadas de los objetos al nuevo recuadro
# centers[:, :, 0] -= min_x
# centers[:, :, 1] -= min_y

# # Guardar los datos en un archivo
# np.save('centers.npy', centers)
# print(centers)



# import numpy as np
# import cv2

# # Parámetros del recuadro
# width = 1300
# height = 700

# # Parámetros del movimiento
# num_frames = 150
# velocity = 1  # Velocidad de movimiento

# # Número de objetos
# num_objects = 5

# # Generar puntos que se mueven a lo largo del recuadro
# centers = np.zeros((num_objects, num_frames, 2))  # Inicializar los centros

# for j in range(num_objects):
#     center_x = np.random.randint(width // 4, width // 4 * 3)  # Coordenada x central aleatoria
#     center_y = np.random.randint(height // 4, height // 4 * 3)  # Coordenada y central aleatoria
    
#     for i in range(num_frames):
#         angle = 2 * np.pi * i / num_frames  # Ángulo para la trayectoria circular
#         radius = width / 8  # Radio de la trayectoria circular
        
#         x = center_x + int(radius * np.cos(angle))  # Coordenada x actual
#         y = center_y + int(radius * np.sin(angle))  # Coordenada y actual
        
#         if x < 0 or x >= width:
#             x = max(0, min(x, width - 1))  # Mantener la coordenada x dentro del rango del recuadro
        
#         if y < 0 or y >= height:
#             y = max(0, min(y, height - 1))  # Mantener la coordenada y dentro del rango del recuadro
        
#         centers[j, i, 0] = x
#         centers[j, i, 1] = y

# # Obtener las coordenadas mínimas y máximas de todos los objetos
# min_x = np.min(centers[:, :, 0])
# max_x = np.max(centers[:, :, 0])
# min_y = np.min(centers[:, :, 1])
# max_y = np.max(centers[:, :, 1])

# # Ajustar las dimensiones del recuadro para abarcar todos los objetos
# width = max_x - min_x + 1
# height = max_y - min_y + 1

# # Ajustar las coordenadas de los objetos al nuevo recuadro
# centers[:, :, 0] -= min_x
# centers[:, :, 1] -= min_y

# # Guardar los datos en un archivo
# np.save('centers.npy', centers)
# print(centers)



# import numpy as np
# import cv2

# # Parámetros del recuadro
# width = 1300
# height = 700

# # Parámetros del movimiento
# num_frames = 150
# velocity = 1  # Velocidad de movimiento

# # Número de objetos
# num_objects = 1

# # Generar puntos que se mueven a lo largo del recuadro
# centers = np.zeros((num_objects, num_frames, 2))  # Inicializar los centros

# for j in range(num_objects):
#     start_x = np.random.randint(width // 4, width // 4 * 3)  # Coordenada x inicial aleatoria
#     start_y = np.random.randint(height // 4, height // 4 * 3)  # Coordenada y inicial aleatoria
    
#     direction_x = np.random.choice([-1, 1])  # Dirección x aleatoria (izquierda o derecha)
#     direction_y = np.random.choice([-1, 1])  # Dirección y aleatoria (arriba o abajo)
    
#     for i in range(num_frames):
#         x = start_x + velocity * i * direction_x  # Coordenada x actual
#         y = start_y + velocity * i * direction_y  # Coordenada y actual
        
#         if x < 0 or x >= width:
#             direction_x *= -1  # Invertir la dirección en el eje x
#             x += velocity * direction_x  # Ajustar la posición x después del rebote
            
#         if y < 0 or y >= height:
#             direction_y *= -1  # Invertir la dirección en el eje y
#             y += velocity * direction_y  # Ajustar la posición y después del rebote
        
#         centers[j, i, 0] = x
#         centers[j, i, 1] = y

# # Obtener las coordenadas mínimas y máximas de todos los objetos
# min_x = np.min(centers[:, :, 0])
# max_x = np.max(centers[:, :, 0])
# min_y = np.min(centers[:, :, 1])
# max_y = np.max(centers[:, :, 1])

# # Ajustar las dimensiones del recuadro para abarcar todos los objetos
# width = max_x - min_x + 1
# height = max_y - min_y + 1

# # Ajustar las coordenadas de los objetos al nuevo recuadro
# centers[:, :, 0] -= min_x
# centers[:, :, 1] -= min_y

# # Guardar los datos en un archivo
# np.save('centers.npy', centers)
# print(centers)


# import numpy as np
# import cv2

# # Parámetros del recuadro
# width = 1700
# height = 700

# # Parámetros del movimiento
# num_frames = 150
# velocity = 1  # Velocidad de movimiento

# # Número de objetos
# num_objects = 3

# # Generar puntos que se mueven a lo largo del recuadro
# centers = np.zeros((num_objects, num_frames, 2))  # Inicializar los centros

# for j in range(num_objects):
#     start_x = width // 2  # Coordenada x inicial en el centro
#     start_y= height // 2  # Coordenada y inicial en el centro
    
#     direction_x = np.random.choice([-1, 1])  # Dirección x aleatoria (izquierda o derecha)
#     direction_y = np.random.choice([-1, 1])  # Dirección y aleatoria (arriba o abajo)
    
#     for i in range(num_frames):
#         x = start_x + velocity * i * direction_x  # Coordenada x actual
#         y = start_y + velocity * i * direction_y  # Coordenada y actual
        
#         if x < 0 or x >= width:
#             direction_x *= -1  # Invertir la dirección en el eje x
#             x += velocity * direction_x  # Ajustar la posición x después del rebote
            
#         if y < 0 or y >= height:
#             direction_y *= -1  # Invertir la dirección en el eje y
#             y += velocity * direction_y  # Ajustar la posición y después del rebote
        
#         centers[j, i, 0] = x
#         centers[j, i, 1] = y

# # Calcular el desplazamiento necesario para centrar los objetos
# center_offset_x = width // 2 - np.mean(centers[:, :, 0])
# center_offset_y = height // 2 - np.mean(centers[:, :, 1])

# # Ajustar las coordenadas de los objetos al nuevo recuadro centrado
# centers[:, :, 0] += center_offset_x
# centers[:, :, 1] += center_offset_y

# # Guardar los datos en un archivo
# np.save('centers.npy', centers)
# print(centers)



import numpy as np
import cv2

# Parámetros del recuadro
width = 1700
height = 700

# Parámetros del movimiento
num_frames = 150
velocity = 1  # Velocidad de movimiento

# Número de objetos
num_objects = 4

# Generar puntos que se mueven a lo largo del recuadro
centers = np.zeros((num_objects, num_frames, 2))  # Inicializar los centros

for j in range(num_objects):
    start_x = np.random.randint(0, width)  # Coordenada x inicial aleatoria
    start_y = np.random.randint(0, height)  # Coordenada y inicial aleatoria
        
    x_route = np.linspace(start_x, np.random.randint(0, width), num_frames)  # Ruta x gradualmente aleatoria
    y_route = np.linspace(start_y, np.random.randint(0, height), num_frames)  # Ruta y gradualmente aleatoria
    
    for i in range(num_frames):
        x = x_route[i]  # Coordenada x actual
        y = y_route[i]  # Coordenada y actual
        
        centers[j, i, 0] = x
        centers[j, i, 1] = y

# # Calcular el desplazamiento necesario para centrar los objetos
# center_offset_x = width // 2 - np.mean(centers[:, :, 0])
# center_offset_y = height // 2 - np.mean(centers[:, :, 1])

# # Ajustar las coordenadas de los objetos al nuevo recuadro centrado
# centers[:, :, 0] += center_offset_x
# centers[:, :, 1] += center_offset_y

# Guardar los datos en un archivo
np.save('centers.npy', centers)
print(centers)

with open('centers.txt', 'w') as file:
    for j in range(num_objects):
        tracked_route = []
        for i in range(num_frames):
            x = centers[j, i, 0]
            y = centers[j, i, 1]
            tracked_route.append((x, y))
        # Convertir la lista de tuplas en una cadena de texto
        tracked_route_str = ', '.join([f'({x}, {y})' for x, y in tracked_route])
        file.write(tracked_route_str)
        file.write('\n')

            # tracked_route = []  # Reiniciar la lista para la segunda parte
            # for i in range(50, num_frames):
            #     x = centers[j, i, 0]
            #     y = centers[j, i, 1]
            #     tracked_route.append((x, y))
            # # Convertir la lista de tuplas en una cadena de texto
            # tracked_route_str = ', '.join([f'({x}, {y})' for x, y in tracked_route])
            # file2.write(tracked_route_str)
            # file2.write('\n')






# import numpy as np
# import cv2

# # Parámetros del recuadro
# width = 1700
# height = 700

# # Parámetros del movimiento
# num_frames = 150
# velocity = 1  # Velocidad de movimiento

# # Número de objetos
# num_objects = 4

# # Generar puntos que se mueven a lo largo del recuadro
# centers = np.zeros((num_objects, num_frames, 2))  # Inicializar los centros

# for j in range(num_objects):
#     start_x = np.random.randint(0, width)  # Coordenada x inicial aleatoria
#     start_y = np.random.randint(0, height)  # Coordenada y inicial aleatoria
    
#     x_direction = np.random.choice([-1, 1])  # Dirección x aleatoria (izquierda o derecha)
#     y_direction = np.random.choice([-1, 1])  # Dirección y aleatoria (arriba o abajo)
    
#     x_route = np.linspace(start_x, np.random.randint(0, width), num_frames)  # Ruta x gradualmente aleatoria
#     y_route = np.linspace(start_y, np.random.randint(0, height), num_frames)  # Ruta y gradualmente aleatoria
    
#     for i in range(num_frames):
#         x = x_route[i]  # Coordenada x actual
#         y = y_route[i]  # Coordenada y actual
        
#         if x < 0 or x >= width:
#             x_direction *= -1  # Invertir la dirección en el eje x
        
#         if y < 0 or y >= height:
#             y_direction *= -1  # Invertir la dirección en el eje y
        
#         centers[j, i, 0] = x
#         centers[j, i, 1] = y
        
#         if j == 0 and i >= 60:
#             break  # Detener la generación de muestras para el primer objeto después de 60 muestras

# # Calcular el desplazamiento necesario para centrar los objetos
# center_offset_x = width // 2 - np.mean(centers[:, :, 0])
# center_offset_y = height // 2 - np.mean(centers[:, :, 1])

# # Ajustar las coordenadas de los objetos al nuevo recuadro centrado
# centers[:, :, 0] += center_offset_x
# centers[:, :, 1] += center_offset_y

# # Guardar los datos en un archivo
# np.save('centers.npy', centers)
# print(centers)


