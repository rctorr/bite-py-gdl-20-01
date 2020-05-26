import numpy as np


def main():
    """ Función principal del script """
    
    # Generar nuestro conjunto de matriz y vectores
    a = np.array([
        [5, 112],
        [35, -31]
    ])
    b = np.array([19, 242])
    
    # Resolver el sistema de ecuaciones
    x = np.linalg.solve(a, b)
    print("La solución al sistema de ecuaciones es:", x)
    
    # Comprobando soluciones:
    # a * x -->> b
    b1 = np.dot(a, x)
    print("b original:", b)
    print("b calculada:", b1)
    
    if np.allclose(b, b1):
        print("El resultado es correcto")
    else:
        print("No seas zope!")
    
    # Guardando resultados en el archivo soluciones.txt
    nomarch = "soluciones.txt"
    np.savetxt(nomarch, x, fmt="%f")
    print("Solución guardada en el archivo:", nomarch)

if __name__ == "__main__":
    main()