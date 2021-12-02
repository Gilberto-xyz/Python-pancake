# Eliminar elementos de un diccionario
diccionario  = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

# Imprimimos el diccionario y su longitud
print(diccionario,len(diccionario))

## Primer metodo para eliminar un elemento del diccionario
del diccionario['c']

## Segundo metodo para eliminar un elemento del diccionario
valor = diccionario.pop('e')
print('valor eliminado: ',valor)

# Mostramos el diccionario actualizado
print(diccionario, len(diccionario))

## Limpiamos todo el diccionario
diccionario.clear()
print(diccionario, len(diccionario))