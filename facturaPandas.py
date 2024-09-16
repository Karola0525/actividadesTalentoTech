import pandas as pd

# Datos de ejemplo para la factura
data = {
    "Descripción": ["tomate de árbol", "mora", "chilacuan", "lulo", "guayaba"],
    "Valor Unitario": [500, 100, 200, 350, 150],
    "Cantidad": [10, 5, 2, 3, 1]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Calcular el subtotal para cada artículo (Valor Unitario * Cantidad)
df["Subtotal"] = df["Valor Unitario"] * df["Cantidad"]

# Calcular el total de la factura
total_factura = df["Subtotal"].sum()

# Mostrar la tabla de la factura
print("Tabla de Factura:")
print(df)

# Mostrar el total de la factura
print(f"\nTotal de la Factura: ${total_factura:.2f}")
