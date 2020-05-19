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
        if isinstance(e, lc.Archivo):
            fila = f"<tr><td>{e.tamanio}</td><td>{e.fecha}</td><td>{e.nombre}</td></tr>"
            tabla.append(fila)
        else:
            e.obtener_elementos()
            for f in e.elementos:
                fila = f"<tr><td>{f.tamanio}</td><td>{f.fecha}</td><td>{f.nombre}</td></tr>"
                tabla.append(fila)
    
    tabla = "\n".join(tabla)
    html = html.replace("{tabla}", tabla)
    
    
    # return template("<h1>Hola {{ nom }}!</h1>", nom=nombre)
    return html


# GET /hola/nombre
@route("/hola/<nombre>")
def inicio(nombre):
    """ Atiende la petición GET /hola/nombre """
    return template("<h1>Hola {{ nom }}!</h1>", nom=nombre)



# Equivalente a la ejecución del main()
run(host="localhost", port=8000)