import sqlite3

# Ruta de la base de datos
ruta_basedatos = r'D:\Documents\__MACOSX\Diana Marcela\mi_basedatos.sqlite'

# Conectar a la base de datos
conexion = sqlite3.connect(ruta_basedatos)

# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Ejemplo: Realizar una consulta para obtener datos
cursor.execute('SELECT * FROM tabla_nombre')
datos = cursor.fetchall()

# Cerrar la conexión
conexion.close()

# Cargar la base de datos en un DataFrame (reemplaza ruta_basedatos con tu ruta)
ruta_basedatos = r'D:\Documents\__MACOSX\Diana Marcela\archivo.dta'
dataframe = pd.read_stata(ruta_basedatos)

# Calcular estadísticos descriptivos para todas las variables
descriptivos = dataframe.describe()

# Mostrar los estadísticos descriptivos
print(descriptivos)
