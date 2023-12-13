import pandas as pd
import pickle

# Datos obtenidos de Data Set fuente: INE https://www.ine.es/jaxi/Tabla.htm?path=/t20/e245/p08/l0/&file=01003.px&L=0
# Tenemos 52 provincias por lo que tendremos 52 ID de provincia. Asignamos por orden alfabético un ID del 101 al 152.
data_esperanza_vida = {
    'id_provincia': list(range(101, 153)),
    'provincia': [
        'Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Balears, Illes', 'Barcelona', 'Bizkaia',
        'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón', 'Ceuta', 'Ciudad Real', 'Córdoba', 'Coruña, A', 'Cuenca', 'Gipuzkoa',
        'Girona', 'Granada', 'Guadalajara', 'Huelva', 'Huesca', 'Jaén', 'La Rioja', 'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga', 
        'Melilla', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Palmas, Las', 'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife', 
        'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Zamora', 'Zaragoza'
    ],
    'hombres': [
        81.70, 80.30, 79.96, 78.68, 79.65, 81.43, 79.55, 80.19, 80.95, 80.66, 81.05, 80.11, 78.75, 80.43, 79.82, 77.95, 80.25, 79.02, 80.13, 80.96,
        80.37, 80.42, 80.10, 81.91, 78.70, 80.13, 79.03, 80.46, 80.45, 80.27, 80.74, 82.08, 79.66, 79.22, 79.32, 81.05, 80.58, 78.98, 79.19, 80.49,
        81.55, 79.38, 81.77, 78.97, 80.82, 80.22, 80.28, 81.34, 79.76, 81.48, 80.93, 80.22
    ],
    'mujeres': [
        86.47, 85.79, 85.36, 84.10, 85.14, 85.53, 85.12, 85.64, 86.24, 85.92, 86.89, 85.05, 84.16, 85.57, 85.41, 81.45, 85.67, 84.85, 85.99, 85.35, 
        86.35, 85.68, 85.23, 85.58, 84.57, 86.02, 84.44, 86.00, 86.18, 85.92, 85.80, 87.11, 84.62, 83.84, 84.85, 86.67, 86.64, 85.87, 83.98, 85.87,
        86.67, 84.62, 87.21, 84.42, 86.12, 85.56, 86.47, 86.26, 84.81, 86.63, 86.53, 85.86
    ]
}

# Creamos el DataFrame df_esperanza_vida
df_esperanza_vida = pd.DataFrame(data_esperanza_vida)


# Guardar el DataFrame en un archivo usando pickle
with open('df_esperanza_vida.pickle', 'wb') as f:
    pickle.dump(df_esperanza_vida, f)
