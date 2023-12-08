import pandas as pd
from faker import Faker

# Función para calcular la letra del DNI en función del número
def calcular_letra(numero_dni):
    letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return letras[numero_dni % 23]

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

# Creamos una instancia de Faker para generar datos ficticios para España
fake = Faker('es_ES')  # 'es_ES' es el código para España en Faker

# Creamos listas vacías para almacenar los datos generados
nombres = []
apellido1 = []
apellido2 = []
edades = []
correos = []
provincias = []
dnis = []

# Generamos datos aleatorios y los agregamos a las listas
for _ in range(10):  # Cambia el número para generar más o menos registros
    nombre_completo = fake.name().split()  # Obtenemos el nombre completo y lo dividimos en partes
    nombres.append(nombre_completo[0])  # Primer nombre
    if len(nombre_completo) > 1:
        apellido1.append(nombre_completo[1])  # Primer apellido
    else:
        apellido1.append("")
    if len(nombre_completo) > 2:
        apellido2.append(nombre_completo[2])  # Segundo apellido
    else:
        apellido2.append("")
    edades.append(fake.random_int(min=18, max=80))
    correos.append(fake.email())
    provincia = fake.random_element(provincias_espana)  # Seleccionamos una provincia de la lista
    provincias.append(provincia)
    numero_dni = fake.random_int(min=10000000, max=99999999)  # Generamos un número de DNI aleatorio
    letra_dni = calcular_letra(numero_dni)  # Calculamos la letra correspondiente
    dni_completo = f"{numero_dni}-{letra_dni}"
    dnis.append(dni_completo)

# Creamos un diccionario con los datos
data = {
    'Nombre': nombres,
    'Apellido1': apellido1,
    'Apellido2': apellido2,
    'Edad': edades,
    'Correo': correos,
    'Provincia': provincias,
    'DNI': dnis
}

# Creamos un DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Mostramos el DataFrame
print(df)
