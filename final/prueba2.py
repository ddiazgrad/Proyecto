import math
import matplotlib.pyplot as plt

def calcular_coordenadas_transmisores(x_receptor, y_receptor, distancias, azimuths):
    coordenadas_transmisores = []
    for distancia, azimuth in zip(distancias, azimuths):
        # Convertir el azimuth a radianes
        azimuth_rad = math.radians(azimuth)

        # Calcular las coordenadas de cada transmisor
        x_transmisor = x_receptor + distancia * math.sin(azimuth_rad)
        y_transmisor = y_receptor + distancia * math.cos(azimuth_rad)

        coordenadas_transmisores.append((x_transmisor, y_transmisor))

    return coordenadas_transmisores

def pintar_escenario(x_receptor, y_receptor, coordenadas_transmisores, distancias, azimuths):
    # Crear una figura y ejes
    fig, ax = plt.subplots()

    # Dibujar la antena receptora
    ax.plot(x_receptor, y_receptor, 'ro', label='Receptor')

    # Dibujar las antenas transmisoras y mostrar las distancias y azimuths
    for i, coordenadas in enumerate(coordenadas_transmisores):
        ax.plot(coordenadas[0], coordenadas[1], 'bo', label=f'Transmisor {i+1}')
        dx = coordenadas[0] - x_receptor
        dy = coordenadas[1] - y_receptor
        x_medio = (x_receptor + coordenadas[0]) / 2
        y_medio = (y_receptor + coordenadas[1]) / 2
        ax.plot([x_receptor, coordenadas[0]], [y_receptor, coordenadas[1]], 'g--')
        ax.text(x_medio, y_medio, f'{distancias[i]} m', horizontalalignment='center', verticalalignment='bottom')
        ax.text(x_medio, y_medio+0.5, f'{azimuths[i]}°', horizontalalignment='center', verticalalignment='bottom')

    # Configurar los ejes
    ax.set_aspect('equal')
    ax.set_xlabel('Coordenada x')
    ax.set_ylabel('Coordenada y')

    # Mostrar leyenda y título
    ax.legend()
    plt.title('Escenario de las antenas')

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso
x_receptor = 2  # Coordenada x de la antena receptora
y_receptor = 3  # Coordenada y de la antena receptora
distancias = [5, 6, 7]  # Distancias entre las antenas
azimuths = [45, 60, 120]  # Azimuths de llegada de las señales en grados

coordenadas_transmisores = calcular_coordenadas_transmisores(x_receptor, y_receptor, distancias, azimuths)

pintar_escenario(x_receptor, y_receptor, coordenadas_transmisores, distancias, azimuths)
