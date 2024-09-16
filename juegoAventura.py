print("¡Bienvenido al Cuento de Aventura Interactivo!")
print("Eres un explorador en una jungla misteriosa. Tienes que tomar decisiones para sobrevivir y encontrar un tesoro perdido.")

# Comienzo de la historia
print("\nTe encuentras en una encrucijada. ¿Qué decides hacer?")
print("1. Ir a la izquierda hacia el río.")
print("2. Ir a la derecha hacia la cueva oscura.")

# Primera decisión
decision1 = input("Elige 1 o 2: ")

if decision1 == '1':
    print("\nDecides ir hacia el río. El agua es cristalina, pero hay cocodrilos alrededor.")
    print("1. Intenta nadar a través del río.")
    print("2. Busca un puente más adelante.")
    decision2 = input("Elige 1 o 2: ")

    if decision2 == '1':
        print("\nIntentas nadar, pero los cocodrilos te ven. ¡Fin del juego!")
    elif decision2 == '2':
        print("\nEncuentras un puente y cruzas el río con seguridad. ¡Encuentras el tesoro escondido! ¡Ganaste!")
    else:
        print("Opción no válida. Fin del juego.")

elif decision1 == '2':
    print("\nEntras a la cueva oscura. Escuchas ruidos extraños.")
    print("1. Continúa adentrándote en la cueva.")
    print("2. Regresa a la encrucijada.")
    decision2 = input("Elige 1 o 2: ")

    if decision2 == '1':
        print("\nTe encuentras con un oso, pero logras asustarlo y sigues adelante. Encuentras el tesoro escondido. ¡Ganaste!")
    elif decision2 == '2':
        print("\nDecides regresar a la encrucijada, pero te pierdes en la jungla. ¡Fin del juego!")
    else:
        print("Opción no válida. Fin del juego.")

else:
    print("Opción no válida. Fin del juego.")
