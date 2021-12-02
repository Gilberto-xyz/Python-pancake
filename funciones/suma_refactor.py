# Refactor de la funcion que permite sumar dos numeros 

# Funcion que permite sumar dos numeros independientemente de su entrada 
## Las varibles de la funcion son completamente independientes
def suma(n1, n2):
    resultado = n1 + n2
    print(resultado)

numero_uno = int(input('Ingresa tu primer numero entero: '))
numero_dos = int(input('Ingresa tu segundo numero entero: '))

# Agregamos argumentos a nuestra funcion para que realice la operacion
suma(numero_uno, numero_dos)
