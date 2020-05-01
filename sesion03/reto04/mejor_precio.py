"""Móudlo para mostrar el mejor precio de un array con opciones y destinos"""
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

if __name__ == "__main__":
    destinos = ["Ixtapa", "Acapulco", "Cancún"]
    opciones = ["Hospedaje", "Transporte", "Excursion", "Comida"]

    valores = np.array([[1500, 3000, 4500], 
                        [800, 1200, 100], 
                        [500, 800, 1200], 
                        [ 120, 240, 360]])

    destino, precio = mejor_precio(destinos, valores)

    print("El mejor precio es {} por ${}".format(destino, precio))