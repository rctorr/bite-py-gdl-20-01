## Reto 06

`reservaciones/`

Organizar el programa de tiempos de usuario, en un paquete llamado recorridos con dos módulos: `entrada.py` y `salidas.py`. Como sus nombres lo indican, el primero incluirá funciones de entrada de información del usuario, y el otro mostrará resultados.

```
$ tree
├── main.py
└── recorridos
    ├── entradas.py
    ├── __init__.py
    ├── __pycache__
    │   ├── entradas.cpython-36.pyc
    │   ├── __init__.cpython-36.pyc
    │   └── salidas.cpython-36.pyc
    └── salidas.py

$ python main.py 
Quieres conocer la distancia total de recorrido? (s/n) Si
Quieres conocer el tiempo total de recorrido? (s/n) Si

------------------------------------------------------------------
ORIGEN               | DESTINO             | DISTANCIA  | TIEMPO    
------------------------------------------------------------------
Roma Norte           | Tabacalera          | 3.5 km     | 15:00
Reforma              | Juárez              | 1.2 km     |  8:00
Alameda              | Condesa             | 5.4 km     | 20:00
Roma Sur             | Roma Norte          | 0.8 km     |  4:00
Buenavista           | Del Valle Norte     | 7.4 km     | 30:00
------------------------------------------------------------------
                                           Tiempo total |  1:17:00
                                        Distancia total |  18.3 km
```