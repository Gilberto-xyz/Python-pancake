# Podemos usar una funcion dentro de otra funcion

# funcion que nos permite simular una transaccion bancaria 
def operacion():


    def deposito(cantidad, balance):
        return (cantidad + balance)


    def retiro(cantidad, balance):
        if cantidad < balance:
            return balance - cantidad
        else:
            return None

    print(deposito(10,20))
    print(retiro(50,90))

operacion()