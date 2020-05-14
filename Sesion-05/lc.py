import csv
import json
import os
import time

"""
Versión usando POO (Programació Orientada a Objetos)
"""

class Elemento():
    def __init__(self, nom, tam):
        """ El constructor del objeto Elemento """
        # Definición y asignación de atributos
        self.nom = nom  # valor de un argumento
        self.tam = tam  # idem
        self.fech = self.obteber_fecha()  # obtenido del S.O.
    
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
        """ Regresa la versión en str de Elemento """
        
        return "{} | {} | {}".format(self.nom, self.tam, self.fech)

    
class Carpeta(Elemento):
    def __init__(self, ruta):
        """ """
        Elemento.__init__(self, ruta, 0)  # super()
        self.elementos = []
        
    def obtener_elementos(self):
        """
        Obtiene los elementos de la carpeta y regresa en forma de
        lista
        """
        # Obtener la lista de elemento de un carpeta
        try:
            nombres = os.listdir(self.nom)
        except PermissionError:
            return [], 0

        # Agregando carpeta a la lista de nombres
        for i, nom in enumerate(nombres):
            nombres[i] = os.path.join(self.nom, nom)

        # Agregar los datos adicionales a cada elemento
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

            elemento = [tam, fecha, nom]
            self.elementos.append(elemento)

            # si es una carpeta, entonces obtenemos sus elementos
            if os.path.isdir(nom):  # Si nom es una carpeta?
                sub_carpeta = Carpeta(nom)
                sub_carpeta.obtener_elementos()
                
                self.elementos += sub_carpeta.elementos
                tam = sub_carpeta.elementos[-1][0]

            # sumar el tam a total para cada elemento
            total += tam  # total = total + tam
            # Para hacer depuraci´on pusada
            # print(elementos)
            # input("Presiona ENTER")

        # Agregando un elemento auxiliar para el total
        elemento = [total, "bytes", "en total",]
        self.elementos.append(elemento)

        
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
        print("{:10} | {:15} | {}".format(*e))
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
        print("{:10} | {:15} | {}".format(*e), file=da)
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
        enc = ["Tamaño", "Fecha","Nombre"]
        da_csv.writerow(enc)
        # Guardar la lista
        for e in elementos:  # e = [1234,"fecha","nom"]
            # print("{} {}".format(e[0], e[1])
            if os.path.isdir(e[2]): # e = [1234, "fecha","nom/"]
                e[2] += "/" # e[3] = e[3] + "/"
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
    carpeta.obtener_elementos()
    
    imprimir_elementos(carpeta.elementos)
    guardar_elementos(carpeta.elementos)
    guardar_elementos_csv(carpeta.elementos)
    guardar_elementos_json(carpeta.elementos)

# Para poder ejecutarlo como módulo
if __name__ == "__main__": 
    main()