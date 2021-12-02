# Funcion lambda que permite calcular el promedio de calificaciones
promedio = lambda *args : sum(args) / len(args)


# Funcion que demuestra si una calificacion es aprobatoria o no
aprobatorio = lambda calificacion : calificacion >= 7


# Funcion que devuelve una funcion armada con valores lambda
def mostrar_mensaje (func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprovaste la materia con: {promedio}')
    else:
        print(f'Lo siento, no aprobaste. tu calificacion es: {promedio}')

# Ejecucion
mostrar_mensaje(promedio, aprobatorio, 6, 8,6,7)