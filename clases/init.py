# Cuando se cree un objeto de tipo usuario, se creen 2 atributos 

class Usuario():

    def __init__(self):
        self.username = ''
        self.password = ''

# Ese metodo se va a ejecutar cuando instanciamos a la clase

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)