'''
Ejercicio 3-Operaciones aritmeticas
'''
def operacionAritmetica(n1, n2, clave):
    '''
        Parametros de entrada: numero 1, numero 2, clave de operacion
        Valor de salida: resultado de la operacion
    '''
    
    if clave == 's':
        return n1 + n2
    elif clave == 'r':
        return n1 - n2
    elif clave == 'm':
        return n1 * n2
    elif clave == 'd':
        return n1 / n2
    else:
        return 999

def main():
    '''
    Funcion principal
    '''
    #escribe tu código abajo de esta línea
    
    n1  = float(input("Valor 1:"))
    n2  = float(input("Valor 2:"))
    cve = input("Clave:")

    print(f"{n1:<5.2f}{cve}{n2:<5.2f}={operacionAritmetica(n1,n2,cve):<5.2f}")


if __name__=='__main__':
    main()
