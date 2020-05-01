## Reto 06 

`recorridos-lambda.py`

Modificar el script del reto04 `recorridos-con-diccionarios.py`, para que se ordenen sus usos de bibicleta, basándose en su distancia y tiempo.

Utilizar la función sort de la lista de diccionarios, e indicarle mediante el lambda, que elementos utilizar, para que los ordene de esa manera, en un orden de mayor a menor. Si dos recorridos tienen el mismo tiempo, debe de utilizar la distancia como segundo.

```
Quieres conocer la distancia total de recorrido? (s/n) Si

------------------------------------------------------------------
ORIGEN               | DESTINO             | DISTANCIA  | TIEMPO    
------------------------------------------------------------------
Buenavista           | Del Valle Norte     | 7.4 km     | 30:00
Alameda              | Condesa             | 5.4 km     | 20:00
Roma Norte           | Tabacalera          | 3.5 km     | 15:00
Reforma              | Juárez              | 1.2 km     |  8:00
Roma Sur             | Roma Norte          | 0.8 km     |  4:00
------------------------------------------------------------------
                                           Tiempo total |  1:17:00
                                        Distancia total |  18.3 km
```