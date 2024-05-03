'''
Una vez establecida la conexión a la base de datos, podemos realizar
consultas y manipulaciones de datos utilizando sentencias SQL. A
continuación, presentaremos un ejemplo básico de consulta utilizando
sqlite3:'''

import sqlite3
# Establecer una conexión a la base de datos
conexion = sqlite3.connect('basedatos.db')
# Crear un cursor para ejecutar las consultas
cursor = conexion.cursor()
# Ejecutar una consulta SELECT
cursor.execute("SELECT * FROM usuarios")
# Obtener los resultados de la consulta
resultados = cursor.fetchall()
# Mostrar los resultados
for resultado in resultados:
 print(resultado)
# Cerrar el cursor y la conexión a la base de datos
cursor.close()
conexion.close()

'''
EEn este ejemplo, después de establecer la conexión a la base de datos,
creamos un cursor utilizando el método cursor() de la conexión. Luego,
ejecutamos una consulta SELECT utilizando el método execute() del
cursor y obtenemos los resultados utilizando el método fetchall().
Finalmente, recorremos los resultados y los mostramos en la consola.'''