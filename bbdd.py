import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Le pedimos a faker que nos de datos de España, para que los nombres y apellidos sean más típicos de aquí
fake = Faker('es_ES')  # 'es_ES' es el código para España en Faker

# Función para calcular la letra del DNI en función del número
def calcular_letra(numero_dni):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return letras[numero_dni % 26]

# Lista de provincias en España
provincias_espana = [
    'Álava', 'Albacete', 'Alicante', 'Almería', 'Ávila', 'Badajoz', 'Balears, Illes', 'Barcelona',
    'Burgos', 'Cáceres', 'Cádiz', 'Castellón', 'Ciudad Real', 'Córdoba', 'Coruña, A', 'Cuenca',
    'Girona', 'Granada', 'Guadalajara', 'Gipuzkoa', 'Huelva', 'Huesca', 'Jaén', 'León', 'Lleida',
    'La Rioja', 'Lugo', 'Madrid', 'Málaga', 'Murcia', 'Navarra', 'Ourense', 'Asturias', 'Palencia',
    'Palmas, Las', 'Pontevedra', 'Salamanca', 'Santa Cruz de Tenerife', 'Cantabria', 'Segovia',
    'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Bizkaia',
    'Zamora', 'Zaragoza', 'Ceuta', 'Melilla'
]

# Creamos listas para cada campo
nombres = []
apellido1 = []
apellido2 = []
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
for _ in range(10):  # Cambia el número para generar 10 registros
    nombre_completo = fake.name().split()  # Obtenemos el nombre y lo divididimos en nombre, apellido1 y apellido2
    nombres.append(nombre_completo[0])  # Primer nombre
    if len(nombre_completo) > 1:
        apellido1.append(nombre_completo[1])  # Primer apellido
    else:
        apellido1.append("")
    if len(nombre_completo) > 2:
        apellido2.append(nombre_completo[2])  # Segundo apellido
    else:
        apellido2.append("")
    fecha_nac = fake.date_of_birth(minimum_age=18, maximum_age=120)  # Generamos una fecha de nacimiento aleatoria
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
    d_movilidad.append(random.randint(0, 100))
    d_aprendizaje.append(random.randint(0, 100))
    d_comunicacion.append(random.randint(0, 100))
    d_relaciones_sociales.append(random.randint(0, 100))
    d_autocuidado.append(random.randint(0, 100))
    d_vision.append(random.randint(0, 100))
    d_audicion.append(random.randint(0, 100))
    d_vida_domestica.append(random.randint(0, 100))

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
enfermedad_terminal = ['Sí' if random.random() < 0.004216 else 'No' for _ in range(10)]

# Una enfermedad terminal va de 1 a 180 días
enfermedad_terminal_dias = [random.randint(0, 180) if enfermedad == 'Sí' else 0 for enfermedad in enfermedad_terminal]

# Calculamos la fecha del último viaje realizado, con dos condiciones: más de 7 días desde fecha actual y menos de 730 días (2 años)
fecha_ultimo_viaje = []
for _ in range(10):
    fecha_minima = datetime.now() - timedelta(days=7)
    fecha_maxima = datetime.now() - timedelta(days=730)

    fecha_viaje = fake.date_time_between(start_date=fecha_minima, end_date=fecha_maxima)
    fecha_ultimo_viaje.append(datetime.strptime(fecha_viaje.strftime('%Y-%m-%d'), '%Y-%m-%d').date())

# Creamos el campo de valoración del 1 al 100 puntos (esto nos viene dado random)
valoracion_usuario = [random.randint(0, 100) for _ in range(10)]

# Calculamos la fecha de la última cancelación, aunque solo existirá el 1% de las veces. (esto lo definimos nosotros)
fecha_cancelacion = [datetime.now() - timedelta(days=random.randint(7, 730)) if random.random() < 0.01 else None for _ in range(10)]


# Creamos un diccionario con los datos
data = {
    'Nombre': nombres,
    'Apellido1': apellido1,
    'Apellido2': apellido2,
    'Fecha de nacimiento': fecha_nacimiento,
    'Año de nacimiento': ano_nacimiento,
    'Correo': correos,
    'Teléfono': telefono,
    'Provincia': provincias,
    'DNI': dnis,
    'D_Movilidad': d_movilidad,
    'D_Aprendizaje': d_aprendizaje,
    'D_Comunicación': d_comunicacion,
    'D_Relaciones sociales': d_relaciones_sociales,
    'D_Autocuidado': d_autocuidado,
    'D_Visión': d_vision,
    'D_Audición': d_audicion,
    'D_Vida doméstica': d_vida_domestica,
    'Edad en días': edades_en_dias,
    'Edad': edad,
    'Enfermedad terminal': enfermedad_terminal,
    'Enfermedad terminal en días': enfermedad_terminal_dias,
    'Fecha último viaje realizado': fecha_ultimo_viaje,
    'Valoración usuario': valoracion_usuario,
    'Fecha cancelación': fecha_cancelacion

}



# Creamos un DataFrame que llamamos df_bbdd
df_bbdd = pd.DataFrame(data)

# Imprimimos el DataFrame
print(df_bbdd)
