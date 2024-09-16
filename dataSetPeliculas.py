import pandas as pd
from IPython.display import display

# Crear el dataset de personajes de la película Coraline
data = {
    "Nombre": [
        "Coraline Jones",
        "Mel Jones",
        "Charlie Jones",
        "The Beldam (Other Mother)",
        "Other Father",
        "Wybie Lovat",
        "Mr. Bobinsky",
        "Miss Spink",
        "Miss Forcible",
        "Cat"
    ],
    "Rol": [
        "Protagonista",
        "Madre",
        "Padre",
        "Antagonista",
        "Personaje Secundario",
        "Amigo",
        "Vecino",
        "Vecina",
        "Vecina",
        "Aliado"
    ],
    "Relación con Coraline": [
        "Ella misma",
        "Madre en el mundo real",
        "Padre en el mundo real",
        "Madre en el Otro Mundo",
        "Padre en el Otro Mundo",
        "Amigo y vecino",
        "Vecino excéntrico",
        "Vecina amable",
        "Vecina amable",
        "Guía y protector"
    ],
    "Característica Distintiva": [
        "Curiosa y aventurera",
        "Ocupada y estricta",
        "Despreocupado y distraído",
        "Engañosa y manipuladora",
        "Creativo pero controlado",
        "Intrépido y curioso",
        "Acrobático y excéntrico",
        "Amante de los perros",
        "Ex-actriz de teatro",
        "Misterioso y sabio"
    ]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Mostrar el DataFrame como una tabla


display(df)
