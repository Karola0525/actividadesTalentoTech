# Conjunto de películas vistas por Juan
peliculas_juan = {"El Padrino", "Pulp Fiction", "El Señor de los Anillos", "Matrix", "Toy Story", "Inception"}

# Conjunto de películas vistas por María
peliculas_maria = {"Matrix", "Titanic", "Toy Story", "Avatar", "El Rey León", "El Padrino"}

# Imprimir los conjuntos originales
print("Películas vistas por Juan:", peliculas_juan)
print("Películas vistas por María:", peliculas_maria)

# Películas vistas por ambos (intersección)
peliculas_comunes = peliculas_juan.intersection(peliculas_maria)
print("\nPelículas vistas por ambos:", peliculas_comunes)

# Películas únicas de Juan (diferencia)
peliculas_unicas_juan = peliculas_juan.difference(peliculas_maria)
print("Películas únicas de Juan:", peliculas_unicas_juan)

# Películas únicas de María (diferencia)
peliculas_unicas_maria = peliculas_maria.difference(peliculas_juan)
print("Películas únicas de María:", peliculas_unicas_maria)

# Películas vistas por al menos uno de los dos (unión)
peliculas_totales = peliculas_juan.union(peliculas_maria)
print("Películas vistas por al menos uno de los dos:", peliculas_totales)

# Películas únicas entre ambos (diferencia simétrica)
peliculas_unicas_ambos = peliculas_juan.symmetric_difference(peliculas_maria)
print("Películas únicas entre ambos:", peliculas_unicas_ambos)
