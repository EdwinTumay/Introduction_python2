'''
Para conectarnos a una base de datos en Python, necesitamos utilizar
una biblioteca específica que admita el motor de base de datos que
estamos utilizando. Algunas bibliotecas populares para la conexión a
bases de datos en Python son sqlite3, MySQL Connector, psycopg2
(para PostgreSQL), entre otras. A continuación, presentaremos un
ejemplo utilizando sqlite3'''

import sqlite3
# Establecer una conexión a la base de datos
conexion = sqlite3.connect('basedatos.db')
# Realizar operaciones en la base de datos
# Cerrar la conexión a la base de datos
conexion.close()

'''
En este ejemplo, importamos la biblioteca sqlite3 y utilizamos la función
connect() para establecer una conexión a la base de datos basedatos.db.
Luego, podemos realizar operaciones en la base de datos, como
consultas y modificaciones. Finalmente, cerramos la conexión utilizando
el método close().'''
