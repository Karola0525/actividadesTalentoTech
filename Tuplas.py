# Crear una tupla de números
numeros = (10, 20, 30, 40, 50)

# Imprimir la tupla completa
print("Tupla de números:", numeros)

# Acceder a un elemento de la tupla
print("Primer número:", numeros[0])

# Contar la cantidad de veces que aparece un elemento
print("Número de veces que aparece el 20:", numeros.count(20))

# Obtener el índice de un elemento específico
print("Índice del número 30:", numeros.index(30))

# Intentar modificar una tupla (esto generará un error)
try:
    numeros[0] = 100
except TypeError as e:
    print("Error:", e)
