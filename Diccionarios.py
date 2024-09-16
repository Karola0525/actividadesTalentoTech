# Crear un diccionario de países y sus capitales
capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín"
}

# Imprimir el diccionario completo
print("Diccionario de capitales:", capitales)

# Acceder al valor asociado a una clave
print("La capital de Francia es:", capitales["Francia"])

# Añadir un nuevo par clave-valor
capitales["Portugal"] = "Lisboa"
print("Diccionario después de añadir Portugal:", capitales)

# Eliminar un par clave-valor
del capitales["Italia"]
print("Diccionario después de eliminar Italia:", capitales)

# Obtener solo las claves del diccionario
print("Países en el diccionario:", list(capitales.keys()))

# Obtener solo los valores del diccionario
print("Capitales en el diccionario:", list(capitales.values()))
