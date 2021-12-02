## Funcion que nos permite guardar diccionarios
#      *        Hacemos uso de una tupla            args
#      **       Hacemos uso de un diccionario       kwargs

def usuarios(**kwargs):
    print(kwargs, type(kwargs))

usuarios(gilberto=[10, 9, 7], eduardo=[10, 10, 10])

# Funcion que permite almacenar tuplas o diccionarios 
def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, gilberto=[10, 20, 30], eduardo=[40,50,60])