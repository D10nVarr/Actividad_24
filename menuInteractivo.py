digitos=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n-1)

def secuencia_Fibonacci(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    else:
        return secuencia_Fibonacci(n-1)+secuencia_Fibonacci(n-2)

def contador_letras(palabra, letra):
    if palabra=="":
        return 0

    if palabra[0]==letra:
        return 1 + contador_letras(palabra[1:], letra)
    else:
        return contador_letras(palabra[1:], letra)

def invertir_texto(palabra):
    if palabra=="":
        return ""
    else:
        return invertir_texto(palabra[1:]) + palabra[0]

def potencia(n,exp):
    if exp==0:
        return 1
    else:
        return n*potencia(n,exp-1)



while True:
    print("___Bienvenido al menu de opciones___")
    print("1. Calcular el factorial de un numero")
    print("2. Calcular la suma de todos los numeros naturales hasta el deseado")
    print("3. Calcular la secuencia de Fibonacci")
    print("4. Contador de letras")
    print("5. Invertir texto")
    print("6. Calcular una potencia")
    print("7. Salir")

    opcion=input("\nSeleccione una opción: ")

    match opcion:
        case "1":
            print("Calcualar el factorial de un numero")
            try:
                numero = int(input("\nIngrese su número: "))
                if numero>=0:
                    print(f"El factorial de {numero} es {factorial(numero)}\n")
                else:
                    print("El numero debe ser un entero positivo\n")

            except ValueError:
                print("El numero debe ser un entero positivo\n")

        case "2":
            print("Suma de numero naturales hasta el deseado")

            try:
                numero=int(input("\nIngrese su número natural: "))

                if numero>=0:
                    print(f"La suma de todos los numeros naturales hasta {numero} es {suma_naturales(numero)}\n")
                else:
                    print("El numero debe ser un entero positivo\n")
            except ValueError:
                print("El numero debe ser un entero positivo\n")

        case "3":
            print("Calcular la secuencia de Fibonacci en la posición deseada")

            try:
                posicion=int(input("\nIngrese la posicion Fibonacci que desee conocer: "))
                if posicion>=0:
                    print(f"El numero de Fibonacci en la posición {posicion} es {secuencia_Fibonacci(posicion)}\n")

                else:
                    print("La posición debe ser un entero positivo\n")

            except ValueError:
                print("El numero debe ser un entero positivo\n")

        case "4":
            print("Contar letras dentro de una palabra")

            palabra=str(input("\nIngrese una palabra: "))
            letra=input("Ingrese una letra: ")

            if palabra.strip()=="" or letra.strip()=="":
                print("Ninguno de los campos debe quedar vacio\n")

            elif len(letra) != 1:
                print("Solo se debe ingresar una letra\n")

            elif letra.isdigit():
                print("Se debe ingresar una letra\n")

            else:
                numeros=False
                for i in palabra:
                    if i in digitos:
                        numeros=True
                        break

                if numeros:
                    print("La palabra no debe contener números\n")

                else:
                    print(f"La letra '{letra}' se encuentra {contador_letras(palabra, letra)} veces dentro de la palabra {palabra}\n")

        case "5":
            print("Invertir una cadena de texto")

            texto=input("\nIngrese una cadena de texto: ")

            if texto.strip()=="":
                print("Debe ingresar un texto\n")

            elif texto.isdigit():
                print("No se deben ingresar numeros\n")

            else:
                print(f"El texto invertido es '{invertir_texto(texto)}'\n")

        case "6":
            print("Potencia de un número")

            try:
                base=int(input("\nIngrese el número: "))
                exponente=int(input("Ingrese el exponente: "))

                if exponente>0:
                    print(f"La potencia es de {potencia(base,exponente)}\n")
                else:
                    print("El exponente debe ser un entero positivo\n")

            except ValueError:
                print("Se deben ingresar números\n")

        case "7":
            print("Saliendo del programa")

        case _:
            print("Opción no válida")