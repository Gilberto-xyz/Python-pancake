# Podemos busacar palabras o letras en una cadena de texto

titulo_curso = 'Curso profesional de Python, en Python 3.10'

# Usamos el metodo count para contar las veces que aparece una palabra
coincidencias = titulo_curso.count('python')
print(coincidencias)

# Otra forma de buscar una palabra es usando el metodo in
# Devuelve True si la palabra esta en la cadena

print('python' in titulo_curso.lower())

# Estandarizando y luego buscando
print('#######')


texto = titulo_curso.lower()
print('python' in texto)
print(texto.count('python'))