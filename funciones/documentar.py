# Para documentar nos apoyaremos del Docstring
# __doc__ (Modulos, Clases, Metodos y Funciones)

def suma(numero_1, numero_2):
    """
    La funcion suma dos numeros enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parametros

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    200

    """
    return numero_1 + numero_2

# Accedemos a el mediante el llamado help o .__doc__
# print(suma.__doc__)
# print(help(suma))