import funciones 
def llamarFunciones(num, matriz, lst_codigos, tpl_meses):
    if num==1:
        promedio_sector(lst_codigos, matriz,tpl_meses)
    elif num==2:
        promedio_mes(matriz,tpl_meses)
    elif num==3:
        calcularPromedioGeneral(matriz)
    elif num==4:
        obtenerMayorMedicion(matriz)
    elif num==5:
        obtenerMenorMedicion(matriz)
    elif num==6:
        contabilizarSectores(matriz)
    elif num==7:
        sectoresAtencion(matriz)
    funciones.SubOpciones(4, matriz, lst_codigos, tpl_meses)

    print("\nPresione ENTER para continuar...")
    input()
    funciones.SubOpciones(4, matriz, lst_codigos, tpl_meses)

def promedio_sector(sectores, matriz,tpl_meses):
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
    print(f"El promedio es: {promedio}")

    
def promedio_mes(matriz,tpl_meses):
    mes = int(input("Indique el numero de mes: "))
    while mes < 1 or mes > 12:
        print("Ingrese un numero valido")
        mes = int(input("Indique el numero de mes: "))
    mes -= 1 

    mediciones = [c[mes] for c in matriz if len(c) > mes and c[mes] != -1]
    cantidad = len(mediciones)
    if cantidad == 0:
        print("La cantidad de mediciones es de 0")
        return None
    suma = sum(mediciones)
    promedio = suma/cantidad
    print(f"El promedio es: {promedio}")


def calcularPromedioGeneral(matriz):
    cant=0
    suma=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==0:
                continue
            else:
                cant+=1
                suma+=matriz[i][j]
    promedio=suma/cant
    print(f'el promedio general de humedad de los sectores es: {promedio}')


def obtenerMayorMedicion(matriz):
    max=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]>max:
                max=matriz[i][j]
            else:
                continue
    print(f'el sector con mayor humedad registrada es: {max}')
    print(f'poner sector completo')

def obtenerMenorMedicion(matriz):
    min=matriz[0][0]
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==0:
                continue
            else:
                if matriz[i][j]<min:
                    min=matriz[i][j]
                else:
                    continue
    print(f'el sector con menor humedad registrada es: {min}')
    print(f'poner sector completo')


def contabilizarSectores(matriz):
    cant=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==0:
                continue
            else:
                cant+=1
    print(f'{cant} sectores fueron cargados')


def sectoresAtencion(matriz):
    lstAtencion=[]
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==0:
                continue
            else:
                if matriz[i][j]<50:
                    lstAtencion.append(matriz[i][j])
    print(f'Estos son los sectores que requieren atencion: ')

    for s in lstAtencion:
        print(f'informe completo')



