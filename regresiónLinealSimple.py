# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generar datos de ejemplo
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
reg = LinearRegression()

# Entrenar el modelo
reg.fit(X_train, y_train)

# Predecir los valores del conjunto de prueba
y_pred = reg.predict(X_test)

# Mostrar los coeficientes
print("Intersección (b):", reg.intercept_)
print("Pendiente (m):", reg.coef_)

# Calcular y mostrar el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print("Error Cuadrático Medio:", mse)

# Visualizar los datos de entrenamiento y la línea de regresión
plt.scatter(X_train, y_train, color='blue', label='Datos de entrenamiento')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Línea de regresión')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regresión Lineal Simple")
plt.legend()
plt.show()
