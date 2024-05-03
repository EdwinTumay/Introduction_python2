'''
En ocasiones, necesitamos manipular rutas de archivo para trabajar con
archivos en diferentes ubicaciones o directorios. Python proporciona la
biblioteca os.path para manejar las rutas de archivo de manera
eficiente'''

# Leer el contenido del archivo
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()
# Dividir el contenido en líneas
lineas = contenido.split("\n")
# Unir las líneas con un separador
nuevo_contenido = "\n".join(lineas)

'''
En este ejemplo, leemos el contenido del archivo "datos.txt" y lo
almacenamos en la variable contenido. Luego, utilizamos el método
split() para dividir el contenido en líneas utilizando el carácter de salto
de línea ("\n"). Después, utilizamos el método join() para unir las líneas
nuevamente con el carácter de salto de línea, almacenando el resultado
en la variable nuevo_contenido'''