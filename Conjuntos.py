# Crear un conjunto de colores
colores = {"rojo", "verde", "azul", "amarillo"}

# Imprimir el conjunto completo
print("Conjunto de colores:", colores)

# Añadir un nuevo color al conjunto
colores.add("morado")
print("Conjunto después de añadir 'morado':", colores)

# Intentar añadir un color que ya existe (no se añadirá porque es un conjunto)
colores.add("rojo")
print("Conjunto después de intentar añadir 'rojo' de nuevo:", colores)

# Eliminar un color del conjunto
colores.remove("amarillo")
print("Conjunto después de eliminar 'amarillo':", colores)

# Realizar la unión de dos conjuntos
colores2 = {"naranja", "rosa", "verde"}
union_colores = colores.union(colores2)
print("Unión de dos conjuntos:", union_colores)

# Realizar la intersección de dos conjuntos
interseccion_colores = colores.intersection(colores2)
print("Intersección de dos conjuntos:", interseccion_colores)
