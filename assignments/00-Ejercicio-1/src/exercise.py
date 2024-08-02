'''
Ejercicio 1-Equivalente
'''
def equivalente(horas, minutos, segundos):
    '''
        Parametros de entrada: horas, minutos, segundos
        Valor de salida: total en segundos
    '''
    minutos_a_segundos = minutos * 60
    horas_a_minutos = horas * 60
    total_segundos = minutos_a_segundos + horas_a_minutos * 60 + segundos

    return total_segundos

def main():
    '''
    Funcion principal
    '''
    #escribe tu código abajo de esta línea
    horas = int(input("Horas:"))
    minutos = int(input("Minutos:"))
    segundos = int(input("Segundos:"))

    print(f"Tiempo equivalente en segundos={equivalente(horas, minutos, segundos)}")

if __name__=='__main__':
    main()
