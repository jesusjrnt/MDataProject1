import pandas as pd
import random
from faker import Faker

fake = Faker('es_ES')

# listamos los 4 tipos de viaje posibles
tipos_viaje = [
    'Costa peninsular',
    'Costa insular - Baleares',
    'Costa insular - Canarias',
    'Turismo de escapada'
]

# generamos los 5 viajes con fecha y tipo; esto generará dos campos para cada viaje, es decir, 10 campos en total.
def generar_viajes(numero_registros):
    data_viajes = {
        f'fecha_viaje_{i}': ['' for _ in range(numero_registros)]
        for i in range(1, 6)
    }
    data_tipos_viaje = {
        f'tipo_viaje_{i}': ['' for _ in range(numero_registros)]
        for i in range(1, 6)
    }
    return {**data_viajes, **data_tipos_viaje}

def crear_dataframe_viajes(numero_registros):
    data_viajes = generar_viajes(numero_registros)
    df_tipos_viaje = pd.DataFrame(data_viajes)
    df_tipos_viaje['id_usuario'] = [f'{i+1:04}' for i in range(numero_registros)]

    for i in range(numero_registros):
        num_viajes = random.randint(1, min(5, len(tipos_viaje)))
        fechas = sorted([fake.date_between(start_date='-2y', end_date='-7d') for _ in range(num_viajes)])
        tipos = random.sample(tipos_viaje, num_viajes)

        for j in range(num_viajes):
            df_tipos_viaje.at[i, f'fecha_viaje_{j+1}'] = fechas[j].strftime('%Y-%m-%d')
            df_tipos_viaje.at[i, f'tipo_viaje_{j+1}'] = tipos[j]
        
        # Con esto sacamos la fecha y tipo del último viaje para el usuario actual
        fechas_validas = [fecha for fecha in fechas if fecha]
        if fechas_validas:
            df_tipos_viaje.at[i, 'fecha_ultimo_viaje'] = max(fechas_validas).strftime('%Y-%m-%d')
            indice_ultimo_viaje = fechas.index(max(fechas_validas))
            df_tipos_viaje.at[i, 'ultimo_tipo_viaje'] = tipos[indice_ultimo_viaje]
        else:
            df_tipos_viaje.at[i, 'fecha_ultimo_viaje'] = None
            df_tipos_viaje.at[i, 'ultimo_tipo_viaje'] = None

    return df_tipos_viaje

numero_registros = 1500  # Número de registros
df_tipos_viaje = crear_dataframe_viajes(numero_registros)

# Imprimimos el DataFrame
print(df_tipos_viaje)

# Si quisieramos ver todas las columnas sin truncar, podemos usar lo siguiente:
# pd.set_option('display.max_columns', None)
# print(df_tipos_viaje)