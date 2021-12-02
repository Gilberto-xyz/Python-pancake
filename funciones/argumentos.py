# Podemos crear funciones que permitan n cantidad de argumentos 

## funcion que permite calcular el promedio de un listado de numeros enteros

# agregamos un * al inicio de nuestro parametro para indicar que sera una tupla y asi podra trabajar con todos los argumentos que le pasemos
# por convesion de la comunidad se nombrara *args a todas aquellas tuplas que recibiran muchos paramentros

def promedio(*args):
    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)