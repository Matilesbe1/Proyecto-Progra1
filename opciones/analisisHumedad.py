import funciones 
def llamarFunciones(num, matriz, lst_codigos, tpl_meses):
    if num==1:
        promedio_sector(lst_codigos, matriz,tpl_meses)
    elif num==2:
        promedio_mes(matriz,tpl_meses)
    elif num==3:
        calcularPromedioGeneral(matriz)
    elif num==4:
        obtenerMayorMedicion(matriz, lst_codigos, tpl_meses)
    elif num==5:
        obtenerMenorMedicion(matriz, lst_codigos, tpl_meses)
    elif num==6:
        contabilizarSectores(matriz)
    elif num==7:
        sectoresAtencion(matriz, lst_codigos, tpl_meses)
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
    print("\n" + "=" * 55)
    print(f"💧 PROMEDIO GENERAL DE HUMEDAD: {promedio:.2f}%")
    print("=" * 55)


def obtenerMayorMedicion(matriz, lst_codigos, tpl_meses):
    max=0
    index_cod=0
    index_mes=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]>max:
                max=matriz[i][j]
                index_cod=i
                index_mes=j
            else:
                continue
    n, mes=tpl_meses[index_mes]
    print("\n" + "=" * 55)
    print("           💧 MAYOR HUMEDAD REGISTRADA")
    print("=" * 55)
    print(f"  Sector : {lst_codigos[index_cod]}")
    print(f"  Mes    : {mes}")
    print(f"  Humedad: {max:.2f}%")
    print("=" * 55)

def obtenerMenorMedicion(matriz, lst_codigos, tpl_meses):
    min=matriz[0][0]
    index_cod=0
    index_mes=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==0:
                continue
            else:
                if matriz[i][j]<min:
                    min=matriz[i][j]
                    index_cod=i
                    index_mes=j
                else:
                    continue
    n, mes=tpl_meses[index_mes]
    print("\n" + "=" * 55)
    print("           💧 MENOR HUMEDAD REGISTRADA")
    print("=" * 55)
    print(f"  Sector : {lst_codigos[index_cod]}")
    print(f"  Mes    : {mes}")
    print(f"  Humedad: {min:.2f}%")
    print("=" * 55)

def contabilizarSectores(matriz):
    cant=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==0:
                continue
            else:
                cant+=1
    print("\n" + "=" * 55)
    print(f"        ✓ {cant} SECTORES CARGADOS")
    print("=" * 55)


def sectoresAtencion(matriz, lst_codigos, tpl_meses):
    print("\n" + "=" * 55)
    print("       SECTORES QUE REQUIEREN ATENCIÓN")
    print("=" * 55)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                continue
            if matriz[i][j] < 50:
                mes = tpl_meses[j][1]
                print(f"  {lst_codigos[i]:<10} | {mes:<10} | {matriz[i][j]:>6.2f}%")
    print("=" * 55)