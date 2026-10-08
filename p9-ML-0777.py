# catherine eileen huerta rascon NC = 0072
# practica prueba
import pandas as pd
print(pd.__version__) # Output: 1.5.2

print("ejercision de lista = 30")

# 30.
datos30 = {
    'distancia_km': [2.7, 5.5, 1.5, 3.9, 4.6],
    'trafico_nivel': [2, 3, 1, 2, 1],
    'edad_repartidor': [30, 41, 26, 34, 27],
    'tiempo_entrega_min': [21, 50, 11, 32, 31]
}

df = pd.DataFrame(datos30)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))