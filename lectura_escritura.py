# 1.fLectura de un archivo:
# Abrir un archivo en modo lectura
archivo = open("datos.txt", "r")
# Leer el contenido del archivo
contenido = archivo.read()
# Cerrar el archivo
archivo.close()

# 2.Escritura en un archivo:
# Abrir un archivo en modo escritura
archivo = open("datos.txt", "w")
# Escribir en el archivo
archivo.write("Hola, mundo!")
# Cerrar el archivo
archivo.close()
