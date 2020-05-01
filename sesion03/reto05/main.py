import numpy as np
from comparador import mejor_precio, precio_promedio

destinos = ["Ixtapa", "Acapulco", "Cancún"]
opciones = ["Hospedaje", "Transporte", "Excursion", "Comida"]

valores = np.array([[1500, 3000, 4500], 
                    [800, 1200, 100], 
                    [500, 800, 1200], 
                    [ 120, 240, 360]])

destino, precio = mejor_precio.mejor_precio(destinos, valores)
promedio = precio_promedio.precio_promedio(valores)

print("El mejor precio es {} por ${}".format(destino, precio))
print("El precio promerio de los destinos es ${:02.2f}".format(promedio))