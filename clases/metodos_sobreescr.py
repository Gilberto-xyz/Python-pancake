class Animal():# Clase padre

    def comer(self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')


class Mascota(Animal):# Clase Hibrida
    def comer(self):
        super().comer()
        print('La mascota come')


class Felino():
    def cazar(self):
        print('El felino caza')


class Gato(Mascota, Felino):# Clase hija

    def __init__(self,nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'El {self.nombre} come')

    def dormir(self):
        print(f'El {self.nombre} duerme')

bolita = Gato('Señor bolita')

bolita.comer()
bolita.dormir()

# El metodo Super() nos permite acceder a la clase padre de manera inmediata para poder ocupar sus metodos
