nombre = 'Gilberto'
apellido = 'Nava Marcos'

# Por defecto se separa con un espacio
# Podemos definir el separador
print(nombre, apellido, sep = ' espacio ')

# Podemos imprimir valores generando interpolaciones
nombre_completo = f'Nombre: {nombre} {apellido}'
print(nombre_completo)

print(f'Nombre: {nombre} {apellido}')