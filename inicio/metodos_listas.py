# Raw list

numeritos = [8, 90, 1, 5, 44, 123, 132, 600, 3, 4, 0, 50, 20]

# Ordenar lista de manera ascendente
numeritos.sort()
print(numeritos)

# Buscar un numero en la lista
print(132 in numeritos) # True/False

# Buscar un numero en la lista
print(numeritos.index(132)) # Posicion del numero

# Mostrar el numero mas pequeño
print(min(numeritos))
print(numeritos[0])

# Mostrar el numero mas grande
print(max(numeritos))
print(numeritos[-1])


# Ordenar lista de manera descendente
numeritos.sort(reverse=True)
print(numeritos)


##      sort()     sort(reverse=True)
##      min()      max()
##      lista[0]   lista[-1]
##      in          index()
##      not in 