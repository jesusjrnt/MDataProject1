
from sqlalchemy import create_engine
import mysql.connector

# Especifica tus credenciales y detalles de la base de datos MySQL
usuario = 'dataproject'  # El usuario predeterminado en XAMPP es 'root'
contrasena = 'dataproject'  # Deja la contraseña en blanco si no la has configurado
host = 'localhost'
base_datos = 'dataproject'  # Reemplaza con el nombre de tu base de datos en phpMyAdmin

# Crea la cadena de conexión a la base de datos usando sqlalchemy
cadena_conexion = f"mysql+mysqlconnector://dataproject:dataproject@localhost/dataproject"

# Crea el motor de la base de datos
motor = create_engine(cadena_conexion)

# Convierte el DataFrame a una tabla en la base de datos
df_bbdd.to_sql('nombre_de_la_tabla', con=motor, if_exists='replace', index=False)

# Si if_exists='replace', reemplazará la tabla si ya existe. Si prefieres agregar los datos, puedes usar if_exists='append'

# Cierra la conexión después de cargar los datos
motor.dispose()
