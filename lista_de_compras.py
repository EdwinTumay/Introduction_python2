def main():
    shopping_listas = []

    while True:
        print("\n---Lista de Compras---")
        print("1. Agregar articulo")
        print("2. Eliminar articulo")
        print("3. Ver lista")
        print("4. Salir")

        option = input("Por favor introduzca una opción ")

        if option == "1":
            item = input("Introduce el nombre del articulo que quieres ingresar: ")
            shopping_listas.append(item)
        elif option == "2":
            item = input("Introduce el nombre del articulo que quieres eliminar: ")
            shopping_listas.remove(item)
        elif option == "3":
            if shopping_listas:  # Verifica si la lista no está vacía
                print("\nTu lista de compras es: ")
                for item in shopping_listas:
                    print("- " + item)
            else:
                print("\nTu lista de compras está vacía.")
        elif option == "4":
            break
        else:
            print("Opción inválida. Por favor intenta de nuevo.")
    
if __name__ == "__main__":
    main()
