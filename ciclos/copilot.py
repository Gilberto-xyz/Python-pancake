# Programa que cuenta la cantidad de digitos de un numero 
numero = int(input("Ingrese un numero: "))
contador = 0

while numero > 0:
    numero = numero // 10
    contador += 1

print("La cantidad de digitos es: ", contador)