# Es una funcion que toma de entrada otra funcion que a su vez retorna otra funcion
# input   output     funcion principal
## Permite extender las funcionalidades sin tener que modificar la funcion original 

"""
    a -> La funcion principal (Decorador)
    b -> La funcion de decorar
    c -> La funcion decorada

    a(b) -> c
"""

# Funcion decorada
def funcion_a(funcion_b):

    def funcion_c():
        # Para hacer uso de la otra funcion, debemos de pasarle el parametro definido
        print('>> Antes del llamado a la funcion')

        funcion_b()

        print('>> Despues del llamado a la funcion')


    return funcion_c

# funcion extra que retorna un saludo
# Para pasarle un parametro a una funcion la llamaremos con @ y le pasaremos la funcion que queremos decorar
# no estamos usando la nueva funcion, estamos usando la decorada
@funcion_a
def saludar():
    print('Hola, nos encontramos dentro de la funcion saludar xc')

saludar()

## Podemos realizar tareas antes y despues del llamado de una funcion