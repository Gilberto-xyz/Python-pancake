# Para poder crear una funcion necesitamos definirla con la palabra reservada 'DEF'

# Funcion que permite sumar dos numeros

def suma():
    numero_uno = int(input('Ingresa el primer numero entero: '))
    numero_dos = int(input('Ingresa el segundo numero entero: '))

    resultado = numero_uno + numero_dos
    print(resultado)

suma()