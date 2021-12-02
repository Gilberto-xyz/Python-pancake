## Scope
# El valor de una variable se determina mediante su ubicacion
# Las variables globales o locales influyen el en comportamiento

# La variable global puede ser ocupada en cualquier bloque
animal = 'Tigre'

def imprimir_animal():
    # La variable local solo se puede ocupar en el bloque donde fue declarada
    global animal
    animal = 'Perro'
    print(id(animal))
    print(animal)

# Uso de la funcion
imprimir_animal()
# llamada a la variable gloabal
print(id(animal))
print(animal)

# Podemos identificar un elemento mediante su identificador
# id(elemento)

# Podemos usar y modificar una variable global mediante la palabra global