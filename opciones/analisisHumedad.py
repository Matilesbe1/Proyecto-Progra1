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
        contabilizarSectores(matriz, lst_codigos, tpl_meses)
    elif num==7:
        sectoresAtencion(matriz, lst_codigos, tpl_meses)
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
            if matriz[i][j]<=0:
                continue
            else:
                cant+=1
                suma+=matriz[i][j]
    if cant==0:
        print("\n" + "=" * 55)
        print("           ⚠️  SIN MEDICIONES DISPONIBLES")
        print("=" * 55)
    else:
        promedio=suma/cant
        print("\n" + "=" * 55)
        print(f"💧 PROMEDIO GENERAL DE HUMEDAD: {promedio:.2f}%")
        print("=" * 55)


def obtenerMayorMedicion(matriz, lst_codigos, tpl_meses):
    max = 0
    mayores = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > max:
                max = matriz[i][j]
                mayores = [(i, j)]
            elif matriz[i][j] == max:
                mayores.append((i, j))
            else:
                continue
    if max == 0:
        print("\n" + "=" * 55)
        print("           ⚠️  SIN MEDICIONES DISPONIBLES")
        print("=" * 55)
    else:
        print("\n" + "=" * 55)
        print("           💧 MAYOR HUMEDAD REGISTRADA")
        print("=" * 55)
        for i, j in mayores:
            n, mes = tpl_meses[j]
            print(f"  Sector : {lst_codigos[i]}")
            print(f"  Mes    : {mes}")
            print(f"  Humedad: {max:.2f}%")
            print("-" * 55)
        print("=" * 55)



def obtenerMenorMedicion(matriz, lst_codigos, tpl_meses):
    min = 500
    menores = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 0:
                continue
            if matriz[i][j] < min:
                min = matriz[i][j]
                menores = [(i, j)]
            elif matriz[i][j] == min:
                menores.append((i, j))
    if min == 500:
        print("\n" + "=" * 55)
        print("           ⚠️  SIN MEDICIONES DISPONIBLES")
        print("=" * 55)
    else:
        print("\n" + "=" * 55)
        print("           💧 MENOR HUMEDAD REGISTRADA")
        print("=" * 55)
        for i, j in menores:
            n, mes = tpl_meses[j]
            print(f"  Sector : {lst_codigos[i]}")
            print(f"  Mes    : {mes}")
            print(f"  Humedad: {min:.2f}%")
            print("-" * 55)
        print("=" * 55)

def contabilizarSectores(matriz, lst_codigos, tpl_meses):
    cant=0
    for i in range (len(lst_codigos)):
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
            if matriz[i][j] <= 0:
                continue
            if matriz[i][j] < 50:
                mes = tpl_meses[j][1]
                print(f"  {lst_codigos[i]:<10} | {mes:<10} | {matriz[i][j]:>6.2f}%")
    print("=" * 55)