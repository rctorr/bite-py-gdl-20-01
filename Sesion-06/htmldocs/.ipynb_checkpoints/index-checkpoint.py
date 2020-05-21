from bottle import route, run, template
import lc

@route("/")
def inicio():
    """ Atiende la petición GET / """
    ruta = "."
    carpeta = lc.Carpeta(ruta)
    carpeta.obtener_elementos()
    
    html = """
    <!DOCTYPE html>
    <html>
        <h1>Lista de archivos</h1>
        <hr />
            <table>
            {tabla}
            </table>
        <hr />
    </html>
    """
    tabla = []  # Lista de filas
    for e in carpeta.elementos:
        # Determina si un elemento e es un objeto Archivo o
        # Carpeta
        if isinstance(e, lc.Archivo):
            # Si es archivo, lo agregamos tal cual
            fila = f"<tr><td>{e.tamanio}</td><td>{e.fecha}</td><td>{e.nombre}</td></tr>"
            tabla.append(fila)
        else:
            # Es una carpeta y procesamos sus elementos
            e.obtener_elementos()
            for f in e.elementos:
                fila = f"<tr><td>{f.tamanio}</td><td>{f.fecha}</td><td>{f.nombre}</td></tr>"
                tabla.append(fila)

    # Unimos todas las fila separadas por un salto de línea
    tabla = "\n".join(tabla)
    # Integrar la tabla en el html replanzando la etiqueta.
    html = html.replace("{tabla}", tabla)
    
    
    # return template("<h1>Hola {{ nom }}!</h1>", nom=nombre)
    return html


# GET /hola/nombre
@route("/hola/<nombre>")
def inicio(nombre):
    """ Atiende la petición GET /hola/nombre """
    return template("<h1>Hola {{ nom }}!</h1>", nom=nombre)

# Funciones para atender las peticones de la API
@route("/api/json")
def apijson():
    """ Atendiendo la petición GET /api/json """
    ruta = "."
    carpeta = lc.Carpeta(ruta)
    carpeta.obtener_elementos()

    arch_dict = {
        "Archivos": []
    }
    for e in carpeta.elementos:
        arch_dict["Archivos"].append(e.dict)
    
    return arch_dict















# Equivalente a la ejecución del main()
run(host="localhost", port=8000)