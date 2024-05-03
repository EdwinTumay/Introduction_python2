# Busqueda lineal
def busqueda_lineal(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return True
    return False
# Ejemplo de uso
mi_lista = [4, 2, 6, 1, 8, 3]
resultado = busqueda_lineal(mi_lista, 6)
print(resultado)

# Busqueda binaria
def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return True
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False
# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 6, 8]
resultado = busqueda_binaria(mi_lista, 6)
print(resultado)

