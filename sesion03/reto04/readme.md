## Reto 04

`mas_centrico_modulo.py`

De forma similar al ejemplo anterior, modifica `mas_centrico_modulo.py` para que la función de calcular un mejor precio se pueda usar como módulo o como archivo independiente. Agrega docstrings para indicar al usuario final cómo utilizarlo.


```python
$ python3 mas_centrico_modulo.py

El lugar más centrico es Roma con 51 minutos de ida y 45 de vuelta.

$ ipython3
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import mas_centrico

In [2]: mas_centrico?
                                        
Type:        module
String form: <module 'mas_centrico' from '/home/checor/dev/python-clases-ds/sesion03/reto04/mas_centrico.py'>
File:        ~/dev/python-clases-ds/sesion03/reto04/mas_centrico.py
Docstring:   Módulo para mostrar el lugar mas centrico de varios puntos de la ciudad.

In [3]: mas_centrico.mas_centrico?

Signature: mas_centrico.mas_centrico(lugares, tabla)
Docstring: Muestra el destino mas centrico. Recibe una lista de lugares y un array con los tiempos.
File:      ~/dev/python-clases-ds/sesion03/reto04/mejor_precio.py
Type:      function

In [4]:        

```
