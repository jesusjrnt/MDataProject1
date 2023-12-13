import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import datetime
from contextlib import redirect_stdout
import io


# Establecer la conexión a la base de datos SQL
nombre_de_usuario = 'user'
contraseña = 'password'
nombre_de_base_de_datos = 'imserso_database'
nombre_de_host = 'localhost'  # O el host de tu base de datos
puerto = '3306'  # El puerto de tu base de datos MySQL

# Cadena de conexión para MySQL
cadena_conexion = f"mysql+pymysql://{nombre_de_usuario}:{contraseña}@{nombre_de_host}:{puerto}/{nombre_de_base_de_datos}"

# Crear el motor de la base de datos
engine = sqlalchemy.create_engine(cadena_conexion)

# Definir la consulta SQL para obtener los datos de la tabla_equilibrio_discapacidad
consulta_sql = "SELECT * FROM tabla_equilibrio_discapacidad"

# Cargar los datos desde la tabla SQL en un DataFrame
data = pd.read_sql(consulta_sql, engine)

# Definir los multiplicadores para cada tipo de discapacidad
multiplicadores = {
    'd_movilidad': 1.0,
    'd_aprendizaje': 0.8,
    'd_comunicacion': 0.8,
    'd_relaciones_sociales': 0.6,
    'd_autocuidado': 0.6,
    'd_vision': 0.5,
    'd_audicion': 0.5,
    'd_vida_domestica': 0.5
}

# Multiplicar las columnas por sus respectivos multiplicadores
for col, mult in multiplicadores.items():
    data[col] *= mult

# Obtener la columna 'puntos_discapacidad' con el valor máximo de las columnas multiplicadas
data['puntos_discapacidad'] = data[list(multiplicadores.keys())].max(axis=1)

# Multiplicar la columna 'puntos_discapacidad' por 0.25
data['puntos_discapacidad'] *= 0.35

# Ordenar el DataFrame por la columna 'puntos_discapacidad' de mayor a menor
data = data.sort_values(by='puntos_discapacidad', ascending=False)

data['id_usuario'] = [f'{i+1:04}' for i in range(len(data))]

# Mostrar el DataFrame ordenado por 'puntos_discapacidad'
print(data[['puntos_discapacidad', 'id_usuario']])

# Leer las tablas desde SQL
tabla_esperanza_de_vida_provincia_sexo = pd.read_sql_table('tabla_esperanza_de_vida_provincia_sexo', engine)
tabla_edad_sexo = pd.read_sql_table('tabla_edad_sexo', engine)

# Combinar DataFrames basados en 'id_provincia'
merged_data = pd.merge(tabla_edad_sexo, tabla_esperanza_de_vida_provincia_sexo, on='id_provincia')

# Calcular la esperanza de vida en días
def calcular_esperanza_vida(row):
    provincia = row['id_provincia']
    sexo = row['sexo']

    # Obtener el valor correspondiente de 'tabla_esperanza_de_vida_provincia_sexo'
    valor_esperanza = tabla_esperanza_de_vida_provincia_sexo[tabla_esperanza_de_vida_provincia_sexo['id_provincia'] == provincia]

    # Obtener la esperanza de vida basada en el sexo y el valor de 'hombres' o 'mujeres'
    if sexo == 'Hombre':
        esperanza_vida_anios = valor_esperanza['hombres'].values[0]
    else:
        esperanza_vida_anios = valor_esperanza['mujeres'].values[0]

    # Calcular esperanza de vida en días
    esperanza_vida_dias = float(esperanza_vida_anios) * 365  # Convertir a número y multiplicar por 365

    return esperanza_vida_dias

# Calcular los días de vida restantes
def calcular_dias_restantes(row):
    esperanza_vida = row['esperanza_vida']
    edad_en_dias = row['edad_en_dias']
    enfermedad_terminal = row['enfermedad_terminal_en_dias']  # Nueva columna de edad terminal

    # Si existe un valor en 'enfermedad_terminal_en_dias', reemplazar días_restantes con ese valor
    if not pd.isnull(enfermedad_terminal):
        dias_restantes = enfermedad_terminal
    else:
        # Calcular días restantes de vida
        dias_restantes = esperanza_vida - edad_en_dias

    return dias_restantes

# Calcular el porcentaje de vida recorrido
def calcular_puntos_esperanza(row):
    esperanza_vida = row['esperanza_vida']
    edad_en_dias = row['edad_en_dias']

    # Calcular porcentaje de vida recorrido
    puntos_esperanza = (edad_en_dias / esperanza_vida) * 100

    return puntos_esperanza

# Calcular la esperanza de vida, días restantes y porcentaje de vida recorrido
merged_data['esperanza_vida'] = merged_data.apply(calcular_esperanza_vida, axis=1)
merged_data['dias_restantes'] = merged_data.apply(calcular_dias_restantes, axis=1)
merged_data['puntos_esperanza'] = merged_data.apply(calcular_puntos_esperanza, axis=1)

# Limitar los valores de 'puntos_esperanza' a un máximo de 100
merged_data['puntos_esperanza'] = merged_data['puntos_esperanza'].clip(upper=100)

# Multiplicar 'puntos_esperanza' por 0.15
merged_data['puntos_esperanza'] *= 0.25


merged_data['id_usuario'] = [f'{i+1:04}' for i in range(len(merged_data))]

# Mostrar el resultado con los campos relevantes
print(merged_data[['puntos_esperanza', 'id_usuario']])

#################################-----VIAJES--------###############################

# Consulta SQL para obtener los datos de 'tabla_diferencia_fechas_viajes'
consulta_sql = "SELECT fecha_ultimo_viaje FROM tabla_diferencia_fechas_viajes"

# Ejecutar la consulta y obtener los datos en un DataFrame de pandas
datos = pd.read_sql_query(consulta_sql, engine)

# Obtener la fecha de hoy
fecha_hoy = datetime.datetime.now()

# Calcular la diferencia entre la fecha actual y 'fecha_ultimo_viaje'
datos['fecha_ultimo_viaje'] = pd.to_datetime(datos['fecha_ultimo_viaje'])  # Convertir la columna a tipo datetime si no está en ese formato
datos['diferencia_dias'] = (fecha_hoy - datos['fecha_ultimo_viaje']).dt.days  # Calcular la diferencia en días

# Aplicar las condiciones para calcular los puntos del viaje
datos['puntos_diferencia_viajes'] = datos['diferencia_dias'] * 0.2739726  # Multiplicar por 0.2739726

# Aplicar la condición de asignar 100 puntos si la diferencia es mayor a 365
datos.loc[datos['diferencia_dias'] > 365, 'puntos_diferencia_viajes'] = 100
datos['puntos_diferencia_viajes'] *= 0.15  # Multiplicar por 0.1


datos['id_usuario'] = [f'{i+1:04}' for i in range(len(datos))]

# Mostrar los resultados
print(datos[['puntos_diferencia_viajes', 'id_usuario']])

################################-----COMPROMISO---###########################

# Consulta SQL para obtener los datos de 'tabla_compromiso_usuario'
consulta_sql = "SELECT valoracion_usuario, fecha_cancelacion FROM tabla_compromiso_usuario"

# Ejecutar la consulta y obtener los datos en un DataFrame de pandas
datos_compromiso = pd.read_sql_query(consulta_sql, engine)

# Obtener la fecha de hoy
fecha_hoy = datetime.datetime.now()

# Calcular la diferencia entre la fecha actual y 'fecha_cancelacion'
datos_compromiso['fecha_cancelacion'] = pd.to_datetime(datos_compromiso['fecha_cancelacion'])  # Convertir la columna a tipo datetime si no está en ese formato
datos_compromiso['diferencia_dias'] = (fecha_hoy - datos_compromiso['fecha_cancelacion']).dt.days  # Calcular la diferencia en días

# Calcular la variable 'cancelacion' según las condiciones dadas
datos_compromiso['cancelacion'] = datos_compromiso['diferencia_dias'].apply(lambda x: 0 if x <= 180 else 100)

# Calcular la variable 'puntos_compromiso' según la fórmula dada
datos_compromiso['puntos_compromiso'] = datos_compromiso['valoracion_usuario'] * 0.7 + datos_compromiso['cancelacion'] * 0.3
datos_compromiso['puntos_compromiso'] *= 0.25

# Creamos una columna 'id_usuario' que asigna un valor incremental desde 0001 hasta el máximo de la base de datos

datos_compromiso['id_usuario'] = [f'{i+1:04}' for i in range(len(datos_compromiso))]


# Mostrar los resultados
print(datos_compromiso[['puntos_compromiso', 'id_usuario']])

# Unir todos los DataFrames en uno solo
all_data = pd.concat([data[['puntos_discapacidad', 'id_usuario']],
                      merged_data[['puntos_esperanza', 'id_usuario']],
                      datos[['puntos_diferencia_viajes', 'id_usuario']],
                      datos_compromiso[['puntos_compromiso', 'id_usuario']]])

# Generar una columna 'id_usuario' común con la longitud máxima de todos los DataFrames
max_length = max(len(data), len(merged_data), len(datos), len(datos_compromiso))
id_usuario_comun = pd.Series([f'{i+1:04}' for i in range(max_length)], name='id_usuario')

# Asignar la serie 'id_usuario_comun' a cada DataFrame
data['id_usuario'] = id_usuario_comun
merged_data['id_usuario'] = id_usuario_comun
datos['id_usuario'] = id_usuario_comun
datos_compromiso['id_usuario'] = id_usuario_comun

# Unir todos los DataFrames en uno solo con la columna 'id_usuario' común
all_data = pd.concat([data[['puntos_discapacidad', 'id_usuario']],
                      merged_data[['puntos_esperanza', 'id_usuario']],
                      datos[['puntos_diferencia_viajes', 'id_usuario']],
                      datos_compromiso[['puntos_compromiso', 'id_usuario']]])

# Insertar los datos en la tabla 'tabla_puntos'
all_data.to_sql('tabla_puntos', con=engine, if_exists='replace', index=False)



