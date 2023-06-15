#Ejercicio n_1:

def fraccion():
    while True:
        try:
            fract = input("Ingrese una fracción en formato X/Y, siendo X,Y números enteros positivos: ")
            x, y = map(int, fract.split('/'))
            if x < 0 or y <= 0 or x > y:
                raise ValueError
            return x, y
        
        except (ValueError, ZeroDivisionError):
            print("Datos ingresados invalidos. Vuelva a intentarlo.")


def gasolina_porcentaje(x, y):
    percentage = (x / y) * 100
    if percentage < 1:
        return 'E'
    elif percentage > 99:
        return 'F'
    else:
        return str(round(percentage)) + '%'


def main_p():
    x, y = fraccion()
    G_P = gasolina_porcentaje(x, y)
    print("Porcentaje de gasolina en el tanque:", G_P)


if __name__ == '__main__':
    main_p()


#Ejercicio n_2:

def obtener_calificaciones():
    while True:
        try:
            ingreso_notas = input("\n Ingrese notas separadas por comas: ")
            notas = ingreso_notas.split(',')
            convertir_notas = [int(notas) for notas in notas]
            return convertir_notas
        except ValueError:
            print("\n Ingreso de datos invalido. Por favor, realicelo correctamente.")


def main():
    notas_1 = obtener_calificaciones()
    print("Notas convertidas:", notas_1)


if __name__ == '__main__':
    main()

#Ejercicio n_3:

def triangulo_pascal(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n debe ser un entero positivo.")

    triangulo = []
    for i in range(n):
        fila = [1] * (i + 1)
        if i >= 2:
            prev_fila = triangulo[i - 1]
            for j in range(1, i):
                fila[j] = prev_fila[j - 1] + prev_fila[j]
        triangulo.append(fila)


    for fila in triangulo:
        print(" ".join(map(str, fila)))


def main():
    while True:
        try:
            n = int(input("Ingrese un numero de filas del triangulo de Pascal: "))
            triangulo_pascal(n)
            break
        except ValueError as e:
            print("Ingreso invalido.", str(e))
            continue


if __name__ == '__main__':
    main()


#Ejercicio n_4:

def longitud_ultima_palabra(string):
    if not isinstance(string, str):
        raise ValueError("El dato de entrada debe ser un tipo string.")

    string = string.strip()

    palabras = string.split()

    if len(palabras) == 0:
        return 0
    else:
        return len(palabras[-1])


def main():
    try:
        string = input("Ingrese un string: ")
        longitud = longitud_ultima_palabra(string)
        print("Longitud de la ultima palabra:", longitud)
    except ValueError as e:
        print("Entrada invalida:", str(e))


if __name__ == '__main__':
    main()

