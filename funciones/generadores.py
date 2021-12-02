# Tipo especial de funcion que retorna objetos que podemos iterar sin que la funcion finalice

# Generador que nos permite iterar entre todos los numeros pares

## Creamos a la funcion que se convierte a generador
def pares():
    for numero in range(0, 100, 2):
        # return numero   // Esto nos retorna el primer numero y finaliza el programa 
        yield numero # Suspende la ejecucion para retornar un objeto para luego reanudar donde se detuvo
        print('Pequeña pausa')

## Mandamos a llamar a la funcion
print(pares())

for par in pares():
    print(par)