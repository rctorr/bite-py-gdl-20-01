"""Módulo para calcular el precio promedio de destinos indicados"""
import numpy as np


def precio_promedio(tabla):
    """Calcula el precio promedio de los destinos indicados"""
    sum = 0
    for column in tabla.T:
        sum += np.sum(column)
    return sum / len(tabla.T)