#Palindromos con un slicing

palindromo="Somos o no somos"
print(palindromo)

#invirtiendo el orden de los caracteres para comprobar el palindromo
print(palindromo[::-1])

#Cuadro magico de 5x5
print('Palindromo multiple "Cuadro Magico"')

arreglo = [ ["S A T O R"],
            ["A R E P O"],
            ["T E N E T"],
            ["O P E R A"],
            ["R O T A S"] ]

for i in range(len(arreglo)):
    for j in range(len(arreglo[i])):
        print(arreglo[i][j], end=" ")
    print()