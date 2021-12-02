# Calificacion aprobatoria segun el alumno 

calificacion = input('Ingresa tu calificacion: ')
calificacion = int(calificacion)

# Metodo tradicional
color = None

if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'
print(calificacion, color)

# Refactorizando codigo
color = 'verde' if calificacion >= 7 else 'Rojo'
print(calificacion, color)