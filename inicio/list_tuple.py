# Las listas y tuplas pueden compartirse elementos

cursos_lista = ['Python', 'Java', 'C++', 'JavaScript', 'C#']

# Generando una tupla a partir de una lista
cursos_tupla = tuple(cursos_lista)
print(cursos_lista)
print(cursos_tupla)

tupla_niveles = ('Básico', 'Intermedio', 'Avanzado')

# Generando una lista a partir de una tupla
lista_niveles = list(tupla_niveles)
print(tupla_niveles)
print(lista_niveles)
