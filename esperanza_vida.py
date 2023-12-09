import pandas as pd

# Datos obtenidos de Data Set fuente: INE https://www.ine.es/jaxi/Tabla.htm?path=/t20/e245/p08/l0/&file=01003.px&L=0
# Tenemos 52 provincias por lo que tendremos 52 ID de provincia. Asignamos por orden alfabético un ID del 101 al 152.
data_esperanza_vida = {
    'id_provincia': list(range(101, 153)),
    'provincia': [
        'Álava', 'Albacete', 'Alicante', 'Almería', 'Ávila', 'Badajoz', 'Balears, Illes', 'Barcelona',
        'Burgos', 'Cáceres', 'Cádiz', 'Castellón', 'Ciudad Real', 'Córdoba', 'Coruña, A', 'Cuenca',
        'Girona', 'Granada', 'Guadalajara', 'Gipuzkoa', 'Huelva', 'Huesca', 'Jaén', 'León', 'Lleida',
        'La Rioja', 'Lugo', 'Madrid', 'Málaga', 'Murcia', 'Navarra', 'Ourense', 'Asturias', 'Palencia',
        'Palmas, Las', 'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife', 'Cantabria', 'Segovia',
        'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Bizkaia',
        'Zamora', 'Zaragoza', 'Ceuta', 'Melilla'
    ],
    'esperanza_vida': [
        84.13, 82.99, 82.62, 81.31, 83.41, 82.29, 82.90, 83.69, 83.87, 82.53, 81.44, 82.57, 82.95, 81.94, 83.11,
        83.09, 83.02, 82.67, 83.72, 83.39, 81.59, 82.94, 81.72, 83.29, 83.01, 83.20, 83.23, 84.76, 82.15, 82.05,
        83.85, 83.58, 82.46, 82.27, 81.56, 83.26, 84.12, 82.01, 83.06, 84.41, 81.74, 83.29, 82.86, 83.14, 83.77,
        82.34, 84.09, 83.39, 83.62, 83.07, 79.71, 81.55
    ]
}

# Creamos el DataFrame df_esperanza_vida
df_esperanza_vida = pd.DataFrame(data_esperanza_vida)

# Imprimir el DataFrame
print(df_esperanza_vida)
