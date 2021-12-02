# La funcion range no permite crear una secuencia de numeros que podemos iterar
rango  = range(6)

# Iteramos los valores del rango con un for 
for valor in rango:
    print(valor)

# Podemos trabjar directamente con el valor range 
# se puede definir tambien el inicio y el final del rango 
for valor in range(20, 31):
    print(valor)
print('Fin del rango 30')

# Imprimimos un valor de rango con un salto cada tiempo
##          inicio  final   saltos
for valor in range(0,21,2):
    print(valor)