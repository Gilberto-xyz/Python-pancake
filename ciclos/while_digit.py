# Programa que cuenta la cantidad de digitos de un numero
# Se ocupa cuando no sabemos la cantidad de iteraciones que tendremos al final

numero = input('Ingresa tu numero: ')
numero = int(numero)

contador_digitos = 0

while numero >=1:
    contador_digitos = contador_digitos +1
    numero = numero / 10

print(contador_digitos)