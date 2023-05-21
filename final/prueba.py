import math

def calculate_distance(ptx, gtx, grx, wavelength, received_power):
    """
    Calcula la distancia entre un transmisor y un receptor utilizando la fórmula de Friis.

    Args:
        ptx (float): Potencia de transmisión en dBm.
        gtx (float): Ganancia de la antena transmisora en dBi.
        grx (float): Ganancia de la antena receptora en dBi.
        wavelength (float): Longitud de onda de la señal en metros.
        received_power (float): Potencia recibida en dBm.

    Returns:
        float: La distancia calculada en metros.
    """
    ptx_mw = 10 ** ((ptx - 30) / 10)  # Potencia de transmisión en mW
    received_power_mw = 10 ** ((received_power - 30) / 10)  # Potencia recibida en mW

    # Cálculo de la distancia utilizando la fórmula de Friis
    distance = (wavelength / (4 * math.pi)) * math.sqrt(ptx_mw * gtx * grx / received_power_mw)

    return distance










ptx = 20  # Potencia de transmisión en dBm
gtx = 10  # Ganancia de la antena transmisora en dBi
grx = 5  # Ganancia de la antena receptora en dBi
wavelength = 0.125  # Longitud de onda de la señal en metros
received_power = -71.99  # Potencia recibida en dBm

distance = calculate_distance(ptx, gtx, grx, wavelength, received_power)
print("La distancia calculada es:", distance, "metros")



