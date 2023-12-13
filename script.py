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

######

# Seleccionar todas las columnas del DataFrame df_proximo_viaje que sirven para la tabla_proximo_viaje
columnas_df_proximo_viaje = df_proximo_viaje[['id_usuario', 'id_provincia_proximo_viaje', 'provincia_proximo_viaje', 'plazas_disponibles', 'tipo_de_viaje']]

# Insertar los campos seleccionados en la tabla 'tabla_proximo_viaje' en la base de datos
columnas_df_proximo_viaje.to_sql('tabla_proximo_viaje', con=engine, if_exists='replace', index=False)

######

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_edad_sexo
columnas_df_bbdd_04 = df_bbdd[['id_provincia', 'sexo', 'edad_en_dias', 'enfermedad_terminal_en_dias']]

# Insertar los campos seleccionados en la tabla 'tabla_esperanza_de_vida_provincia_sexo' en la base de datos
columnas_df_bbdd_04.to_sql('tabla_edad_sexo', con=engine, if_exists='replace', index=False)

#######

# Seleccionar todas las columnas del DataFrame df_esperanza_vida que sirven para la tabla_esperanza_de_vida_provincia_sexo
columnas_df_esperanza_vida = df_esperanza_vida[['id_provincia', 'provincia', 'hombres', 'mujeres']]

# Insertar los campos seleccionados en la tabla 'tabla_esperanza_de_vida_provincia_sexo' en la base de datos
columnas_df_esperanza_vida.to_sql('tabla_esperanza_de_vida_provincia_sexo', con=engine, if_exists='replace', index=False)

#######

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_promocion_provincia
columnas_df_bbdd_03 = df_bbdd[['id_usuario', 'id_provincia', 'provincia']]

# Insertar los campos seleccionados en la tabla 'tabla_tipo_de_viaje' en la base de datos
columnas_df_bbdd_03.to_sql('tabla_promocion_movilidad', con=engine, if_exists='replace', index=False)

#######

# Seleccionar todas las columnas del DataFrame df_tipos_viaje que sirven para la tabla_tipo_de_viaje
columnas_df_tipos_viaje = df_tipos_viaje[['id_usuario', 'tipo_viaje_1', 'tipo_viaje_2', 'tipo_viaje_3', 'tipo_viaje_4']]

# Insertar los campos seleccionados en la tabla 'tabla_tipo_de_viaje' en la base de datos
columnas_df_tipos_viaje.to_sql('tabla_tipo_de_viaje', con=engine, if_exists='replace', index=False)

#######

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_compromiso_usuario
columnas_df_bbdd_01 = df_bbdd[['id_usuario', 'valoracion_usuario', 'fecha_cancelacion']]

# Insertar los campos seleccionados en la tabla 'tabla_compromiso_usuario' en la base de datos
columnas_df_bbdd_01.to_sql('tabla_compromiso_usuario', con=engine, if_exists='replace', index=False)

#######

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_diferencia_fechas_viaje
columnas_df_tipos_viaje_01 = df_tipos_viaje[['id_usuario', 'fecha_ultimo_viaje', 'fecha_hoy']]

# Insertar los campos seleccionados en la tabla 'tabla_diferencia_fechas_viajes' en la base de datos
columnas_df_tipos_viaje_01.to_sql('tabla_diferencia_fechas_viajes', con=engine, if_exists='replace', index=False)

#######

# Seleccionar todas las columnas del DataFrame df_bbdd que sirven para la tabla_equilibrio_discapacidad
columnas_df_bbdd_02 = df_bbdd[['id_usuario', 'd_movilidad', 'd_aprendizaje', 'd_comunicacion', 'd_relaciones_sociales', 'd_autocuidado', 'd_vision', 'd_audicion', 'd_vida_domestica']]

# Insertar los campos seleccionados en la tabla 'tabla_equilibrio_discapacidad' en la base de datos
columnas_df_bbdd_02.to_sql('tabla_equilibrio_discapacidad', con=engine, if_exists='replace', index=False)


# Cierra la conexión después de realizar la inserción
engine.dispose()