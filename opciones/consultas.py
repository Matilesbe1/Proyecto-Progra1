import funciones
def llamarfunciones(lst_codigos, matriz, num, tpl_meses, dicc):
    if num == 1:
        consultar_sector(lst_codigos, matriz)
    elif num == 2:
        consultar_mediciones_mes(matriz)
    elif num == 3:
        consultar_estado_humedad(lst_codigos, matriz, dicc)

    input("\nPresione ENTER para continuar...")
    funciones.SubOpciones(3, matriz, lst_codigos, tpl_meses, dicc)
    
def consultar_sector(sectores, matriz):
    sector = input("Ingrese el ID del sector a consultar: ").upper()
    while sector not in sectores:
        print("El sector ingresado no esta dentro de los sectores")
        sector = input("Ingrese el ID del sector a consultar: ").upper()

    indice = sectores.index(sector)
    resultado = [c for c in matriz[indice]]
    print("\n" + "=" * 90)
    print("El sector", sector, "tiene las siguientes mediciones:", end="")
    for i in resultado:
        print(i, end="|")
    print("\n" + "=" * 90)

def consultar_mediciones_mes(matriz):
    mes = int(input("Ingrese el numero de mes: "))
    while mes < 1 or mes > 12:
        print("Indique un mes valido")
        mes = int(input("Ingrese el numero de mes: "))
    mes -= 1

    resultado = [c[mes] for c in matriz if len(c) > mes]
    print("\n" + "=" * 90)
    print(f"Las mediciones del mes numero {mes+1} son de:", end="")
    for i in resultado:
        print(i, end="|")
    print("\n" + "=" * 90)

    if mediciones==True:
        print("\n" + "=" * 90)
        print(f"Las mediciones del mes numero {mes+1} son de: ", end="")
        for i in resultado:
            print(i, end="|")
        print("\n" + "=" * 90)
    else:
        print("\n" + "=" * 90)
        print('No hay mediciones registradas.')
        print( "=" * 90)

def consultar_estado_humedad(sectores, matriz, rangos):
    sector = input("Ingrese el ID del sector a consultar: ").upper()
    med_rangos=[]
    while sector not in sectores:
        print("El sector ingresado no esta dentro de los sectores")
        sector = input("Ingrese el ID del sector a consultar: ").upper()
    for rango in rangos:
        if sector[4:7].upper()==rango[0:3].upper():
            med_rangos.append(rango)
        else:
            continue
    indice=matriz.index(sector)

    mes = int(input("Ingrese el numero de mes: "))
    while mes < 1 or mes > 12:
        print("Indique un mes valido")
        mes = int(input("Ingrese el numero de mes: "))
    mes -= 1

    valor = matriz[indice][mes]
    if valor == -1:
        print("\n" + "=" * 28)
        print("No hay medicion registrada")
        print("=" * 28)
        return None
    else:
        for med_rango in med_rangos:
            nombre, estado, minimo, maximo= med_rango.split(',')
            if valor>=minimo and valor<=maximo:
                return estado
        
    print("=" * 30)
    print(f"ESTADO: {estado.upper()}")
    print("=" * 30)

