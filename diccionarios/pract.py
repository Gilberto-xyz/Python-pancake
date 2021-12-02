# Declaramos el diccionario incial 
diccionario = {'a':2, 'b':4, 'c':6}

# Buscamos la clave 'd' en el diccionario 
if 'd' in diccionario:
    print('La clave d está en el diccionario')
else:
    diccionario.setdefault('d', 8)
    print('Se ha agregado la clave al diccionario')

print(diccionario.get('d'))