# Definimos una funcion que contiene test en su documentacion 
def resta(numero_1, numero_2):
    """
    La funcion resta dos numeros enteros 

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la resta de los parametros

    test:
    >>> resta(90,80)
    10

    """
    return numero_1 - numero_2

# Para realizar un test mediante los valores, se ejecuta con el comando
## python -m doctest [nombre_del_archivo]