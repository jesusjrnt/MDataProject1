import pandas as pd
from datetime import datetime

# Cargar el archivo CSV en un DataFrame
nombre_archivo = 'base_de_datos.csv'
data = pd.read_csv(nombre_archivo)

# Convertir las columnas relevantes a tipos de datos apropiados si es necesario
data['Valoracion_usuario'] = pd.to_numeric(data['Valoracion_usuario'], errors='coerce')
data['Fecha_cancelacion'] = pd.to_datetime(data['Fecha_cancelacion'], errors='coerce')

# Rellenar los valores NaN en 'Fecha_cancelacion' con la fecha actual
data['Fecha_cancelacion'].fillna(datetime.now().strftime('%Y-%m-%d'), inplace=True)

# Calcular la diferencia de fechas en días para 'punto_compromiso'
fecha_actual = datetime.now()
data['diferencia_dias'] = (fecha_actual - pd.to_datetime(data['Fecha_cancelacion'])).dt.days

# Calcular el campo 'punto_compromiso' según las condiciones dadas
data['punto_compromiso'] = data['Valoracion_usuario'] * 0.7 + 0.3 * (data['diferencia_dias'].apply(lambda x: 0 if x <= 180 else 100))

# Mostrar el DataFrame con el campo 'punto_compromiso' calculado
print(data[['Nombre', 'Apellido1', 'Apellido2', 'Fecha_cancelacion', 'Valoracion_usuario', 'diferencia_dias', 'punto_compromiso']])

# Definir los multiplicadores para cada tipo de discapacidad
multiplicadores = {
    'D_Movilidad': 1.0,
    'D_Aprendizaje': 0.8,
    'D_Comunicacion': 0.8,
    'D_Relaciones_sociales': 0.6,
    'D_Autocuidado': 0.6,
    'D_Vision': 0.5,
    'D_Audicion': 0.5,
    'D_Vida_domestica': 0.5  # Reemplazar 'D_vida_domestica' por 'D_Vida_domestica' si es necesario
}

# Multiplicar las columnas por sus respectivos multiplicadores para discapacidad
for col, mult in multiplicadores.items():
    data[col] *= mult

# Obtener la columna 'puntos_discapacidad' con el valor máximo de las columnas multiplicadas
data['puntos_discapacidad'] = data[list(multiplicadores.keys())].max(axis=1)

# Ordenar el DataFrame por la columna 'puntos_discapacidad' de mayor a menor
data = data.sort_values(by='puntos_discapacidad', ascending=False)

# Mostrar el DataFrame ordenado por 'puntos_discapacidad'
print(data[['puntos_discapacidad']])

# Cargar los archivos CSV en DataFrames
base_datos = pd.read_csv('base_de_datos.csv')
esperanza = pd.read_csv('esperanza.csv')

# Verificar valores únicos de 'id_provincia'
print(base_datos['id_provincia'].unique())
print(esperanza['id_provincia'].unique())

# Verificar relación entre 'Sexo' en 'base_de_datos.csv' y 'Hombres', 'Mujeres' en 'esperanza.csv'
sexo_base_datos = base_datos['Sexo'].unique()
print(esperanza[esperanza['Hombres'].isin(sexo_base_datos) | esperanza['Mujeres'].isin(sexo_base_datos)])

# Corregir discrepancias si las hay, ajustar los datos para que coincidan adecuadamente

# Combinar los DataFrames basándose en 'id_provincia'
merged_data = pd.merge(base_datos, esperanza, on='id_provincia')

# Calcular la esperanza de vida en días
def calcular_esperanza_vida(row):
    provincia = row['id_provincia']
    sexo = row['Sexo']

    # Obtener el valor correspondiente de 'esperanza.csv'
    valor_esperanza = esperanza[(esperanza['id_provincia'] == provincia)]

    # Obtener la esperanza de vida basada en el sexo y el valor de 'Hombres' o 'Mujeres'
    if sexo == 'Hombre':
        esperanza_vida_anios = valor_esperanza.iloc[0]['Hombres']
    else:
        esperanza_vida_anios = valor_esperanza.iloc[0]['Mujeres']

    # Calcular esperanza de vida en días
    esperanza_vida_dias = esperanza_vida_anios * 365

    return esperanza_vida_dias

# Calcular los puntos de esperanza (antes puntos_esperanza)
def calcular_queda_vida(row):
    enfermedad_terminal_en_dias = row['Enfermedad_terminal_en_dias']
    edad_en_dias = row['Edad_en_dias']

    # Sustituir 'esperanza_vida' por 'enfermedad_terminal_en_dias' si hay enfermedad terminal
    if row['Enfermedad_terminal'] == 'si':
        esperanza_vida = enfermedad_terminal_en_dias
    else:
        esperanza_vida = row['esperanza_vida']

    # Calcular puntos de esperanza (antes vida_cumplida)
    queda_vida = esperanza_vida - edad_en_dias
    
    # Ajustar a 100 los valores negativos en queda_vida
    if queda_vida < 0:
        return 0
    
    return queda_vida

# Aplicar la función para calcular 'esperanza_vida' en días
merged_data['esperanza_vida'] = merged_data.apply(calcular_esperanza_vida, axis=1)

# Aplicar la función para calcular 'queda_vida' (antes puntos_esperanza)
merged_data['queda_vida'] = merged_data.apply(calcular_queda_vida, axis=1)

# Cambiar el nombre de vida_cumplida a puntos_esperanza
merged_data.rename(columns={'vida_cumplida': 'puntos_esperanza'}, inplace=True)

# Calcular el porcentaje de vida cumplido (antes vida_cumplida)
merged_data['puntos_esperanza'] = ((merged_data['esperanza_vida'] - merged_data['queda_vida']) / merged_data['esperanza_vida']) * 100

# Mostrar el resultado con los campos relevantes, incluyendo 'puntos_esperanza' (antes vida_cumplida)
print(merged_data[['id_provincia', 'Edad', 'Sexo', 'esperanza_vida', 'queda_vida', 'puntos_esperanza']])

# Código para el cálculo de puntos_viaje
# Convertir la columna 'Fecha_ultimo_viaje_realizado' al tipo datetime si no está en ese formato
data['Fecha_ultimo_viaje_realizado'] = pd.to_datetime(data['Fecha_ultimo_viaje_realizado'])

# Calcular la diferencia en días entre la fecha actual y 'Fecha_ultimo_viaje_realizado'
fecha_actual = datetime.now()
data['diferencia_dias'] = (fecha_actual - data['Fecha_ultimo_viaje_realizado']).dt.days

# Calcular la variable 'puntos_viaje' con las condiciones dadas
data['puntos_viaje'] = data['diferencia_dias'] * 0.2739726
data.loc[data['diferencia_dias'] >= 365, 'puntos_viaje'] = 100

# Ordenar el DataFrame por la columna 'puntos_viaje' de mayor a menor
data = data.sort_values(by='puntos_viaje', ascending=False)

# Mostrar el DataFrame con las nuevas variables calculadas
print(data[['Fecha_ultimo_viaje_realizado', 'diferencia_dias', 'puntos_viaje']])

# Calcular 'puntos_viaje', 'puntos_esperanza', 'puntos_discapacidad' y 'puntos_compromiso' según tus datos
# ...

# Sumar los puntos correspondientes
data['puntos_total'] = data['puntos_viaje'] + merged_data['puntos_esperanza'] + data['puntos_discapacidad'] + data['punto_compromiso']

# Seleccionar las columnas necesarias y ordenar según 'puntos_total' de forma descendente
result = data[['id_usuario', 'DNI', 'Nombre', 'Apellido1', 'puntos_total']].sort_values(by='puntos_total', ascending=False)

# Mostrar el resultado
print(result)




















