# Definimos el diccionario
diccionario = {'a':1, 'b':2, 'c':3, 'd':4 }

# Obtenemos el valor de un elemento del diccionario
valor = diccionario['c']
print(valor)

# Averiguar si un valor se encuentra en el diccionario
search = 'z' in diccionario
print(search)
print('x' in diccionario)


## GET

# Obtener el valor de manera segura con get
elemento = diccionario.get('c')
print(elemento)

# Se puede mostrar un argumento en el caso de que la llave no exista 
print(diccionario.get('v','La llave no existe en el diccionario'))


## SETDEFAULT

# Si el valor no existe, se puede agregar con setdefault
valor_default = diccionario.setdefault('y',90)
print(valor_default)
print(diccionario)