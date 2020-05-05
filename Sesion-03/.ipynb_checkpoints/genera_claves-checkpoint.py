import random

n = 5
m = 10

# Listas de símbolos
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()
digitos = "1234567890"
simbolos = "#$%&/()="
alfabeto = minusculas + mayusculas + digitos + simbolos

for i in range(n):
    # Crear una sóla clave
    clave = random.choice(minusculas)  # Elegir una minusc. al azar. ej. clave = "k"
    clave += random.choice(mayusculas)  # clave = "kR"
    clave += random.choice(digitos)  # clave = "kR3"
    clave += random.choice(simbolos)  # clave = "kR3%"

    r = m - 4  # Calculamos cuantas nos faltan. ej 4
    faltantes = random.choices(alfabeto, k=r)  # ["a", "B", "r", "3", "s"]
    faltantes = "".join(faltantes)  # "aBr3s"
    clave += faltantes # "kR3%aBr3s"
    lclave = list(clave)  # ["k", "R", ...]
    random.shuffle(lclave)  # ["R", "3", ...]
    clave = "".join(lclave)  # "R3..."
    print(clave)
