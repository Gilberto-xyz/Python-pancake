# Raw string
lenguajes = 'Python-Clojure-Elixir-C#-Java-C++'

# El metodo split() divide por defecto un string que contiene espacios
lista_lenguajes = lenguajes.split('-') # Podemos dividir los elementos con caracteres especiales

print(lista_lenguajes)

# Podemos dividir los elementos que deseemos declarandolo en el split()
paises = 'España-Francia-Italia-Alemania-Portugal'
lista_paises = paises.split('-',2)
print(lista_paises)

# Podemos generar un string a partir de variables 
capitales = ['Madrid','Paris','Roma','Berlin','Lisboa']

resumen_capitales =  ' '.join(capitales) # Concatenamos los elementos de la lista capitales con un espacio

print(resumen_capitales)

## El metodo split nos permite dividir un string por un caracter especial
## El metodo join nos permite unir una lista de strings con un caracter especial

