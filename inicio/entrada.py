# Todos los datos de entrada del programa se guardan en variables de tipo string
nombre_completo = input('Ingresa tu nombre completo: ')

# Todos los datos de tipo numerico permiten generar un int a partir del string
edad = input('Introduce tu edad: ')
edad =  int(edad)
fecha_nacimiento = 2021 - edad
print('Naciste en: ', fecha_nacimiento)

# Todos los datos de tipo numerico de punto flotante permiten generar un float a partir del string
altura = input('Introduce tu altura: ')
altura = float(altura)

# Todos los datos de tipo texto se pueden convertir de string a bool
autorizacion = input('Autorizas el programa? (si/no)')
autorizacion = autorizacion == 'si'
