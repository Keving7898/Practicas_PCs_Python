def s_tabla_producto():
    try:
        numero = int(input("Ingrese un entero entre 1 a 10: "))
        if numero < 1 or numero > 10:
            print("Dato inválido.Escriba un numero entero entre 1 a 10.")
            return
        
        archivo_fichero = f"tabla de-{numero}.txt"
        with open(archivo_fichero, 'w') as file:
            for i in range(1, 11):
                linea = f"{numero} x {i} = {numero * i}\n"
                file.write(linea)
        
        print(f"La tabla de multiplicación para {numero} ha sido guardada en {archivo_fichero}.")

    except ValueError:
        print("Dato inválido. Haga caso las instrucciones, intenta otra vez.")

def disp_tabla():
    try:
        numero= int(input("Ingrese un entero entre 1 a 10: "))
        if numero < 1 or numero > 10:
            print("Dato inválido.Escriba un numero entero entre 1 a 10.")
            return
        
        archivo_fichero = f"tabla de-{numero}.txt"
        try:
            with open(archivo_fichero, 'r') as file:
                tabla = file.read()
                print(tabla)

        except FileNotFoundError:
            print(f"Fichero {archivo_fichero} no existe.")

    except ValueError:
        print("Dato inválido. Haga caso las instrucciones, intenta otra vez..")

def display_line():
    try:
        numero= int(input("Ingrese un entero entre 1 a 10: "))
        if numero < 1 or numero > 10:
            print("Dato inválido.Escriba un numero entero entre 1 a 10.")
            return
        
        linea_numero = int(input("Ingrese un numero de linea: "))
        if linea_numero < 1 or linea_numero > 10:
            print("Dato inválido.Escriba un numero entero entre 1 a 10.")
            return
        
        archivo_fichero = f"tabla de-{numero}.txt"
        try:
            with open(archivo_fichero, 'r') as file_1:
                lineas = file_1.readlines()
                if linea_numero <= len(lineas):
                    print(lineas[linea_numero - 1])
                else:
                    print(f"linea {linea_numero} no existe en el archivo. ")
                    
        except FileNotFoundError:
            print(f"Archivo {archivo_fichero} does not exist.")

    except ValueError:
        print("Dato inválido. Haga caso las instrucciones, intenta otra vez..")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Guardar una tabla de multiplicación para un número ")
        print("2. Mostrar la multiplicación de cada numero ")
        print("3. Mostrar una linea específica de la tabal de multiplicación")
        print("4. Salir")
        choice = input("Escoga una de las opciones (1-4): ")

        if choice == '1':
            s_tabla_producto()
        elif choice == '2':
            disp_tabla()
        elif choice == '3':
            display_line()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

menu()