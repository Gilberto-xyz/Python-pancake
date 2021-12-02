# La herencia multiple permite mostrar resultados de varias clases padre

class Mascota:# Primer clase padre

    def comer(self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')


class Felino:# Segunda clase padre

    def cazar(self):
        print('El felino caza')


class Gato(Mascota, Felino):# Clase hija
    pass


bolita = Gato()

bolita.comer()
bolita.dormir()
bolita.cazar()