import pandas as pd
import numpy as np

def correr_simulacion(precio_inicial, drift, rand):
    daily_returns = np.exp(drift + rand)
    simulacion = np.zeros_like(daily_returns)
    simulacion[0] = precio_inicial

    for t in range(1, simulacion.shape[0]):
        simulacion[t] = simulacion[t - 1] * daily_returns[t]

    return simulacion

if __name__ == "__main__":
    precios = extraer_precios("TSLA")
    drift = calcular_drift(precios)
    rand = calcular_rand(precios, 5, 3)
    print(type(correr_simulacion(100, drift, rand)))