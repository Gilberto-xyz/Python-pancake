diccionario = {'a': 1, 'b': 2, 'c': 3, 'd':4}

## Imprimimos las llaves que tiene el diccionario 
llaves = diccionario.keys()
print('Las llaves son: \n',llaves)

# Pasamos las llaves a una tupla
tupla = tuple(llaves)
print(tupla)



## Imprimimos los valores que tiene el diccionario 
valores = diccionario.values()
print('Los valores son: \n',valores)

lista = tuple(valores)
print(lista)

## Imprimir el listado de los elementos del diccionario 
print('Los elementos son: \n',tuple(diccionario.items()))