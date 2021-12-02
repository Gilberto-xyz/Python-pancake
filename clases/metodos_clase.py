class Circulo:

    pi = 3.141592

    @classmethod #Definimos que el metodo area es un metodo de clase
    def area(cls, radio):# Metodo que nos permite calcular el area de un circulo
        return cls.pi * (radio ** 2)


resultado = Circulo.area(14)
print(resultado)