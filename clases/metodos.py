# Para crear metodos, basta con definir funciones dentro de las clases 

class Usuario:
    def inicializar(self):
        self.username = ''
        self.password = ''

user1 = Usuario()
user2 = Usuario()

user1.inicializar()
user2.inicializar()


print(user1.__dict__)
print(user2.__dict__)
