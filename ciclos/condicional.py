resultado = input('Valor a comparar: ')
resultado = int(resultado)

primer_valor = input('Valor minimo: ')
primer_valor = int(primer_valor)

segundo_valor = input('Valor maximo: ')
segundo_valor = int(segundo_valor)

if resultado > primer_valor and resultado < segundo_valor:
    print(f'La variable {resultado} se encuentra entre {primer_valor} y {segundo_valor}')
else:
    print(f'La variable esta fuera de los rangos de {primer_valor} y {segundo_valor}')