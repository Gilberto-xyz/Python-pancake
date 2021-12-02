# Podemos definir una tupla que almacena valores y despues asignarle esos valores en una variable

# Definimos una tupla
numeros = (1, 2, 3)

# Definimos las variables que almacenaran los valores de la tupla
uno, dos, tres = numeros
# se puede hacer de la manera extensa, pero consume mas lineas de codigo
# uno = numeros[0]
# dos = numeros[1]
# tres = numeros[2]

print(uno)
print(dos)
print(tres)


# Cuando hay demasiados valores dentro de una tupla y pocas variables se puede usar una ultima variable que guardara los valores restantes en una lista
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Se crea una lista a partir de una tupla de los valores que no fueron desempaquetados
one, two, three, four, *valores_sobrantes = tupla

print(one)
print(two)
print(three)
print(four)
print(valores_sobrantes)

# Se puede tambien descartar los elementos de una tupla desempaquetada 
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, *_ = tupla
print(uno)
print(dos)
print(tres)


# Se puede tambien descartar elementos, guardando los 2 ultimos valores de una lista
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, *_, nueve, dies = tupla
print(uno)
print(dos)
print(tres)
print(nueve)
print(dies)


##   *  -> Lista
##   *_ -> Omitir valores sobrantes
##   _  -> Omite un valor de la tupla