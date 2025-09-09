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




while True:
    print("___Bienvenido al menu de opciones___")
    print("1. Calcular el factorial de un numero")
    print("2. Calcular la suma de todos los numeros naturales hasta el deseado")
    print("3. Calcular la secuencia de Fibonacci")
    print("4. Contador de letras")
    print("5. Invertir texto")

    opcion=input("\nSeleccione una opción: ")

    match opcion:
        case "1":
            print("Calcualar el factorial de un numero")
            numero = int(input("\nIngrese su número: "))
            print(f"El factorial de {numero} es {factorial(numero)}\n")

        case "2":
            print("Suma de numero naturales hasta el deseado")
            numero=int(input("Ingrese su número natural: "))
            print(f"La suma de todos los numeros naturales hasta {numero} es {suma_naturales(numero)}\n")

        case "3":
            print("Calcular la secuencia de Fibonacci en la posición deseada")
            posicion=int(input("Ingrese la posicion Fibonacci que desee conocer: "))

            print(f"El numero de Fibonacci en la posición {posicion} es {secuencia_Fibonacci(posicion)}\n")

        case "4":
            print("Contar letras dentro de una palabra")

            palabra=input("Ingrese una palabra: ")
            letra=input("Ingrese una letra: ")

            print(f"La letra '{letra}' se encuentra {contador_letras(palabra, letra)} veces dentro de la palabra {palabra}\n")

        case "5":
            print("Invertir una cadena de texto")
            texto=input("Ingrese una cadena de texto: ")

            print(f"El texto invertido es '{invertir_texto(texto)}'\n")