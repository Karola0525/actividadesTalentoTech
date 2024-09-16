import math
#Agregar mas opciones para próximo viernes, agregar ciclos para salir, swich case
# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no es posible"

# Función para calcular el logaritmo de un número
def logaritmo(a, base=10):
    if a > 0:
        return math.log(a, base)
    else:
        return "Error: El logaritmo de un número no positivo no es posible"

# Función para calcular el coseno de un número (en radianes)
def coseno(a):
    return math.cos(a)

# Función principal que ejecuta la calculadora
def calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Logaritmo")
    print("6. Coseno")

    # Entrada de la operación elegida
    eleccion = input("Introduce el número de la operación (1/2/3/4/5/6): ")

    # Realizar la operación correspondiente
    if eleccion in ['1', '2', '3', '4']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if eleccion == '1':
            print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
        elif eleccion == '2':
            print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
        elif eleccion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif eleccion == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")

    elif eleccion == '5':
        num = float(input("Introduce el número: "))
        base = input("Introduce la base del logaritmo (presiona Enter para base 10): ")
        if base == '':
            base = 10
        else:
            base = float(base)
        print(f"Resultado: log_{base}({num}) = {logaritmo(num, base)}")

    elif eleccion == '6':
        num = float(input("Introduce el ángulo en radianes: "))
        print(f"Resultado: cos({num}) = {coseno(num)}")

    else:
        print("Opción no válida")

# Ejecutar la calculadora
calculadora()
