# Palabras reservadas que nos permiten interrumpir el flujo del programa
# Break detiene el programa
# Continue permite pasar a la siguiente iteracion

titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:
    if caracter == 'P':
        print('Letra mayuscula detectada')
        break
    
    print(caracter)


for caracter in titulo_curso:
    if caracter == ' ':
        continue

    print(caracter)