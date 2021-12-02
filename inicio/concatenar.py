nombre = 'Angela'
apellido = 'Estrada'

# Concatenamos el nombre y el apellido mediante el operador +
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

# Concatenamos el nombre y el apellido mediante un string base y %s donde se incluiran los valores
nombre_r = '%s %s %s.'%(nombre, apellido,'Aguilar')
print(nombre_r)

# Concatenar el nombre y apellidos mediante un string base con string holders y el metodo format
nombre_format = 'Amiga: {} {}'.format(nombre, apellido)
print(nombre_format)

# Aplicar el metodo format con una lista de valores, podemos ordenarlos de la manera que queramos
nombre_format_v2 = 'Usuario: {nombre} {apellido} {segundo_apellido}'.format(
    nombre = nombre,
    apellido = apellido,
    segundo_apellido = 'Gonzales'
)
print(nombre_format_v2)
