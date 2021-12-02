# Una funcion dinamica que permite generar otra funcion
# Esta funcion puede acceder a las variables locales aun cuando la primera haya finalizado

def saludar(username):
    mensaje = f'Hola {username}' # Esta es una variable local

    def mostrar_mensaje(): # Funcion anidada
        print(mensaje)

    return mostrar_mensaje

# Una funcion que tiene memoria
username = 'cody'
respuesta = saludar(username)

respuesta()