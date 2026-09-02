def calcularPromedioGeneral(sectores):
    cant=len(sectores)
    suma=0
    for sector in sectores:
        id, mes, humedad=sector
        suma+=humedad
    promedio=suma/cant
    print(f'el promedio general de humedad de los sectores es: {promedio}')


def obtenerMayorMedicion(sectores):
    max=0
    for sector in sectores:
        id, mes, humedad= sector
        if max<humedad:
            max=humedad
        else:
            continue
    print(f'el sector con mayor humedad registrada es: ')
    print(f'poner sector completo')

def obtenerMenorMedicion(sectores):
    min=sectores[0]
    for sector in sectores:
        id, mes, humedad=sector
        if min>humedad:
            min=humedad
        else: 
            continue
    print(f'el sector con menor medicion registrada es: ')
    print(f'poner secotr completo')

def contabilizarSectores(sectores):
    cont=len(sectores)
    print(f'Hay un total de {cont} sectores')

def sectoresAtencion(sectores):
    lstAtencion=[]
    for sector in sectores:
        id, mes, humedad=sector
        if humedad<=50:
            lstAtencion.append(sector)
    print(f'Estos son los sectores que requieren atencion: ')
    for s in lstAtencion:
        id, mes, humedad=s
        print(f'informe completo')



