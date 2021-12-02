# Se recomienda usar generadores siempre que se hace uso de coleciones
# el generador no consume espacio extra en la memoria, tan solo cuando se hace uso de esta

def pares(): # Generador  -> Lazy iterator
    for numero in range(0, 100, 2):
        yield numero # La funcion susprende su ejecucion

        print('Se realuda la ejecucion')

# Gracias al generador podemos mostrar los elementos bajo demanda
# Almacenamos el generador en una variable
generador = pares()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))