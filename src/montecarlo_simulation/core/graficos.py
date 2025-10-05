import matplotlib.pyplot as plt
import numpy as np

def graficar_lineas(simulacion: np.ndarray):
    fig, ax = plt.subplots(facecolor="black")
    ax.plot(simulacion)
    ax.set_xlabel("cantidad de días")
    ax.set_ylabel("stock price")
    for spine in ax.spines.values():
        spine.set_color('white')
        spine.set_linewidth(2)
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.set_facecolor("black")
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.12)
    return fig

def graficar_hist(simulacion: np.ndarray):
    fig, ax = plt.subplots(facecolor="black")
    plt.hist(simulacion[-1], bins=10)
    ax.set_xlabel("precio final")
    ax.set_ylabel("cantidad de simulaciones")
    for spine in ax.spines.values():
        spine.set_color('white')
        spine.set_linewidth(2)
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.set_facecolor("black")
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.12)
    return fig