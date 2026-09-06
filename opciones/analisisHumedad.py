def promedio_sector(sectores, matriz):
    sector = input("Indique el ID del sector: ").upper()
    while sector not in sectores:
        print("No es un sector valido")
        sector = input("Indique el ID del sector: ").upper()

    indice = sectores.index(sector)
    mediciones = [c for c in matriz[indice] if c != -1]
    cantidad = len(mediciones)
    if cantidad == 0:
        print("La cantidad de mediciones es de 0")
        return None
    suma = sum(mediciones)
    promedio = suma / cantidad
    return promedio

def promedio_mes(matriz):
    mes = int(input("Indique el numero de mes: "))
    while mes < 1 or mes > 12:
        print("Ingrese un numero valido")
        mes = int(input("Indique el numero de mes: "))
    mes -= 1 

    mediciones = [c[mes] for c in matriz if c[mes] != -1]
    cantidad = len(mediciones)
    if cantidad == 0:
        print("La cantidad de mediciones es de 0")
        return None
    suma = sum(mediciones)
    promedio = suma/cantidad
    return promedio

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



