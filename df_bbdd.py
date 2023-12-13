import pandas as pd
import random
import pickle
from faker import Faker
from datetime import datetime, timedelta
import numpy as np  # Para poder ponderar los sexos


# Le pedimos a faker que nos de datos de España, para que los nombres y apellidos sean más típicos de aquí
fake = Faker('es_ES')  # 'es_ES' es el código para España en Faker

# Función para calcular la letra del DNI en función del número
def calcular_letra(numero_dni):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return letras[numero_dni % 26]

# Lista de provincias en España
provincias_espana = [
    'Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Balears, Illes', 'Barcelona', 'Bizkaia',
        'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón', 'Ceuta', 'Ciudad Real', 'Córdoba', 'Coruña, A', 'Cuenca', 'Gipuzkoa',
        'Girona', 'Granada', 'Guadalajara', 'Huelva', 'Huesca', 'Jaén', 'La Rioja', 'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga', 
        'Melilla', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Palmas, Las', 'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife', 
        'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Zamora', 'Zaragoza'
]
# Lista de sexos
sexos = ['Hombre', 'Mujer']

# Necesitamos generar un diccionario con el id_provincia correspondiente para cada Provincia, desde Álava que es el 101 a Zaragoza que es el 152.
id_provincia = {
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

# Creamos listas para cada campo
nombres = []
apellido1 = []
apellido2 = []
sexo = []
correos = []
fecha_nacimiento = []
ano_nacimiento = []
telefono = []
provincias = []
dnis = []
d_movilidad = []
d_aprendizaje = []
d_comunicacion = []
d_relaciones_sociales = []
d_autocuidado = []
d_vision = []
d_audicion = []
d_vida_domestica = []

# Generamos datos aleatorios y los agregamos a las listas
for _ in range(1500):  # Cambia el número para generar 1500 registros
    datos_sexo = np.random.choice(['Hombre', 'Mujer'], p=[0.41, 0.59]) # Con esto tendremos el 59% de mujeres y el 41% de hombres
    sexo.append(datos_sexo)

    if datos_sexo=="Hombre": 
        nombre = fake.first_name_male() # Así le ponemos nombre de hombre a los que se asignen aleatoriamente como "Hombre"
    else:
        nombre = fake.first_name_female()
    
    nombres.append(nombre)

    primer_apellido = fake.last_name()
    apellido1.append(primer_apellido)

    segundo_apellido = fake.last_name()
    apellido2.append(segundo_apellido)


    
    fecha_nac = fake.date_of_birth(minimum_age=60, maximum_age=120)  # Generamos una fecha de nacimiento aleatoria
    fecha_nacimiento.append(datetime.strptime(fecha_nac.strftime('%Y-%m-%d'), '%Y-%m-%d').date())  # Convertimos a datetime.date
    ano_nacimiento.append(fecha_nac.strftime('%Y'))  # Añade el año de nacimiento
    correos.append(fake.email())
    telefono.append(fake.phone_number())
    provincia = fake.random_element(provincias_espana)  # Seleccionamos una provincia
    provincias.append(provincia)
    numero_dni = fake.random_int(min=10000000, max=99999999)  # Generamos un número de DNI aleatorio
    letra_dni = calcular_letra(numero_dni)  # Calculamos la letra correspondiente
    dni_completo = f"{numero_dni}-{letra_dni}"
    dnis.append(dni_completo)

    probabilidad_discapacidad = random.random()
    if probabilidad_discapacidad <= 0.9076:
        d_aprendizaje.append(0)
        d_audicion.append(0)
        d_autocuidado.append(0)
        d_comunicacion.append(0)
        d_movilidad.append(0)
        d_relaciones_sociales.append(0)
        d_vida_domestica.append(0)
        d_vision.append(0)
    else:
        d_aprendizaje.append(random.randint(0, 100) if random.random() > 0.9316 else 0)
        d_audicion.append(random.randint(0, 100) if random.random() > 0.8808 else 0)
        d_autocuidado.append(random.randint(0, 100) if random.random() > 0.8678 else 0)
        d_comunicacion.append(random.randint(0, 100) if random.random() > 0.9082 else 0)
        d_movilidad.append(random.randint(0, 100) if random.random() > 0.7670 else 0)
        d_relaciones_sociales.append(random.randint(0, 100) if random.random() > 0.9411 else 0)
        d_vida_domestica.append(random.randint(0, 100) if random.random() > 0.8054 else 0)
        d_vision.append(random.randint(0, 100) if random.random() > 0.8981 else 0)

# Convertir la fecha actual a datetime.date
fecha_actual = datetime.now().date()

# Calculamos la edad en días restando a la fecha de nacimiento
edades_en_dias = []
for fecha_nac in fecha_nacimiento:
    diferencia = fecha_actual - fecha_nac
    edad_en_dias = diferencia.days
    edades_en_dias.append(edad_en_dias)

# Calculamos la edad en años
edad = []
for fecha_nac in fecha_nacimiento:
    resta_años = fecha_actual.year - fecha_nac.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day): #Hay que tener en cuenta si ha pasado su cumpleaños
        resta_años -= 1
    edad.append(resta_años)

# Asignamos una probabilidad del 0,4216% de tener enfermedad terminal; valores sí/no.
enfermedad_terminal = ['Sí' if random.random() < 0.004216 else 'No' for _ in range(1500)]

# Una enfermedad terminal va de 1 a 180 días
enfermedad_terminal_dias = [random.randint(0, 180) if enfermedad == 'Sí' else 0 for enfermedad in enfermedad_terminal]

# Creamos el campo de valoración del 1 al 100 puntos (esto nos viene dado random)
valoracion_usuario = [random.randint(0, 100) for _ in range(1500)]

# Calculamos la fecha de la última cancelación, aunque solo existirá el 1% de las veces. (esto lo definimos nosotros)
fecha_cancelacion = [(datetime.now() - timedelta(days=random.randint(7, 730))).strftime('%Y-%m-%d') if random.random() < 0.01 else None for _ in range(1500)]

# Creamos un diccionario con los datos
data = {
    'nombre': nombres,
    'apellido1': apellido1,
    'apellido2': apellido2,
    'sexo': sexo,
    'fecha_nacimiento': fecha_nacimiento,
    'ano_nacimiento': ano_nacimiento,
    'email': correos,
    'telefono': telefono,
    'provincia': provincias,
    'nif': dnis,
    'd_aprendizaje': d_aprendizaje,
    'd_audicion': d_audicion,
    'd_autocuidado': d_autocuidado,
    'd_comunicacion': d_comunicacion,
    'd_movilidad': d_movilidad,
    'd_relaciones_sociales': d_relaciones_sociales,
    'd_vida_domestica': d_vida_domestica,
    'd_vision': d_vision,
    'edad_en_dias': edades_en_dias,
    'edad': edad,
    'enfermedad_terminal': enfermedad_terminal,
    'enfermedad_terminal_en_dias': enfermedad_terminal_dias,
    'valoracion_usuario': valoracion_usuario,
    'fecha_cancelacion': fecha_cancelacion

}

# Creamos un DataFrame que llamamos df_bbdd
df_bbdd = pd.DataFrame(data)

# Creamos una nueva columna 'id_provincia' con valores mapeados usando el diccionario id_provincia
df_bbdd['id_provincia'] = df_bbdd['provincia'].map(id_provincia)

# Creamos una columna 'id_usuario' que asigna un valor incremental desde 0001 hasta el máximo de la base de datos
df_bbdd['id_usuario'] = [f'{i+1:04}' for i in range(len(df_bbdd))]

# Guardar el DataFrame en un archivo usando pickle
with open('df_bbdd.pickle', 'wb') as f:
    pickle.dump(df_bbdd, f)

# Si quisieramos imprimir el DataFrame
print(df_bbdd)

# Si quisieramos ver todas las columnas sin truncar, podemos usar lo siguiente:
#<<<<<<< HEAD:bbdd.py
pd.set_option('display.max_columns', None)
print(df_bbdd)


# Guardar el DataFrame en un archivo CSV
df_bbdd.to_csv('base_de_datos.csv', index=False)


