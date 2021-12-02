from types import GeneratorType


class Mascota: # Clase padre

    def comer(self):
        print('La mascota come.')

    def dormir(self):
        print('La mascota duerme.')



class Perro(Mascota): # Clase hija
    pass

class Gato(Mascota): # Clase hija
    pass

chingon = Perro()
chingon.comer()
chingon.dormir()

sr_bolita = Gato()
sr_bolita.comer()
sr_bolita.dormir()