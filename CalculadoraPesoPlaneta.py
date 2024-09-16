# Funciones para calcular el peso en diferentes planetas
def peso_mercurio(peso_tierra):
    return round(peso_tierra * 0.3)

def peso_venus(peso_tierra):
    return round(peso_tierra * 0.9)

def peso_marte(peso_tierra):
    return round(peso_tierra * 0.3)

def peso_jupiter(peso_tierra):
    return round(peso_tierra * 2.4)

def peso_saturno(peso_tierra):
    return round(peso_tierra * 1.1)

def peso_urano(peso_tierra):
    return round(peso_tierra * 1.1)

def peso_neptuno(peso_tierra):
    return round(peso_tierra * 0.8)

# Entrada del usuario
peso_tierra = float(input("Ingrese su peso en la Tierra (kg): "))

# Selección del planeta
print("Seleccione el planeta para calcular su peso:")
print("1. Mercurio")
print("2. Venus")
print("3. Marte")
print("4. Júpiter")
print("5. Saturno")
print("6. Urano")
print("7. Neptuno")

opcion = input("Ingrese el número del planeta: ")

# Cálculo del peso basado en la opción seleccionada
if opcion == "1":
    print(f"Su peso en Mercurio sería: {peso_mercurio(peso_tierra)} kg")
elif opcion == "2":
    print(f"Su peso en Venus sería: {peso_venus(peso_tierra)} kg")
elif opcion == "3":
    print(f"Su peso en Marte sería: {peso_marte(peso_tierra)} kg")
elif opcion == "4":
    print(f"Su peso en Júpiter sería: {peso_jupiter(peso_tierra)} kg")
elif opcion == "5":
    print(f"Su peso en Saturno sería: {peso_saturno(peso_tierra)} kg")
elif opcion == "6":
    print(f"Su peso en Urano sería: {peso_urano(peso_tierra)} kg")
elif opcion == "7":
    print(f"Su peso en Neptuno sería: {peso_neptuno(peso_tierra)} kg")
else:
    print("Opción no válida. Por favor, seleccione un número de 1 a 7.")
