## Reto 03

Para el sistema de recorridos, agrega una nueva clase llamada Reporte, que herede de Recorrido, para incluir información extra acerca de un reporte con ese recorrido (falla de bici, problema con la estación...). Su tiempo o distancia NO deben contar para los totales, pero si deben mostarse.

[Clase Reporte](./repote.png)

Agregar la columna de Personas, y utilizar la función `isinstance`, para saber si es un recorrido normal o con reporte.

```
Quieres conocer la distancia total de recorrido? (s/n) Si
Quieres conocer el tiempo total de recorrido? (s/n) Si

--------------------------------------------------------------------------------
ORIGEN               | DESTINO             | DISTANCIA  | TIEMPO | REP | CAUSA |
--------------------------------------------------------------------------------
Buenavista           | Del Valle Norte     | 7.4 km     | 30:00  | No  |       |
Alameda              | Condesa             | 5.4 km     | 20:00  | No  |       |
Roma Norte           | Tabacalera          | 3.5 km     | 15:00  | No  |       |
Reforma              | Juárez              | 1.2 km     |  8:00  | No  |       |
Roma Sur             | Roma Norte          | 0.8 km     |  4:00  | Si  | Falla |
--------------------------------------------------------------------------------
                                                          Tiempo total |  1:13:00
                                                       Distancia total |  17.5 km
```
