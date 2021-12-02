## Refactor al codigo de funciones anidadas

# Funcion que nos permite simular operaciones bancarias
def operacion(cantidad, balance, tipo='deposito'):


    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad < balance:
            return balance - cantidad
        else:
            return None


    if tipo == 'deposito':
        return deposito(cantidad, balance)

    elif tipo == 'retiro':
        return retiro(cantidad, balance)

# Por defecto, nos realiza un deposito con los valores que agregamos 
resultado = operacion(10, 30, 'retiro')
print(resultado)
