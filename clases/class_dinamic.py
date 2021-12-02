class Usuario:
    username = 'Default user'
    email = 'user@email.com'

# Creamos un objeto a partir de la clase 
# Los atributos dinamicos se pueden agregar al hacer uso del objeto y definiendo nuevos datos
user1 = Usuario()

# se crea un atributo de instancia
user1.username = 'Cody'
print(user1.username)