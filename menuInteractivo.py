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
    numeros = [0, 1]

    if numeros[n-1]:
        return numeros[n]
    else:
        numeros.append(numeros[n-1] + numeros[n-2])
        return numeros[n-1] + numeros[n-2]

while True:
    print("___Bienvenido al menu de opciones___")
    print("1. Calcular el factorial de un numero")
    print("2. Calcular la suma de todos los numeros naturales hasta el deseado")
    print("3. Calcular la secuencia de Fibonacci")

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