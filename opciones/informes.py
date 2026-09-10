import funciones
def llamarFunciones (num,matriz,lst_codigos,tpl_meses):
    if num == 1:
        informe_general_campo(matriz,lst_codigos,tpl_meses)
    if num == 2:
        informe_sector(matriz,lst_codigos, tpl_meses)
    if num ==3:
        informe_mensual(matriz,lst_codigos,tpl_meses)
    if num == 4:
        sectores_atencion(matriz,lst_codigos,tpl_meses)
    if num == 5:
       ranking_mensual_humedad(matriz,lst_codigos,tpl_meses) 

    input("\nPresione ENTER para continuar...")
    funciones.SubOpciones(5, matriz, lst_codigos, tpl_meses)

def determinar_estado(humedad):
    if humedad <= 29:
        return "Crítico"
    elif humedad <= 50:
        return "Bajo"
    elif humedad <= 80:
        return "Adecuado"
    else:
        return "Excesivo"

def pedir_mes_valido(tpl_meses):
    mes = int(input("Ingrese el número de mes (1-12): "))
    while mes < 1 or mes > 12:
        print("Mes inválido. Debe ser entre 1 y 12.")
        mes = int(input("Ingrese el número de mes (1-12): "))

    indice_mes = mes - 1
    nombre_mes = tpl_meses[indice_mes][1]
    
    return indice_mes, nombre_mes


def informe_general_campo(matriz,lst_codigos,tpl_meses):
    sectores_registrados = len(lst_codigos) #cantidad de sectores registrados

    cantidad_mediciones = 0
    suma_humedad = 0
    for fila in matriz:
        for valor in fila:
            if valor != -1: #recorremos la matriz y cualquier valor que sea distinto a -1 sumamos en el contador para obtener cuantas mediciones validas hay
                cantidad_mediciones += 1
                suma_humedad += valor #sumamos los valores para sacar promedio

    if cantidad_mediciones > 0:
        promedio_general = suma_humedad/cantidad_mediciones
    else:
        promedio_general = 0

    maxHumedad = -1
    indice_sector_max = -1
    indice_mes_max = -1

    minHumedad = 101
    indice_sector_min = -1
    indice_mes_min = -1

    for f in range(len(matriz)): 
        for c in range(len(matriz[f])):
            if matriz[f][c] != -1: 

                if matriz[f][c] > maxHumedad:
                    maxHumedad = matriz[f][c]
                    indice_mes_max = c
                    indice_sector_max = f

                if matriz[f][c] < minHumedad:
                    minHumedad = matriz[f][c]
                    indice_mes_min = c
                    indice_sector_min = f


    nombre_sector_max = lst_codigos[indice_sector_max] 
    nombre_mes_max = tpl_meses[indice_mes_max][1]
    nombre_sector_min = lst_codigos[indice_sector_min]
    nombre_mes_min = tpl_meses[indice_mes_min][1]


    # 2. Impresión con la estética del menú
    print('\n╔══════════════════════════════════════╗')
    print('║      📊 INFORME GENERAL DEL CAMPO    ║')
    print('╠══════════════════════════════════════╣')
    print(f'║ Sectores registrados: {sectores_registrados:<14} ║')
    print(f'║ Mediciones cargadas: {cantidad_mediciones:<15} ║')
    print(f'║ Promedio general: {promedio_general:<14.2f}     ║')
    print('╠══════════════════════════════════════╣')
    print('║ 🔴 MAYOR MEDICIÓN                    ║')
    print(f'║ Humedad: {maxHumedad:<4} %                      ║')
    print(f'║ Sector: {nombre_sector_max:<28} ║')
    print(f'║ Mes: {nombre_mes_max:<31} ║')
    print('╠══════════════════════════════════════╣')
    print('║ 🔵 MENOR MEDICIÓN                    ║')
    print(f'║ Humedad: {minHumedad:<2}%                         ║')
    print(f'║ Sector: {nombre_sector_min:<28} ║')
    print(f'║ Mes: {nombre_mes_min:<31} ║')
    print('╚══════════════════════════════════════╝')





def informe_sector(matriz,lst_codigos,tpl_meses):
    sector = input("Ingrese el sector:").upper()
    while sector not in lst_codigos:
        print ("Error, el sector no esta registrado")
        sector = input ("Ingrese el sector").upper()

    indice_sector = lst_codigos.index(sector)
    fila_sector = matriz[indice_sector]

    mediciones = [c for c in fila_sector if c != -1]
    cantidad = len(mediciones)
    if cantidad == 0:
        promedio = 0
    else:
        promedio = sum(mediciones) / cantidad

    lineas_meses = []
    for c in range(len(fila_sector)):
        humedad = fila_sector[c]
        if humedad != -1:  # Si hay medición en este mes
            nombre_mes = tpl_meses[c][1]   
            estado =determinar_estado(humedad)
            lineas_meses.append(f"{nombre_mes}: {humedad}% ({estado})")

    print('\n╔══════════════════════════════════════╗')
    print('║         📄 INFORME DE SECTOR         ║')
    print('╠══════════════════════════════════════╣')
    print(f'║ Sector: {sector:<28} ║')
    print(f'║ Mediciones cargadas: {cantidad:<15} ║')
    print(f'║ Promedio: {promedio:<5} %                    ║')
    print('╠══════════════════════════════════════╣')
    print('║ 💧 MEDICIONES POR MES:               ║')

    if len(lineas_meses) == 0:
        print('║ Sin mediciones registradas           ║')
    else:
        for linea in lineas_meses:
            print(f'║  • {linea:<33} ║')

    print('╚══════════════════════════════════════╝')

    


def informe_mensual(matriz,lst_codigos,tpl_meses):
    indice_mes, nombre_mes = pedir_mes_valido(tpl_meses)

    mediciones_mes = []
    lineas_sectores = []

    for f in range(len(matriz)):
        humedad = matriz[f][indice_mes]
        if humedad != -1:
            mediciones_mes.append(humedad)
            id_sector = lst_codigos[f]
            estado = determinar_estado(humedad)  
            lineas_sectores.append(f"{id_sector}: {humedad}% ({estado})")
    
    if len(mediciones_mes) > 0:
        promedio_mes = sum(mediciones_mes) / len(mediciones_mes)
    else:
        promedio_mes = 0

    print('\n╔══════════════════════════════════════╗')
    print('║          📅 INFORME MENSUAL          ║')
    print('╠══════════════════════════════════════╣')
    print(f'║ Mes: {nombre_mes:<31} ║')
    print(f'║ Mediciones registradas: {len(mediciones_mes):<12} ║')
    print(f'║ Promedio del mes: {promedio_mes:<3} %              ║')
    print('╠══════════════════════════════════════╣')
    print('║ 🌾 ESTADO POR SECTOR:                ║')

    if len(lineas_sectores) == 0:
        print('║ Sin mediciones para este mes         ║')
    else:
        for linea in lineas_sectores:
            print(f'║  • {linea:<33} ║')

    print('╚══════════════════════════════════════╝')



def sectores_atencion(matriz,lst_codigos,tpl_meses):
    indice_mes, nombre_mes = pedir_mes_valido(tpl_meses)

    sectores_criticos = [
        (lst_codigos[f],matriz[f][indice_mes])
        for f in range(len(matriz))
        if matriz[f][indice_mes] !=-1 and matriz[f][indice_mes] <= 50
    ]

    print('\n╔══════════════════════════════════════╗')
    print('║      ⚠️ SECTORES EN ATENCIÓN          ║')
    print('╠══════════════════════════════════════╣')
    print(f'║ Mes: {nombre_mes:<31} ║')
    print('╠══════════════════════════════════════╣')

    if len(sectores_criticos) == 0:
        print('║ Ningún sector requiere atención      ║')
        print('║ en este mes.                         ║')
    else:
        for id_sector, humedad in sectores_criticos:
            estado = determinar_estado(humedad)
            linea = f"{id_sector}: {humedad}% ({estado})"
            print(f'║  • {linea:<33} ║')

    print('╚══════════════════════════════════════╝')

def ranking_mensual_humedad(matriz,lst_codigos,tpl_meses):
    indice_mes, nombre_mes = pedir_mes_valido(tpl_meses)
    
    datos_ranking = []
    for f in range (len(matriz)):
        humedad = matriz[f][indice_mes]
        if humedad != -1:
            datos_ranking.append((lst_codigos[f], humedad))

    datos_ranking.sort(key=lambda x: x[1]) #lo que hace esta funcion lambda es agarrar cada tupla (a la que llamamos x), mirá solamente el dato que está en la posición 1 (la humedad), y usá ese número para decidir el orden".
    

    print('\n╔══════════════════════════════════════╗')
    print('║      🏆 RANKING DE HUMEDAD           ║')
    print('╠══════════════════════════════════════╣')
    print(f'║ Mes: {nombre_mes:<31} ║')
    print('╠══════════════════════════════════════╣')

    # Verificamos si la lista quedó vacía (por si eligieron un mes sin datos)
    if len(datos_ranking) == 0:
        print('║ Sin mediciones registradas           ║')
    else:
        # Usamos un contador para mostrar el puesto en el ranking
        puesto = 1
        for id_sector, humedad in datos_ranking:
            # Reutilizamos tu función mágica para el estado
            estado = determinar_estado(humedad)
            
            # Armamos el texto y lo imprimimos con el formato del cuadro
            linea = f"{id_sector}: {humedad}% ({estado})"
            print(f'║ {puesto:2}. {linea:<32} ║')
            
            puesto += 1

    print('╚══════════════════════════════════════╝')

    


