#crear un juego con instrucciones
import random

# Generar un número secreto entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0
print("¡Bienvenido al juego de 'Adivina el Número'!")
print("Intenta adivinar el número secreto entre 1 y 100.")

# Bucle para adivinar el número
while True:
    intento = int(input("Introduce tu conjetura: "))
    intentos += 1

    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
        break
