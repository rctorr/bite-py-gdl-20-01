from bs4 import BeautifulSoup
import requests


def main():
    """ Función principal del script """
    url = "https://unsplash.com/"
    
    # Descarga del contenido de la url
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        # Creando la sopa
        sopa = BeautifulSoup(
            respuesta.content, features="html.parser")
        # Obteniendo el texto de la etiqueta <title>
        t = sopa.title
        print(t.text)
        # Obtener la lista de todas las imágenes
        imagenes = sopa.find_all("img")
        
        for img in imagenes:
            print(img["src"])
        
    else:
        print("Error:", respuesta.status_code)
    


if __name__ == "__main__":
    main()