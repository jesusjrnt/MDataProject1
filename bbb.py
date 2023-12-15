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
data['puntos_discapacidad'] *= 0.25

# Ordenar el DataFrame por la columna 'puntos_discapacidad' de mayor a menor
data = data.sort_values(by='puntos_discapacidad', ascending=False)

# Mostrar el DataFrame ordenado por 'puntos_discapacidad'
print(data[['puntos_discapacidad']])

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
merged_data['puntos_esperanza'] *= 0.15

# Mostrar el resultado con los campos relevantes
print(merged_data[['puntos_esperanza']])

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
datos['puntos_viajes'] = datos['diferencia_dias'] * 0.2739726  # Multiplicar por 0.2739726

# Aplicar la condición de asignar 100 puntos si la diferencia es mayor a 365
datos.loc[datos['diferencia_dias'] > 365, 'puntos_viajes'] = 100
datos['puntos_viajes'] *= 0.1  # Multiplicar por 0.1
# Mostrar los resultados
print(datos[['puntos_viajes']])

################################-----COMPROMISO---###########################

# Consulta SQL para obtener los datos de 'tabla_compromiso_usuario'
consulta_sql = "SELECT valoracion_usuario, fecha_cancelacion FROM tabla_compromiso_usuario"

# Ejecutar la consulta y obtener los datos en un DataFrame de pandas
datos = pd.read_sql_query(consulta_sql, engine)

# Obtener la fecha de hoy
fecha_hoy = datetime.datetime.now()

# Calcular la diferencia entre la fecha actual y 'fecha_cancelacion'
datos['fecha_cancelacion'] = pd.to_datetime(datos['fecha_cancelacion'])  # Convertir la columna a tipo datetime si no está en ese formato
datos['diferencia_dias'] = (fecha_hoy - datos['fecha_cancelacion']).dt.days  # Calcular la diferencia en días

# Calcular la variable 'cancelacion' según las condiciones dadas
datos['cancelacion'] = datos['diferencia_dias'].apply(lambda x: 0 if x <= 180 else 100)

# Calcular la variable 'puntos_compromiso' según la fórmula dada
datos['puntos_compromiso'] = datos['valoracion_usuario'] * 0.7 + datos['cancelacion'] * 0.3
datos['puntos_compromiso'] *= 0.2
# Mostrar los resultados
print(datos[['puntos_compromiso']])

##########################-----MOVILIDAD----#######################

consulta_sql = """
SELECT 
    CASE WHEN pm.id_provincia = pv.provincia THEN 0 ELSE 100 END AS puntos_movilidad
FROM tabla_promocion_movilidad pm, tabla_proximo_viaje pv
"""

# Ejecutar la consulta y obtener los datos en un DataFrame de pandas
datos = pd.read_sql_query(consulta_sql, engine)
datos['puntos_movilidad']*= 0.15
# Imprimir los resultados de la variable 'puntos_movilidad'
print(datos['puntos_movilidad'])

############-----TIPO-VIAJE---############

consulta_sql = """
SELECT 
    CASE 
        WHEN tp.tipo_de_viaje = tv.tipo_viaje_1 THEN 100 - 25
        WHEN tp.tipo_de_viaje = tv.tipo_viaje_2 THEN 100 - 50
        WHEN tp.tipo_de_viaje = tv.tipo_viaje_3 THEN 100 - 75
        WHEN tp.tipo_de_viaje = tv.tipo_viaje_4 THEN 100 - 100
        ELSE 100 
    END AS puntos_tipo_viaje
FROM tabla_tipo_de_viaje tv, tabla_proximo_viaje tp
"""

# Ejecutar la consulta y obtener los resultados en un DataFrame de pandas
datos = pd.read_sql_query(consulta_sql,engine)
datos['puntos_tipo_viaje']*= 0.15
# Mostrar los resultados de la variable 'puntos_tipo_viaje'
print(datos['puntos_tipo_viaje'])