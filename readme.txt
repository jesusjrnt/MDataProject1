ARCHIVO bbdd.py
GENERAR DATAFRAME CON DATOS ALEATORIOS DE PERSONAS DE ESPAÑA
01
Instalamos Anaconda Navigator en nuestro ordenador para no tener que instalar las librerías más usadas manualmente tipo pandas o faker.
02
Importamos las librerías pandas y random para poder generar y almacenar en un dataframe de pandas datos.
Utilizamos faker para datos random y datetime para poder generar fechas
03
Le pedimos a faker que nos de datos de España, para que los nombres y apellidos sean más típicos de aquí
04
Para generar el DNI tenemos que generar un número aleatorio de 8 dígitos y añadirle una de las 26 letras del abecedario de forma aleatoria
05
Definimos las provincias de España: Para las provincias simplemente le listamos las 52 provincias de España tal y como nosotros hemos definido
06
- Después de importar hemos visto los campos iniciales que nos da y definimos los que necesitamos: separamos nombre y apellidos (apellido1 y apellido2), generamos dni, provincia, etc.
- La edad la vamos a tener en dos formatos: edad (en años) y edad_dias (en dias) - Los cálculos se harán en días y en años es simplemente a nivel visual para facilitar comprensión.
- Para calcular la edad en días tenemos que restar fecha actual y fecha de nacimiento. Para poder hacerlo hemos tenido que convertir los campos en el mismo tipo de objeto datetime.date
- Para el campo Enfermedad Terminal el porcentaje que lo representa. Según un artículo del país son 200.000 personas (https://elpais.com/sociedad/2009/05/28/actualidad/1243461607_850215.html)
- El porcentaje de terminales es 0,4216%; así que la bbdd tendrá un 0,4216% de probabilidad de incluir uno.
- El periodo de enf ermedad terminal no puede ser mayor a 6 meses (180 días). Fuente: Elsevier España, S.L.U. (2021). El período de agonía. Gaceta Mexicana de Oncología, 20(4), e305-e308. (https://www.elsevier.es/es-revista-gaceta-mexicana-oncologia-305-articulo-el-periodo-agonia-X1665920113269854)
- Para programarlo queremos: añadir un campo de valor numérico en días que se llame "Enfermedad terminal en días", en el que los datos puedan ir entre 0 y 180 días. Si 'Enfermedad terminal' es 0, "Enfermedad terminal en días" será 0. Si no, se genera un número aleatorio
- EL campo "fecha último viaje realizado" Como mínimo va a ser 7 días antes de la fecha actual. y como máximos será 2 años (730 días), para tener datos lógicos. (en las condiciones luego la máxima puntuacion es 365 días)
- El campo "fecha cancelación" es una fecha aleatoria con un intervalo entre 7 días y 730 días antes de la fecha actual. Este campo estará vacío el 99% de las veces.(esto lo definimos nosotros para tener datos con sentido)
- La cantidad de gente discapacitada en España son 4,38 millones de una población de 47,42 millones, es decir, un 9,24%.
- Nuestro dataframe representará una probabilidad del 9,24% de tener alguna discapacidad, es decir, un 90,76% de que todas las discapacidades sean 0.
- Además dentro de las personas discapacitadas conocemos estas probabilidades de tener cada una:
d_aprendizaje 6,84%
d_audicion 11,92%
d_autocuidado 13,22%
d_comunicacion 9,18%
d_movilidad 23,3%
d_relaciones_sociales 5,89%
d_vida_domestica 19,46%
d_vision 10,19%.
07
Generamos datos random para cada campo utilizando Bucles
08
Generamos un diccionario con todos los datos
09
Creamos dataframe para la generación de datos aleatorios
10
Para que el campo id_provincia siempre dependa del campo provincia y no varíe, hemos hecho una librería en la que cada provincia tiene una id
y entonces le sumamos la columna al dataframe, en lugar de generarla directamente junto al dataframe original directamente. (menos complicado)
11
Imprimir el dataframe (o df) para visualizar los datos que tenemos

_________________________________________________________________________

ARCHIVO esperanza_vida.py
GENERAR DATAFRAME A PARTIR DEL DATA SET OBTENIDO EN EL INE (ESPERANZA DE VIDA POR PROVINCIA Y SEXO)
01
Listamos las provincias y le ponemos un ID a cada provincia del 101 al 152
02
Añadimos los datos obtenidos de la esperanza de vida para cada provincia según sexo
03
creamos el dataframe que llamamos df_esperanza_vida
04
Imprimimos el dataframe para confirmar que se ve todo bien

_________________________________________________________________________

ARCHIVO tipo_viaje.py
GENERAR DATAFRAME CON ID_USUARIO Y LOS 5 ULTIMOS VIAJES REALIZADOS POR FECHA Y TIPO
01
Listamos los 4 tipos de viaje posibles
02
Generamos los 5 tipos de viaje con fecha y tipo; esto generará dos campos para cada viaje.
03
Al generar las fechas ordenamos con SORTED para que vayan por orden cronológico, y el primero siempre sea antes que el segundo, tercero, etc.
04
Obtenemos una tabla con id_usuario, 5 tipos de viajes aleatorios con su tipo y fecha. Y no necesariamente han realizado todos.
05
Aprovechamos este dataframe para obtener una columna más: fecha_ultimo_viaje; que se calcula cogiendo la fecha más reciente de todos los viajes.
06
Aprovechamos este dataframe para obtener una columna más: tipo_ultimo_viaje; que lo coge del viaje más reciente.

_________________________________________________________________________

ARCHIVO conectorbbdd.py

01
Instalamos los módulos que necesitamos.
Estos módulos los necesitamos para pasar la base de datos generada en Python a MySQL para poder visualizarla en phpMyAdmin.

pip install sqlalchemy
pip install mysql.connector

02
Para hacer funcionar phpMyAdmin en local necesitamos XAMPP:
https://www.apachefriends.org/es/download.html

03
Una vez instalado XAMPP lo abriremos y le pediremos que empiece los siguientes procesos:
- MySQL Database
- Apache web server

04
Entramos en la siguiente página:
localhost/dashboard

05
Ahí vamos a phpMyAdmin

06
usuario: dataproject
contraseña: dataproject
host: localhost
nombre bbdd: dataproject

_________________________________________________________________________

ARCHIVO creacion_tablas.sql
RESUMEN DE CADA TABLA CREADA

Equilibrio_discapacidad:
Columnas: id_equilibrio_discapacidad, id_usuario, Movilidad, Aprendizaje, Comunicacion, Relaciones_sociales, Autocuidado, Vision, Audicion, Vida_domestica

Esperanza_de_vida:
Columnas: id_esperanza_de_vida, id_provincia, provincia, sexo, edad_en_dias, Enfermedad_terminal_en_dias

Diferencia_fechas_viajes:
Columnas: id_diferencia_fechas_viajes, id_usuario, fecha_ultimo_viaje

Compromiso_usuario:
Columnas: id_compromiso_usuario, id_usuario, valoracion_usuario, fecha_cancelacion

Promocion_Movilidad:
Columnas: id_promocion_movilidad, id_usuario, id_provincia

Tipo_de_viaje:
Columnas: id_tipo_de_viaje, id_usuario, tipo_viaje_1, tipo_viaje_2, tipo_viaje_3, tipo_viaje_4, tipo_viaje_5

Proximo_viaje:
Columnas: id_proximo_viaje, id_provincia, provincia, plazas_disponibles, tipo_de_viaje