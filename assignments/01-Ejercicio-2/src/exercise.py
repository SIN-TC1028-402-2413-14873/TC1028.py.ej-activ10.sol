'''
Ejercicio 2-Area de Rectangulo
'''
def areaRect(largo, ancho):
    '''
        Parametros de entrada: largo, ancho
        Valor de salida: area Rectangulo
    '''
    
    area_rectangulo = largo * ancho

    return area_rectangulo

def perimetroRect(largo, ancho):
    '''
        Parametros de entrada: largo, ancho
        Valor de salida: perimetro Rectangulo
    '''
    
    perimetro_rectangulo = 2 * (largo + ancho)

    return perimetro_rectangulo

def main():
    '''
    Funcion principal
    '''
    #escribe tu código abajo de esta línea
    
    largo = float(input("Largo:"))
    ancho = float(input("Ancho:"))
    opcion = input("¿a=Area/p=Perimetro?")

    if (opcion.upper() == "A"):
        print(f"Area={areaRect(largo, ancho):<10.1f}")
    else:
        print(f"Perimetro={perimetroRect(largo, ancho):<10.1f}") 


if __name__=='__main__':
    main()
