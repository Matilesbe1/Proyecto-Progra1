import funciones
def llamarFunciones(num, matriz, lst_codigos,tpl_meses):
    if num==1:
        alta_sector(lst_codigos,matriz,tpl_meses)
    elif num==2:
        busca_id(matriz,lst_codigos,tpl_meses)
    elif num==3:
        mostrar_matriz(matriz,lst_codigos,tpl_meses)

def valida_codigo(codigo):
    '''Recibe el codigo ingresado por el usuario.
    Valida que cumpla con el formato establecido y retorna un booleano dependiendo de si es válido o no.'''
    if len(codigo) != 7:
        print("Ha ingresado un código inválido.")
        return False
    elif not codigo[:2].isdigit():
        print("Error. El prefijo debe contener 3 números.")
        return False
    elif codigo[3] != "-":
        print("Error. El código debe estar separado unicamente por un guión (-).")
        return False
    elif not codigo[4:].isalpha():
        print("Error. El sufijo debe contener 3 letras.")
        return False
    else:
        return True


def alta_sector(lst_codigos,matriz,tpl_meses):
    '''Recibe por parametro la lista de codigos y la matriz.
        Se pide al usuario que ingrese el codigo, se valida llamando a la funcion valida_codigo() y en caso correcto, se da por alta en la matriz y en la lista.En caso invalido, se pide que se vuelva a ingresar.
        Las condiciones de corte son: que se ingrese -1 o qeu se llegue al limite de 50 sectores.'''
    
    print("IMPORTANTE: EL código debe estar compuesto por: tres números, un guión (-) y tres letras.")
    print("Por ejemplo: 123-ABC")
    codigo = input("Ingrese el codigo (-1 finaliza): ").upper()
    cant = 0
    while codigo != "-1" and cant <= 50:
        if valida_codigo(codigo) and codigo not in lst_codigos:
            print(f"✓ El sector se ha dado de alta con el codigo {codigo}.")
            lst_codigos.append(codigo.upper())
            matriz.append([-1 for humedad in range(12)])

            print("\nPresione ENTER para continuar...")
            input() # Esto hace una pausa para que el usuario pueda leer el resultado antes de limpiar la pantalla
        else:
            print("✕ El código ingresado es inválido o está repetido. Vuelva a intentarlo.")
        codigo = input("Ingrese el codigo (-1 finaliza): ").upper()
    funciones.SubOpciones(1, matriz, lst_codigos,tpl_meses)
    return None


def busca_id(matriz,lst_codigos,tpl_meses):
    '''Recibe la lista de codigos.
    Pide al usuario que ingrese un ID a buscar. 
    Informa al usuario si el ID buscado se encuentra registrado. Permite realizar más de una búsqueda.
    Retorna None'''
    print("Recuerde que los IDs tienen el siguiente formato: 123-ABC")
    opcion = 0
    while opcion == 0:
        id_buscado = input("Ingrese el ID del sector que quiere buscar: ").upper()
        if id_buscado in lst_codigos:
            print(f"✓ El sector con ID {id_buscado} se encuentra registrado en el sistema.")

            print("\nPresione ENTER para continuar...")
            input() # Esto hace una pausa para que el usuario pueda leer el resultado antes de limpiar la pantalla
        else:
            print(f"✕ No se econtró ningún sector con el ID: {id_buscado}")
        print("Desea realizar una nueva busqueda?: ")
        opcion = int(input("Ingrese 0 para SI y 1 para NO: "))
        while opcion != 0 and opcion != 1:
            print("Opción inválida. Vuelva a intentar")
            opcion = int(input("Ingrese 0 para SI y 1 para NO: "))
    funciones.SubOpciones(1, matriz, lst_codigos,tpl_meses)
    return None

def mostrar_matriz(matriz,sectores,meses):
    '''Recibe como parametros la matriz, la lista de codigos y la tupla de meses.
    Muestra la matriz junto con los sectores y los meses, todo con formato y representado de forma mas visual.
    Retorna None.'''
    print(f"{"-"*22} PORCENTAJES DE HÚMEDAD SECTOR/MES {"-"*22}")
    print(" "*7,end= " ")
    for numero,mes in meses:
        print("%5s"%mes,end=" ")
    print()
    for f in range(len(matriz)):
        print(sectores[f], end=" ")
        for c in range(len(matriz[0])):
            print("%5d" %matriz[f][c],end=" ")
        print()
    print("-"*80)

    print("\nPresione ENTER para continuar...")
    input() # Esto hace una pausa para que el usuario pueda leer el resultado antes de limpiar la pantalla

    funciones.SubOpciones(1, matriz, sectores,meses)
    return None



        
        
