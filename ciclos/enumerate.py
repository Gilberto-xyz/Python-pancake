# Funcion enumerate

# Definimos la lista con la que vamos a trabajar
numeros = [10, 20, 30, 40, 50, 60, 70, 80]

# Retorna un objeto iterable que posee tuplas
# El primer elemento sera un indice, el segundo sera el elemento perse que estamos iterando
for indice, numero in enumerate(numeros):
    print(indice, numero)

## Podemos definir con que elemento inicia el enumerado
for indice, valor in enumerate(numeros, 50):
    print(indice, valor)