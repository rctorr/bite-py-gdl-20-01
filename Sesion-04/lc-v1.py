import os
import time

# Variables
# carpeta = "/home/rctorr/CursoPython/Sesion-03"
carpeta = "./datos"  # Carpeta actual

def obtener_elementos(carpeta):
    """
    Obtiene los elementos de la carpeta y regresa en forma de lista
    """
    # Obtener la lista de elemento de un carpeta
    try:
        nombres = os.listdir(carpeta)  # ["nom1", "nom2", ...]
    except PermissionError:
        return [], 0
    
    # Agregando carpeta a la lista de nombres
    for i, nom in enumerate(nombres):  # [(0, "nom1"), (1, "nom2"), ]
        nombres[i] = os.path.join(carpeta, nom)  # "./nom1"
        
    """
    Estructura de datos para incluir el tamaño
    [
        ["./nom1", 1234],  <- e[0], e[1]
        ["./nom2", 5678],
        ...
    ]
    """
    elementos = []
    total = 0
    for nom in nombres:
        if os.path.isfile(nom):  # si es un archivo?
            tam = os.path.getsize(nom)
        else: # es una carpeta
            tam = 0

        # Obtener la fecha
        try:
            fecha = os.path.getmtime(nom)
            fecha = time.ctime(fecha)
        except FileNotFoundError:
            fecha = ""
        except PermissionError:
            fecha = ""

        elemento = [nom, tam, fecha]
        elementos.append(elemento)
        
        # sumar el tam a total para cada elemento
        total += tam  # total = total + tam
        
        if os.path.isdir(nom):  # Si nom es una carpeta?
            sub_elementos, sub_total = obtener_elementos(nom)
            elementos += sub_elementos
            
    
    return elementos, total

def imprimir_elementos(elementos, total):
    """
    Imprime la lista de elementos en formato texto en la salida
    estándar.
    """
    # Imprimir la lista
    print("-" * 80)
    for e in elementos:  # e = ["nom", 1234, "fecha"]
        # print("{} {}".format(e[0], e[1])
        if os.path.isdir(e[0]): # e = ["nom/", 1234, "fecha"]
            e[0] += "/" # e[0] = e[0] + "/"
        print("{:60}|{:10}|{:15}".format(*e))
    # Imprime toal
    print("-" * 80)
    print("Total: {} bytes".format(total))
    print("-" * 80)
    

def main():
    """ Es la función principal del script o módulo """
    # Llamando a las funciones
    elementos, total = obtener_elementos(carpeta)
    imprimir_elementos(elementos, total)

# Para poder ejecutarlo como módulo
if __name__ == "__main__": 
    main()