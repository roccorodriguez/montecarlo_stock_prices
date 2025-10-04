import pandas as pd
import os
from src.core.data import *
from src.core.brownian_motion import *
from src.core.montecarlo import *
from src.core.graficos import *
from src.core.estadisticos import *

def main(ticker: str, iteraciones: int, n_simulaciones: int, drift_simulado=None):
    precios = extraer_precios(ticker)
    drift_historico = calcular_drift(precios)
    rand = calcular_rand(precios, iteraciones, n_simulaciones)
    precio_inicial = precios.iloc[-1]
    if drift_simulado == None:
        simulacion = correr_simulacion(precio_inicial, drift_historico, rand)
    else: simulacion = correr_simulacion(precio_inicial, drift_simulado, rand)
    graficar_lineas(simulacion).savefig("grafico1.jpg")
    graficar_hist(simulacion).savefig("grafico2.jpg")

    precio_min, precio_max = precio_minmax(simulacion)
    retorno_min, retorno_max = retorno_minmax(simulacion)
    p_ganancia = prob_ganancia(simulacion)
    p_perdida = prob_perdida(simulacion)
    p10, p90 = percentiles(simulacion)

    return drift_historico[0], precio_min, precio_max, retorno_min, retorno_max, p_ganancia, p_perdida, p10, p90

if __name__ == "__main__":
    main("PG", 1000, 100)