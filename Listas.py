# Crear una lista de frutas
frutas = [ "guayaba","motilón","carambolo","mora", "tomate de árbol", "chilacuán"]

# Imprimir la lista completa
print("Lista de frutas:", frutas)

# Acceder a un elemento de la lista
print("Primera fruta:", frutas[0])

# Agregar un nuevo elemento a la lista
frutas.append("chiros")
print("Lista después de añadir 'chiros':", frutas)

# Eliminar un elemento de la lista
frutas.remove("tomate de árbol")
print("Lista después de eliminar 'tomate de árbol':", frutas)

# Ordenar la lista
frutas.sort()
print("Lista ordenada:", frutas)

# Ordenar la lista
frutas.sort(reverse=True)
print("Lista ordenada:", frutas)
