import numpy as np

def precio_minmax(simulacion: np.ndarray):
    min = simulacion[-1].min()
    max = simulacion[-1].max()
    return min, max

def retorno_minmax(simulacion: np.ndarray):
    min = simulacion[-1].min() / simulacion[0, 0] - 1
    max = simulacion[-1].max() / simulacion[0, 0] - 1
    return min, max

def prob_ganancia(simulacion: np.ndarray):
    return np.sum(simulacion[-1] > simulacion[0, 0]) / simulacion[-1].size

def prob_perdida(simulacion: np.ndarray):
    return np.sum(simulacion[-1] < simulacion[0, 0]) / simulacion[-1].size

def percentiles(simulacion: np.ndarray):
    return np.percentile(simulacion[-1], 10), np.percentile(simulacion[-1], 90)