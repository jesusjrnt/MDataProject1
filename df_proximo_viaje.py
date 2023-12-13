import pandas as pd
import random
import pickle
from faker import Faker

fake = Faker('es_ES')  # 'es_ES' es el código para España en Faker


# Lista de opciones para 'tipo de viaje'
opciones_tipo_viaje = [
    'Costa peninsular',
    'Costa insular - Baleares',
    'Costa insular - Canarias',
    'Turismo de escapada'
]
# Lista de provincias en España
provincias_espana = [
    'Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Balears, Illes', 'Barcelona', 'Bizkaia',
        'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón', 'Ceuta', 'Ciudad Real', 'Córdoba', 'Coruña, A', 'Cuenca', 'Gipuzkoa',
        'Girona', 'Granada', 'Guadalajara', 'Huelva', 'Huesca', 'Jaén', 'La Rioja', 'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga', 
        'Melilla', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Palmas, Las', 'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife', 
        'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Zamora', 'Zaragoza'
]

provincia_proximo_viaje = fake.random_element(provincias_espana)  # Seleccionamos una provincia
provincias = [provincia_proximo_viaje] * 1500

tipos_viaje = []

for _ in range(1500):  # Cambia el número para generar un único próximo viaje

    if provincia_proximo_viaje == "Balears, Illes":  
        tipo_viaje = 'Costa insular - Baleares'
    elif provincia_proximo_viaje in ["Santa Cruz de Tenerife", "Palmas, Las"]:
        tipo_viaje = 'Costa insular - Canarias'
    elif provincia_proximo_viaje in ["Alicante", "Valencia", "Castellón", "Murcia", "Tarragona", "Barcelona", "Girona", "Lleida", "Huelva", "Granada", "Sevilla", "Córdoba", "Jaén", "Cádiz", "Málaga", "Almería"]:
        tipo_viaje = 'Costa peninsular'
    else:
        tipo_viaje = 'Turismo de escapada'

    tipos_viaje.append(tipo_viaje)


# Generar datos simulados para el próximo viaje
data = {
    'provincia_proximo_viaje': provincias,
    'tipo_de_viaje': tipos_viaje,
    'plazas_disponibles': 50  # Establecer el número de plazas disponibles para el viaje (en este caso, 50)

}

# Crear el DataFrame
df_proximo_viaje = pd.DataFrame(data)

# Necesitamos generar un diccionario con el id_provincia correspondiente para cada Provincia, desde Álava que es el 101 a Zaragoza que es el 152.
id_provincia_proximo_viaje = {
    'Álava': 101, 'Albacete': 102, 'Alicante': 103, 'Almería': 104, 'Asturias': 105, 'Ávila': 106,
    'Badajoz': 107, 'Balears, Illes': 108, 'Barcelona': 109, 'Bizkaia': 110, 'Burgos': 111,
    'Cáceres': 112, 'Cádiz': 113, 'Cantabria': 114, 'Castellón': 115, 'Ceuta': 116, 'Ciudad Real': 117,
    'Córdoba': 118, 'Coruña, A': 119, 'Cuenca': 120, 'Gipuzkoa': 121, 'Girona': 122, 'Granada': 123,
    'Guadalajara': 124, 'Huelva': 125, 'Huesca': 126, 'Jaén': 127, 'La Rioja': 128, 'León': 129,
    'Lleida': 130, 'Lugo': 131, 'Madrid': 132, 'Málaga': 133, 'Melilla': 134, 'Murcia': 135,
    'Navarra': 136, 'Ourense': 137, 'Palencia': 138, 'Palmas, Las': 139, 'Pontevedra': 140,
    'Salamanca': 141, 'Santa Cruz de Tenerife': 142, 'Segovia': 143, 'Sevilla': 144, 'Soria': 145,
    'Tarragona': 146, 'Teruel': 147, 'Toledo': 148, 'Valencia': 149, 'Valladolid': 150, 'Zamora': 151,
    'Zaragoza': 152
}

# Creamos una nueva columna 'id_provincia' con valores mapeados usando el diccionario id_provincia
df_proximo_viaje['id_provincia_proximo_viaje'] = df_proximo_viaje['provincia_proximo_viaje'].map(id_provincia_proximo_viaje)

# Creamos una columna 'id_usuario' que asigna un valor incremental desde 0001 hasta el máximo de la base de datos
df_proximo_viaje['id_usuario'] = [f'{i+1:04}' for i in range(len(df_proximo_viaje))]

# Guardar el DataFrame en un archivo usando pickle
with open('df_proximo_viaje.pickle', 'wb') as f:
    pickle.dump(df_proximo_viaje, f)

# Mostrar el DataFrame
print(df_proximo_viaje)
