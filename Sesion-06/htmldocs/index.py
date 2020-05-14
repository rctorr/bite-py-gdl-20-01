from bottle import route, run, template

# GET /hola/nombre
@route("/hola/<nombre>")
def inicio(nombre):
    """ Atiende la petición GET /hola/nombre """
    return template("<h1>Hola {{ nom }}!</h1>", nom=nombre)



# Equivalente a la ejecución del main()
run(host="localhost", port=8000)