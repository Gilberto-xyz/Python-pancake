# Atributos de instancia

class Usuario:
    # Atributos de clase 
    username = 'Default user'
    email = 'user@email.com'

# Creamos un objeto que permita acceder a los atributos de la clase
# Podemos agregar de forma dinamica atributos a un objeto
user1 = Usuario()
"""
1.- Verifica su el atributo existe dentro del objeto
2.- Verifica si el atributo existe dentro de la clase (Solo funciona en lectura)
3.- Lanza el error
"""
print(user1.username)