# Existen atributos de clase
# Tambien existen los atributos de instancia 

class Usuario:
    username = 'Default username'
    email = ''

# Para usar los atributos de una clase debemos pasalos usando el nombre de la clase 
print(Usuario.username)

# Podemos cambiar los atributos llamandolos y agregandoles el nuevo valor 
Usuario.username = 'Usuario n1'

print(Usuario.username)

