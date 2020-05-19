import csv
import json
import os
import time

"""
Versión usando POO (Programació Orientada a Objetos)
"""

class Elemento():
    def __init__(self, ruta):
        """ El constructor del objeto Elemento """
        # Definición y asignación de atributos
        if not os.path.exists(ruta):
            raise FileNotFoundError(
                f"La carpeta {ruta} no existe!")
        self.nombre = ruta
        self.tamanio = self.obtener_tamanio()
        self.fecha = self.obtener_fecha()
    
    def obtener_fecha(self):
        """ Obtener la fecha del elemento """
        try:
            fecha = os.path.getmtime(self.nombre)
            fecha = time.ctime(fecha)
        except FileNotFoundError:
            fecha = ""
        except PermissionError:
            fecha = ""
        
        return fecha
    
    def obtener_tamanio(self):
        """ Obtiene el tamaño del elemento """
        if os.path.isfile(self.nombre):
            tam = os.path.getsize(self.nombre)
        else: # es una carpeta
            tam = 0
            
        return tam
        
    def __str__(self):
        """ Regresa la versión en str de Elemento """
        return "{:10} | {:15} | {}".format(
            self.tamanio, self.fecha, self.nombre)


class Archivo(Elemento):
    def __init__(self, ruta):
        """ Iinicializar objeto de tipo Archivo() """
        Elemento.__init__(self, ruta)
        
    
class Carpeta(Elemento):
    def __init__(self, ruta):
        """ """
        Elemento.__init__(self, ruta)
        self.elementos = []
        # self.elementos = self.obtener_elementos()
        self.total = 0
        
    def obtener_elementos(self):
        """
        Obtiene los elementos de la carpeta y regresa en forma de
        lista
        """
        # Obtener la lista de elemento de un carpeta
        try:
            nombres = os.listdir(self.nombre)
        except PermissionError:
            return

        # Ordenar alfabéticamente
        nombres.sort(key=lambda nom: nom.lower())
        
        # Agregando carpeta a la lista de nombres
        nombres = [os.path.join(self.nombre, nom) for nom in nombres]

        # Agregar los datos adicionales a cada elemento
        for nom in nombres:
            if os.path.isdir(nom):  # Si nom es una carpeta?
                carpeta = Carpeta(nom)
                self.elementos.append(carpeta)
            else:
                archivo = Archivo(nom)
                self.elementos.append(archivo)
                self.tamanio += archivo.tamanio

        self.total += self.tamanio
        
        # Ordenar por tamaño de mayor a menor
        # Donde está nuestra lista a ordenar, en que variable?
        self.elementos.sort(key=lambda e: e.tamanio,
            reverse=True)
        

    def __str__(self):
        """ Regresa la versión en str de Elemento """
        return Elemento.__str__(self) + os.path.sep

        
def imprimir_elementos(carpeta):
    """
    Imprime la lista de elementos en formato texto en la salida
    estándar de los elementos de carpeta.
    """
    print(carpeta)
    for e in carpeta.elementos:
        if isinstance(e, Archivo):
            print(e)  # def __str__()
        else:  # e es un objeto Carpeta()
            e.obtener_elementos()
            imprimir_elementos(e)

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
    ruta = ".."  # Carpeta actual

    # Instanciar objetos
    carpeta = Carpeta(ruta)  # carpeta es de tipo Carpeta()
    carpeta.obtener_elementos()
    
    imprimir_elementos(carpeta)
    # guardar_elementos(carpeta.elementos)
    # guardar_elementos_csv(carpeta.elementos)
    # guardar_elementos_json(carpeta.elementos)

# Para poder ejecutarlo como módulo
if __name__ == "__main__": 
    main()