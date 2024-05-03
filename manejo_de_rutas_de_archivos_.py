'''
En ocasiones, necesitamos manipular rutas de archivo para trabajar con
archivos en diferentes ubicaciones o directorios. Python proporciona la
biblioteca os.path para manejar las rutas de archivo de manera
eficiente.'''

import os
# Obtener la ruta absoluta de un archivo
ruta_absoluta = os.path.abspath("datos.txt")
# Comprobar si un archivo existe
existe = os.path.exists("datos.txt")
# Obtener el nombre base de un archivo
nombre_base = os.path.basename("datos.txt")
# Unir dos rutas de archivo
ruta1 = "ruta1"
ruta2 = "ruta2"
ruta_completa = os.path.join(ruta1, ruta2)

'''
En este ejemplo, importamos la biblioteca os y utilizamos las funciones
y métodos proporcionados por os.path. Utilizamos abspath() para
obtener la ruta absoluta de un archivo, exists() para comprobar si un
archivo existe, basename() para obtener el nombre base de un archivo y
join() para unir dos rutas de archivo.'''