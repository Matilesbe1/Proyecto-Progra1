import funciones
def llamarfunciones(lst_codigos, matriz, num, tpl_meses):
    if num == 1:
        consultar_sector(lst_codigos, matriz)
    elif num == 2:
        consultar_mediciones_mes(matriz)
    elif num == 3:
        consultar_estado_humedad(lst_codigos, matriz)

    print("\nPresione 0 para continuar, 1 para finalizar...")
    numero = int(input())
    while numero > 1 or numero < 0:
        print("Indique el numero correctamente")
        numero = int(input("Vuelva a ingresar el numero: "))
    if numero == 0:
        funciones.SubOpciones(3,matriz, lst_codigos, tpl_meses)        
        return True
    else:
        print("finalizando el programa...")
        return False
    
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

def consultar_estado_humedad(sectores, matriz):
    sector = input("Ingrese el ID del sector a consultar: ").upper()
    while sector not in sectores:
        print("El sector ingresado no esta dentro de los sectores")
        sector = input("Ingrese el ID del sector a consultar: ").upper()
    indice = sectores.index(sector)

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

    if valor <= 29:
        estado = "CRÍTICO"
    elif valor <= 50:
        estado = "BAJO"
    elif valor <= 80:
        estado = "ADECUADO"
    else:
        estado = "EXCESIVO"
    
    print("=" * 30)
    print(f"ESTADO: {estado}")
    print("=" * 30)

