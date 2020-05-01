"""Módulo con para calcular el destino con mejor precio."""
import numpy as np

def mejor_precio(destinos, tabla):
    """Muestra el destino con mejor precio y su precio final"""
    lowest_sum = np.sum(tabla.T[1, 0:])
    lowest_index = 0
    for i, column in enumerate(tabla.T):
        if np.sum(column) < lowest_sum:
            lowest_sum = np.sum(column)
            lowest_index = i
    return destinos[lowest_index], lowest_sum