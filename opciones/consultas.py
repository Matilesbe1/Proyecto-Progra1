import funciones
import opciones.informes
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

    resultado = [c[mes] for c in matriz if len(c) > mes and c[mes] != -1]
    print("\n" + "=" * 90)
    if resultado:
        print(f"Las mediciones del mes numero {mes+1} son de:", end="")
        for i in resultado:
            print(i, end="|")
        print()
    else:
        print("\n" + "=" * 90)
        print('No hay mediciones registradas.')
        print( "=" * 90)

def consultar_estado_humedad(sectores, matriz, rangos):
    sector = input("Ingrese el ID del sector a consultar: ").upper()
    while sector not in sectores:
        print("El sector ingresado no esta dentro de los sectores")
        sector = input("Ingrese el ID del sector a consultar: ").upper()
    indice = sectores.index(sector)

    mes = 0
    while mes < 1 or mes > 12:
        try:
            mes = int(input("Ingrese el numero de mes: "))
            if mes < 1 or mes > 12:
                print("Indique un mes valido")
        except ValueError:
            print("Debe ingresar un numero")
    mes -= 1

    if len(matriz[indice]) <= mes or matriz[indice][mes] == -1:
        print("\n" + "=" * 28)
        print("No hay medicion registrada")
        print("=" * 28)
        return None

    valor = matriz[indice][mes]
    estado = opciones.informes.determinar_estado(valor, sector, rangos)
    print("\n" + "=" * 30)
    if estado:
        print(f"Humedad: {valor}%")
        print(f"ESTADO: {estado.upper()}")
    else:
        print("No se encontró un rango para este sector/valor")
    print("=" * 30)
