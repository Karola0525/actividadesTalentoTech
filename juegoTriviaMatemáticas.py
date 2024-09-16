import random

# Inicializar puntuación
puntuacion = 0

print("¡Bienvenido a la Trivia de Matemáticas!")
print("Responde las preguntas matemáticas y gana puntos.")

# Generar 5 preguntas aleatorias
for i in range(5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operacion = random.choice(['+', '-', '*', '/'])

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    else:
        # Para evitar divisiones por cero
        if num2 == 0:
            num2 = 1
        resultado = num1 // num2  # División entera

    # Pregunta al usuario
    respuesta = int(input(f"¿Cuánto es {num1} {operacion} {num2}? "))

    if respuesta == resultado:
        print("¡Correcto!")
        puntuacion += 1
    else:
        print(f"Incorrecto. La respuesta correcta era {resultado}.")

print(f"¡Juego terminado! Tu puntuación final es {puntuacion} de 5.")
5
