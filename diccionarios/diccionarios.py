# Definimos el diccionario

elementos = {}

# Diccinario con clave y valor
elementos['nombre'] = 'Cody'
elementos[(2,4,6)] = 'La llave es una tupla'

# Si la llave no existe, se crea
# Si la llave existe, se reemplaza
elementos['apellido'] = 'Hernandez'
elementos['nombre'] = 'Eduardo'

print(len(elementos))
print(elementos)

diccionario = {'a':1, 'b':2, 'c':3, 'a':4}
print(diccionario)