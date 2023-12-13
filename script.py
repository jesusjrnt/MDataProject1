import pandas as pd
import pickle
from sqlalchemy import create_engine


# Establecer la conexión a la base de datos
nombre_de_usuario = 'user'
contraseña = 'password'
nombre_de_base_de_datos = 'imserso_database'
nombre_de_host = 'localhost'  # O el host de tu base de datos
puerto = '3306'  # El puerto de tu base de datos MySQL

# Cadena de conexión para MySQL
cadena_conexion = f"mysql+pymysql://{nombre_de_usuario}:{contraseña}@{nombre_de_host}:{puerto}/{nombre_de_base_de_datos}"

# Crear el motor de la base de datos
engine = create_engine(cadena_conexion)

# Cargar todos los DataFrame desde el archivo pickle de cada script de python
with open('df_bbdd.pickle', 'rb') as f:
    df_bbdd = pickle.load(f)

with open('df_esperanza_vida.pickle', 'rb') as f:
    df_esperanza_vida = pickle.load(f)

with open('df_proximo_viaje.pickle', 'rb') as f:
    df_proximo_viaje = pickle.load(f)

with open('df_tipos_viaje.pickle', 'rb') as f:
    df_tipos_viaje = pickle.load(f)

# Seleccionar todas las columnas del DataFrame df_tipos_viaje que sirven para la tabla_tipo_de_viaje
columnas_df_tipos_viaje = df_tipos_viaje[['id_usuario', 'tipo_viaje_1', 'tipo_viaje_2', 'tipo_viaje_3', 'tipo_viaje_4', 'tipo_viaje_5']]

# Insertar los campos seleccionados en la tabla 'tabla_tipo_de_viaje' en la base de datos
columnas_df_tipos_viaje.to_sql('tabla_tipo_de_viaje', con=engine, if_exists='append', index=False)

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_compromiso_usuario
columnas_df_bbdd_01 = df_bbdd[['id_usuario', 'valoracion_usuario', 'fecha_cancelacion']]

# Insertar los campos seleccionados en la tabla 'tabla_compromiso_usuario' en la base de datos
columnas_df_bbdd_01.to_sql('tabla_compromiso_usuario', con=engine, if_exists='append', index=False)

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_diferencia_fechas_viaje
columnas_df_tipos_viaje_01 = df_tipos_viaje[['id_usuario', 'fecha_ultimo_viaje']]

# Insertar los campos seleccionados en la tabla 'tabla_diferencia_fechas_viajes' en la base de datos
columnas_df_tipos_viaje_01.to_sql('tabla_diferencia_fechas_viajes', con=engine, if_exists='append', index=False)

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_equilibrio_discapacidad
columnas_df_bbdd_02 = df_bbdd[['id_usuario', 'd_movilidad', 'd_aprendizaje', 'd_comunicacion', 'd_relaciones_sociales', 'd_autocuidado', 'd_vision', 'd_audicion', 'd_vida_domestica']]

# Insertar los campos seleccionados en la tabla 'tabla_equilibrio_discapacidad' en la base de datos
columnas_df_bbdd_02.to_sql('tabla_equilibrio_discapacidad', con=engine, if_exists='append', index=False)


# Cierra la conexión después de realizar la inserción
engine.dispose()