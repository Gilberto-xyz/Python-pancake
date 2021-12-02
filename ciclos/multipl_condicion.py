# Diferentes mensajes dependiendo la calificacion del alumno 

calificacion = input('Ingresa la calificacion: ')
calificacion = int(calificacion)

if calificacion == 10:
    print('Felicidades, aprobaste con una calificacion perfecta')
elif calificacion == 9 or calificacion == 8:
    print('Felicidades, aprobaste la materia')
elif calificacion == 7 or calificacion == 6:
    print('Aprobaste la materia')
else:
    print('Reprobaste')