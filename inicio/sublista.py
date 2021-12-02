# Python permite crear sublistas de listas.

#               0       1       2       3       4       5         6   
empleados = ['Juan', 'Pedro', 'Ana', 'Maria', 'Luis', 'Carlos', 'Julieta']

# [Inicio : Fin : Saltos]


# Sublista de empleados
print(empleados)

# Sublista de empleados desde el indice 0 hasta el indice 3
sub_lista = empleados[0:3]
print(sub_lista)

# Sublista de empleados desde el indice 2 hasta los ultimos elementos
sub_lista = empleados[2:]
print(sub_lista)

# Sublista de empleados desde el indice 0 hasta el indice 3
sub_lista = empleados[:3]
print(sub_lista)

# Sublista de empleados desde el indice 0 al 5 con 2 saltos
sub_lista = empleados[0:5:2]
print(sub_lista)

# Sublista de empleados que invierte el orden de los elementos
sub_lista = empleados[::-1]
print(sub_lista)