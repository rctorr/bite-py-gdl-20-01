import csv
import json
import os
import time

"""
Versi´on usando POO (Programaci´on Orientada a Objetos)
"""

class Elemento():
    def __init__(self, nom, tam):
        """ El constructor del objeto Elemento """
        self.nom = nom
        self.tam = tam
        self.fech = self.obteber_fecha()
    
    def obteber_fecha(self):
        """ Obtener la fecha del elemento """
        try:
            fecha = os.path.getmtime(self.nom)
            fecha = time.ctime(fecha)
        except FileNotFoundError:
            fecha = ""
        except PermissionError:
            fecha = ""
        
        return fecha
        
    def __str__(self):
        """ Regresa la versi´on en str de Elemento """
        
        return "{} | {} | {}".format(self.nom, self.tam, self.fech)

class Carpeta(Elemento):
    def __init__(self, ruta):
        Elemento.__init__(self, ruta, 0)  # super()
        


def obtener_elementos(carpeta):
    """
    Obtiene los elementos de la carpeta y regresa en forma de
    lista
    """
    # Obtener la lista de elemento de un carpeta
    try:
        nombres = os.listdir(carpeta)
    except PermissionError:
        return [], 0
    
    # Agregando carpeta a la lista de nombres
    for i, nom in enumerate(nombres):
        nombres[i] = os.path.join(carpeta, nom)
    
    # Agregar los datos adicionales a cada elemento
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
        
        # si es una carpeta, entonces obtenemos sus elementos
        if os.path.isdir(nom):  # Si nom es una carpeta?
            sub_elementos = obtener_elementos(nom)
            elementos += sub_elementos
            tam = sub_elementos[-1][1]

        # sumar el tam a total para cada elemento
        total += tam  # total = total + tam
        # Para hacer depuraci´on pusada
        # print(elementos)
        # input("Presiona ENTER")
    
    # Agregando un elemento auxiliar para el total
    elemento = ["Total:", total, "bytes"]
    elementos.append(elemento)
    
    return elementos

def imprimir_elementos(elementos):
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
        print("{:40}|{:10}|{:15}".format(*e))
    print("-" * 80)

def guardar_elementos(elementos):
    """
    Guarda la lista de elementos en el archivo salida.txt.
    """
    archivo = "salida.txt"
    
    da = open(archivo, "w")
    # Imprimir la lista
    da.write("-" * 80 + "\n")
    for e in elementos:  # e = ["nom", 1234, "fecha"]
        # print("{} {}".format(e[0], e[1])
        if os.path.isdir(e[0]): # e = ["nom/", 1234, "fecha"]
            e[0] += "/" # e[0] = e[0] + "/"
        print("{:60}|{:10}|{:15}".format(*e), file=da)
    print("-" * 80, file=da)
    
    da.close()

def guardar_elementos_csv(elementos):
    """
    Guarda la lista de elementos en el archivo salida.csv.
    """
    archivo = "salida.csv"
    
    with open(archivo, "w") as da:
        # Crear un descript de archivo en csv
        da_csv = csv.writer(da)
        # Guarda el encabezado
        enc = ["Nombre", "Tamaño", "Fecha"]
        da_csv.writerow(enc)
        # Guardar la lista
        for e in elementos:  # e = ["nom", 1234, "fecha"]
            # print("{} {}".format(e[0], e[1])
            if os.path.isdir(e[0]): # e = ["nom/", 1234, "fecha"]
                e[0] += "/" # e[0] = e[0] + "/"
            da_csv.writerow(e)

def guardar_elementos_json(elementos):
    """
    Guarda la lista de elementos en el archivo salida.json.
    """
    archivo = "salida.json"
    
    with open(archivo, "w") as da:
        json.dump(elementos, da, indent=4)

# MVC: Controlador
def main():
    """ Es la función principal del script o módulo """
    # Variables
    ruta = "."  # Carpeta actual

    # Instanciar objetos
    carpeta = Carpeta(ruta)  # carpeta es de tipo Carpeta()
    print(carpeta)
    # elementos = carpeta.obtener_elementos()
    
    #imprimir_elementos(elementos)
    #guardar_elementos(elementos)
    #guardar_elementos_csv(elementos)
    #guardar_elementos_json(elementos)

# Para poder ejecutarlo como módulo
if __name__ == "__main__": 
    main()