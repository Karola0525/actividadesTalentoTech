# Datos de la factura
productos = [
    {"nombre": "Mora", "valor_unitario": 1000, "cantidad": 20},
    {"nombre": "chilacuan", "valor_unitario": 2000, "cantidad": 50},
    {"nombre": "chiro", "valor_unitario": 1500, "cantidad": 30},
    {"nombre": "tomate de árbol", "valor_unitario": 700, "cantidad": 40},
    {"nombre": "lulo", "valor_unitario": 1200, "cantidad": 10}
]

# Inicializar el total general de la factura
total_general = 0

# Imprimir encabezados de la tabla
print(f"{'Nombre':<15} {'Valor Unitario':<15} {'Cantidad':<10} {'Subtotal':<10}")

# Calcular e imprimir cada fila de la tabla
for producto in productos:
    nombre = producto["nombre"]
    valor_unitario = producto["valor_unitario"]
    cantidad = producto["cantidad"]
    subtotal = valor_unitario * cantidad
    total_general += subtotal

    # Imprimir cada fila con el formato adecuado
    print(f"{nombre:<15} ${valor_unitario:<14.2f} {cantidad:<10} ${subtotal:<10.2f}")

# Imprimir el total general de la factura
print("\nTotal general de la factura: $", round(total_general, 2))
