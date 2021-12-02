# Funcion que permite sumar dos numeros 

def suma(n1, n2):
    return(n1+n2)

# Entrada del usuario fuera de la funcion
numero_uno = int(input('Ingresa tu primer numero entero:'))
numero_dos = int(input('Ingresa tu segundo numero entero:'))

# Al utilizar el return podemos almacenar el valor obtenido en una variable
result = suma(numero_uno, numero_dos)
print(f'El resultado es: {result}')