# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generar datos de ejemplo
np.random.seed(42)
# Datos para regresión lineal simple (1 característica)
X_simple = 2 * np.random.rand(100, 1)
y = 4 + 3 * X_simple + np.random.randn(100, 1)

# Datos para regresión lineal múltiple (2 características)
X1 = 2 * np.random.rand(100, 1)
X2 = 3 * np.random.rand(100, 1)
X_multiple = np.hstack([X1, X2])
# Creando una relación para la variable de salida (y)
y_multiple = 4 + 3 * X1 + 2 * X2 + np.random.randn(100, 1)

# Dividir los datos en conjunto de entrenamiento y prueba (para ambas regresiones)
X_train_simple, X_test_simple, y_train_simple, y_test_simple = train_test_split(X_simple, y, test_size=0.2, random_state=42)
X_train_multiple, X_test_multiple, y_train_multiple, y_test_multiple = train_test_split(X_multiple, y_multiple, test_size=0.2, random_state=42)

# Crear los modelos de regresión lineal simple y múltiple
reg_simple = LinearRegression()
reg_multiple = LinearRegression()

# Entrenar los modelos
reg_simple.fit(X_train_simple, y_train_simple)
reg_multiple.fit(X_train_multiple, y_train_multiple)

# Predecir los valores para los conjuntos de prueba
y_pred_simple = reg_simple.predict(X_test_simple)
y_pred_multiple = reg_multiple.predict(X_test_multiple)

# Mostrar los coeficientes para cada modelo
print("Regresión Lineal Simple:")
print("Intersección (b):", reg_simple.intercept_)
print("Pendiente (m):", reg_simple.coef_)

print("\nRegresión Lineal Múltiple:")
print("Intersección (b):", reg_multiple.intercept_)
print("Pendientes (m1, m2):", reg_multiple.coef_)

# Calcular el error cuadrático medio para cada modelo
mse_simple = mean_squared_error(y_test_simple, y_pred_simple)
mse_multiple = mean_squared_error(y_test_multiple, y_pred_multiple)

print("\nError Cuadrático Medio - Regresión Simple:", mse_simple)
print("Error Cuadrático Medio - Regresión Múltiple:", mse_multiple)

# Visualización de los resultados

# Gráfico para la regresión lineal simple
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_test_simple, y_test_simple, color='blue', label='Datos de prueba')
plt.plot(X_test_simple, y_pred_simple, color='red', linewidth=2, label='Línea de regresión')
plt.xlabel("X (una característica)")
plt.ylabel("y")
plt.title("Regresión Lineal Simple")
plt.legend()

# Gráfico para la regresión lineal múltiple
plt.subplot(1, 2, 2)
plt.scatter(X_test_multiple[:, 0], y_test_multiple, color='blue', label='Datos de prueba (X1)')
plt.scatter(X_test_multiple[:, 1], y_test_multiple, color='green', label='Datos de prueba (X2)')
plt.plot(X_test_multiple[:, 0], reg_multiple.predict(X_test_multiple)[:, 0], color='red', linewidth=2, label='Línea de regresión para X1')
plt.plot(X_test_multiple[:, 1], reg_multiple.predict(X_test_multiple)[:, 0], color='orange', linewidth=2, label='Línea de regresión para X2')
plt.xlabel("X1 y X2 (múltiples características)")
plt.ylabel("y")
plt.title("Regresión Lineal Múltiple")
plt.legend()

plt.tight_layout()
plt.show()
