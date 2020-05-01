n = 1000
lista = list(range(1, n+1))  # Generar u obtener la lista
# Convertir de int -> float
# for i in range(n):
#    lista[i] = float(lista[i])
# Convertir usando listas de compresión
lista = [float(i) for i in lista]  # [float(1), float(2), ...]

for i in lista:  # Imprimir la lista
    print(i)