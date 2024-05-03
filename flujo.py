inventario = {'manzana': 10, 'banana': 5, 'naranjas': 3, 'peras': 7}

def gestion_inventarios(accion, articulo, cantidad = 0):
    if accion == 'agragar':
        if articulo in inventario:
            inventario[articulo] += cantidad
        else:
            inventario[articulo] = cantidad
    elif accion == 'quitar':
        if articulo in inventario and inventario[articulo] >= cantidad:
            inventario[articulo] -= cantidad
        else:
            print('No se puede realizar la acción')
    elif accion == 'buscar':
        if articulo in inventario:
            return inventario[articulo]
        else:
            return None
    else:
        print('Acción no reconocida')

gestion_inventarios('agregar', 'manzanas', 5)
print(inventario)

gestion_inventarios('quitar', 'naranjas', 2)
print(inventario)

print(gestion_inventarios('buscar', 'peras'))