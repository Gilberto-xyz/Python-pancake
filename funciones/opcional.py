# Funcion que permite calcular el area de un circulo 

## Personal
def circulo():
    pi3 = 3.1416
    radio3 = int(input('Ingresa tu radio: '))
    area3 = pi3 * (radio3**2)

    return area3

resultado = circulo()
print(f'{resultado} cm2')


## Curso
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado_curso = area_circulo(19)
print(resultado_curso)