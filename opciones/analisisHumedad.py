import funciones
import opciones.informes
import configuracion.cultivos
def llamarFunciones(num, matriz, lst_codigos, tpl_meses, dicc):
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
        contabilizarSectores(matriz, lst_codigos, tpl_meses, dicc)
    elif num==7:
        sectoresAtencion(matriz, lst_codigos, tpl_meses, dicc)

    input("\nPresione ENTER para continuar...")
    funciones.SubOpciones(4, matriz, lst_codigos, tpl_meses, dicc)

def promedio_sector(sectores, matriz,tpl_meses):
    sector = input("Indique el ID del sector: ").upper()
    while sector not in sectores:
        print("No es un sector valido")
        sector = input("Indique el ID del sector: ").upper()

    indice = sectores.index(sector)
    mediciones = [c for c in matriz[indice] if c != -1]
    cantidad = len(mediciones)
    if cantidad == 0:
        print("\n" + "=" * 35)
        print("La cantidad de mediciones es de 0")
        print("=" * 35)
        return None
    suma = sum(mediciones)
    promedio = suma / cantidad
    print("\n" + "=" * 23)
    print(f"El promedio es: {promedio:.2f}")
    print("=" * 23)

    
def promedio_mes(matriz,tpl_meses):
    mes = int(input("Indique el numero de mes: "))
    while mes < 1 or mes > 12:
        print("Ingrese un numero valido")
        mes = int(input("Indique el numero de mes: "))
    mes -= 1 

    mediciones = [c[mes] for c in matriz if len(c) > mes and c[mes] != -1]
    cantidad = len(mediciones)
    if cantidad == 0:
        print("\n" + "=" * 35)
        print("La cantidad de mediciones es de 0")
        print("=" * 35)
        return None
    suma = sum(mediciones)
    promedio = suma/cantidad
    print("\n" + "=" * 23)
    print(f"El promedio es: {promedio:.2f}")
    print("=" * 23)


def calcularPromedioGeneral(matriz):
    cant=0
    suma=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j]==-1:
                continue
            else:
                cant+=1
                suma+=matriz[i][j]
    if cant==0:
        print("\n" + "=" * 55)
        print("           ⚠️  SIN MEDICIONES DISPONIBLES")
        print("=" * 55)
        return False
    else:
        promedio=suma/cant
        print("\n" + "=" * 55)
        print(f"💧 PROMEDIO GENERAL DE HUMEDAD: {promedio:.2f}%")
        print("=" * 55)
        return True


def obtenerMayorMedicion(matriz, lst_codigos, tpl_meses):
    max = -1
    indice_sector = -1
    indice_mes = -1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > max:
                max = matriz[i][j]
                indice_sector = i
                indice_mes = j
            else:
                continue
    if max == -1:
        print("\n" + "=" * 55)
        print("           ⚠️  SIN MEDICIONES DISPONIBLES")
        print("=" * 55)
    else:
        print("\n" + "=" * 55)
        print("           💧 MAYOR HUMEDAD REGISTRADA")
        print("=" * 55)
        n, mes = tpl_meses[indice_mes]
        print(f"  Sector : {lst_codigos[indice_sector]}")
        print(f"  Mes    : {mes}")
        print(f"  Humedad: {max:.2f}%")
        print("-" * 55)
        print("=" * 55)


def obtenerMenorMedicion(matriz, lst_codigos, tpl_meses):
    min = 500
    indice_sector = -1
    indice_mes = -1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 0:
                continue
            if matriz[i][j] < min:
                min = matriz[i][j]
                indice_sector = i
                indice_mes = j
    if min == 500:
        print("\n" + "=" * 55)
        print("           ⚠️  SIN MEDICIONES DISPONIBLES")
        print("=" * 55)
    else:
        print("\n" + "=" * 55)
        print("           💧 MENOR HUMEDAD REGISTRADA")
        print("=" * 55)
        n, mes = tpl_meses[indice_mes]
        print(f"  Sector : {lst_codigos[indice_sector]}")
        print(f"  Mes    : {mes}")
        print(f"  Humedad: {min:.2f}%")
        print("-" * 55)
        print("=" * 55)

def contabilizarSectores(matriz, lst_codigos, tpl_meses, rangos):
    indice_mes, nombre_mes = opciones.informes.pedir_mes_valido(tpl_meses)
    conteo = {"Crítico": 0, "Bajo": 0, "Adecuado": 0, "Excesivo": 0}
    for i in range(len(lst_codigos)):
        humedad = matriz[i][indice_mes]
        if humedad != -1:
            estado = opciones.informes.determinar_estado(humedad, lst_codigos[i], rangos)
            if estado in conteo:
                conteo[estado] += 1
    print("\n" + "=" * 55)
    print(f"        SECTORES SEGÚN ESTADO - {nombre_mes}")
    for estado in conteo:
        print(f"  {estado}: {conteo[estado]}")
    if sum(conteo.values()) == 0:
        print("No hay mediciones disponibles para este mes.")
    print("=" * 55)


def sectoresAtencion(matriz, lst_codigos, tpl_meses, rangos):
    indice_mes, nombre_mes = opciones.informes.pedir_mes_valido(tpl_meses)
    sectores = [i for i in range(len(lst_codigos))
                if matriz[i][indice_mes] != -1 and
                opciones.informes.determinar_estado(matriz[i][indice_mes], lst_codigos[i], rangos) in ("Crítico", "Bajo")]
    print("\n" + "=" * 55)
    print(f"       SECTORES QUE REQUIEREN ATENCIÓN - {nombre_mes}")
    if len(sectores) == 0:
        print("Ningún sector requiere atención en este mes.")
    for i in sectores:
        cultivo = configuracion.cultivos.obtener_cultivo(lst_codigos[i], rangos)
        estado = opciones.informes.determinar_estado(matriz[i][indice_mes], lst_codigos[i], rangos)
        print(f"  {lst_codigos[i]} | {cultivo} | {matriz[i][indice_mes]}% | {estado}")
    print("=" * 55)
