# from pyproj import Proj

# # Proyección UTM
# myProj = Proj(proj='utm', zone=33, ellps='WGS84', preserve_units=False)

# # Coordenadas en latitud y longitud
# # lat = 37.7749
# # lon = -122.4194

# lat = 16.182699622656763
# lon = 40.64479964952879

# # Conversión a UTM
# x, y = myProj(lon, lat)

# print(x, y)

import pyproj

# Crea los objetos de transformación
ecef = pyproj.Proj(proj='latlong', datum='WGS84')
utm = pyproj.Proj(proj="utm", zone=33, datum='WGS84')

# Coordenadas geográficas originales
longitude_orig = 13.408080  # Este es solo un ejemplo
latitude_orig = 52.520008  # Este es solo un ejemplo

# Transforma las coordenadas geográficas a UTM
x, y = pyproj.transform(ecef, utm, longitude_orig, latitude_orig)

print('UTM coordinates:')
print('X:', x)
print('Y:', y)

# Transforma las coordenadas UTM de vuelta a geográficas
longitude, latitude = pyproj.transform(utm, ecef, x, y)

print('\nGeographic coordinates:')
print('Longitude:', longitude)
print('Latitude:', latitude)



