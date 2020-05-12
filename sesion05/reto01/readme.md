## Reto 01

Para el sistema de reservación de Bedu Bikes, crear una clase llamada Recorrido la cual contendrá los elementos clave para cada elemento del mismo. Cambiar la lista de diccionarios que tenía originalmente por una lista de objetos.

[Clase Producto](./clase_recorrido.png)

La función velocidad será calculada con base al tiempo entre distancia como atributos. De la misma manera, multa será positivo si pasó de 45 minutos.

```
$ python3 main.py 
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
