'''
Estructura de funcion recursiva

Una función recursiva consta de dos componentes principales: el caso
base y el caso recursivo. El caso base es una condición que indica
cuándo detener las llamadas recursivas y devuelve un resultado
concreto. El caso recursivo es el paso en el que la función se llama a sí
misma para resolver un subproblema más pequeño. Veamos un ejemplo
básico
'''
#Factorial
def funcion_recursiva(n):
# Caso base
    if n == 0:
        return 1
    # Caso recursivo
    else:
        return n * funcion_recursiva(n - 1)
# Ejemplo de uso
resultado = funcion_recursiva(6)
print(resultado)


def suma_naturales(n):
    # Caso base
    if n == 0:
        return 0
    # Caso recursivo
    else:
        return n + suma_naturales(n - 1)
# Ejemplo de uso
resultado = suma_naturales(5)
print(resultado)


# Permutaciones
def permutaciones(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return [lista]
    l = []
    for  i in range(len(lista)):
        m = lista[i]
        lista_remanente = lista[:i] + lista[i+1:]
        for p in permutaciones(lista_remanente):
            l.append([m] + p)
    return l

nums = [1, 2, 3]
print(permutaciones(nums))
