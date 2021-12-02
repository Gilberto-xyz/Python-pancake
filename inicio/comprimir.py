# Comprimir variables 

lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

comprimido = zip(lista, tupla) # Comprime los elementos (Lista y Tupla)
comprimido = tuple(comprimido) # Descomrime los elementos en una tupla

print(comprimido)