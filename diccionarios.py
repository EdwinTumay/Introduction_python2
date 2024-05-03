# crear un diccionario
puntajes = {'Juan': 95, 'Maria': 87, 'Pedro': 78, 'Ana': 92}

# Acceder a valores por clave
print(puntajes['Maria']) # SAlida: 87

# Modificar Valores
puntajes['Pedro'] = 82
print(puntajes)

# Agregar nuevos elementos
puntajes['Carlos'] = 88
print(puntajes)

# Eliminar elementos por clave
del puntajes['Ana']
print(puntajes)