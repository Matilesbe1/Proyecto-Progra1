import funciones
def llamarfunciones(lst_codigos, matriz, num, tpl_meses):
    if num == 1:
        consultar_sector(lst_codigos, matriz)
    elif num == 2:
        consultar_mediciones_mes(matriz)
    elif num == 3:
        consultar_estado_humedad(lst_codigos, matriz)

    print("\nPresione ENTER para continuar...")
    input() # Esto hace una pausa para que el usuario pueda leer el resultado antes de limpiar la pantalla
    funciones.SubOpciones(3,matriz, lst_codigos, tpl_meses)
    
def consultar_sector(sectores, matriz):
    sector = input("Ingrese el ID del sector a consultar: ").upper()
    while sector not in sectores:
        print("El sector ingresado no esta dentro de los sectores")
        sector = input("Ingrese el ID del sector a consultar: ").upper()

    indice = sectores.index(sector)
    resultado = [c for c in matriz[indice]]
    print(f"El sector {sector} tiene las siguientes mediciones: {resultado}")

def consultar_mediciones_mes(matriz):
    mes = int(input("Ingrese el numero de mes: "))
    while mes < 1 or mes > 12:
        print("Indique un mes valido")
        mes = int(input("Ingrese el numero de mes: "))
    mes -= 1

    resultado = [c[mes] for c in matriz if len(c) > mes]
    print(f"Las mediciones del mes numero {mes+1} son de: {resultado}")

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
        print("No hay medicion registrada")
        return None

    if valor <= 29:
        print("El estado es Critico")
    elif valor <= 50:
        print("El estado es Bajo")
    elif valor <= 80:
        print("El estado es adecuado")
    else:
        print("El estado es Excesivo")



