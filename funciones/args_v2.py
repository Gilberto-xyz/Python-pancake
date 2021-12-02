# El uso del * no nos limita para usar otros parametros
# Las funciones se separan mediante 2 saltos
def promedio(*args):
    return sum(args) /len(args)


# La funcion puede contener la n cantidad de parametros siempre que este bien definida 
def combinacion(p1, p2, *args, p4=9000):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9)