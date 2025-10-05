import pandas as pd
import numpy as np
from scipy.stats import norm

def calcular_drift(precios: pd.DataFrame):
    log_returns = np.log(1 + precios.pct_change())
    return log_returns.mean().to_numpy() - 0.5 * log_returns.var().to_numpy()

def calcular_rand(precios: pd.DataFrame, iteraciones: int, n_simulaciones: int):
    log_returns = np.log(1 + precios.pct_change())
    return log_returns.std().to_numpy() * norm.ppf(np.random.rand(iteraciones, n_simulaciones))