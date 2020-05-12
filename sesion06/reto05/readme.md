## Reto final

`bedu_bikes_api.py`

Crea un API sencilla en JSON para modificar una reservación utilizando Bottle y sus [verbos](https://bottlepy.org/docs/dev/api.html#bottle.Bottle.get), para agregar, quitar o editar recorridos de usuarios, almacenada en un archivo CSV. Debe de contar con las siguientes direcciones:

* GET /usuarios: Muestra todos los usuarios registrados.
* GET /usuario/<num>: Muestra un usuario en particular, identificado por ID.
* POST /usuario/<num>/recorrido: Agrega un nuevo producto a la reservación.
* DELETE /usuario/<num>/recorrido/<num>: Elimina un recorrido de cierto usuario.
* PUT /usuario/<num>/reocrrido/<num>: Edita un recorrido existente. El usuario debe existir.

El formato JSON que entregue o reciba debe de ser similar al utilizado en sesiones anteriores.
