lista_cursos = ['Python', 'Java', 'C#', 'JavaScript', 'PHP', 'C++', 'C'] 
lista_cursos_2 = ['Scala', 'Rails', 'Rust']
print(lista_cursos)

# Agrega un elemento al final de la lista
lista_cursos.append('Elixir')

# Muestra la lista de cursos
print(lista_cursos)

# Muestra la longitud de la lista
print(len(lista_cursos))

# Agregamos un elemento en la posicion especificada
lista_cursos.insert(0, 'SQL')
print(lista_cursos)

# Podemos agregar los elementos de una lista a otra
lista_cursos.extend(lista_cursos_2)
print(lista_cursos)

# Podemos eliminar un elemento de la lista mediante su nombre
lista_cursos.remove('PHP')
print(lista_cursos)
# Podemos eliminar un elemento de la lista mediante su posicion
del lista_cursos[5]
print(lista_cursos)

# insert     append       extend   remove
# len        del          clear 

# Podemos eliminar todos los elementos de una lista
lista_cursos.clear()
print(lista_cursos)

