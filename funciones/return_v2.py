# En la funcion podemos retornar mas de un valor, pero esto no se recomienda

# Retorna la suma de 2 valores y un mensaje
def suma(n1, n2):
    return(n1+n2, 'Se han sumado 2 valores')

# Entrada del usuario fuera de la funcion
numero_uno = int(input('Ingresa tu primer numero entero:'))
numero_dos = int(input('Ingresa tu segundo numero entero:'))

# Al utilizar el return podemos almacenar el valor obtenido en una variable
# Al retornar mas de 2 valores, se necesitan guardar en las variables para evitar imprimir una tupla

numeros, texto = suma(numero_uno, numero_dos)
print(f'El resultado es: {numeros}')
print(texto)