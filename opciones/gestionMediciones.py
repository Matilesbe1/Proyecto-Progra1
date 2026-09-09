def elige_opcion():
    op = int(input("Ingrese 0 para SI y 1 para NO: "))
    while op != 0 and op != 1:
        print("Ingreso inválido. Solo puede ingresar 0 para SI o 1 para NO.")
        op = int(input("Intente nuevamente: "))
    if op == 0:
        return True
    else:
        return False

def valida_id_y_mes(lst_codigos,tpl_meses,mes,id_sector):
    '''Recibe tanto el mes como el sector que ingreso el usuario como la lista y tupla correspondientes a donde estas se alojan.
    La función valida que el ID y mes introducidos se encuentran efectivamente cargados.
    De ser así retorna True, por el contrario, retorna False si no es así.'''
    if id_sector in lst_codigos and mes in tpl_meses:
        return True
    else:
        return False

def pide_datos():
    '''No recibe parámetros.
    Pide al usuario que ingrese el ID y el mes a acceder.
    Retorna estos dos valores.'''
    print("Recuerde el formato de los IDs: 123-ABC.")
    id_sector = input("Ingrese el ID del sector al que quiere acceder: ").upper()
    print("Ahora, ingresará el mes a actualizar.\nEstos van de 1 a 12, siendo 1 --> Enero y 12 --> Febrero")
    mes = int(input("Ingrese el mes (1-12): "))
    return id_sector,mes

def pide_humedad():
    '''No recibe parámetros. 
    Pide al usuario que ingrese la humedad a registrar y valida que este entre 0 y 100.
    Retorna la humedad introducida.'''
    valor = int(input("Ingrese el porcentaje de humedad que quiere agregar (0-100%): "))
    while valor < 0 or valor > 100:
        print("Error. La humedad debe estar entre 0 y 100%")
        valor = int(input("Intene nuevamente: "))
    return valor

def indice_sector_mes(lst_codigos,tpl_meses,mes,id_sector):
    '''Recibe como parámetros ls lista de los códigos, la tupla de meses y el mes e ID ingresado por el usuario.
    La función captura el indice del ID y mes en sus respectivas listas y las retorna empaquetadas.'''
    i_mes = tpl_meses.index(mes)
    i_id = lst_codigos.index(id_sector)
    return i_mes,i_id

def cargar_medicion(matriz,lst_codigos,tpl_meses):
    '''Recibe la matriz, la lista de codigos y la tupla de los meses.
    Se llama a la funcion pide_datos(), con estos llama a valida_id_y_mes() y de ser True, llama a pide_humedad() y luego a indice_sector_mes(). Con esto accede al lugar en la matriz y registra la humedad anteriormente introducida.'''
    id_sector,mes = pide_datos()
    opcion = True
    while opcion:
        if valida_id_y_mes(lst_codigos,tpl_meses,mes,id_sector):
            humedad = pide_humedad()
            i_mes,i_id = indice_sector_mes(lst_codigos,tpl_meses,mes,id_sector)
            matriz[i_id][i_mes] = humedad
            print(f"Se ha actulizado el valor del sector {id_sector} en el mes {mes} a: {humedad}")
        else:
            print("Ha ingresado un sector o mes inválido.")
            print("Recuerde que el formato del sector es 123-ABC y los meses van de 1 a 12.")
        print("-"*10)
        print("Desea acceder a otro sector y mes?")
        print("-"*10)
        opcion = elige_opcion()
        if opcion:
            id_sector,mes = pide_datos()
        else:
            print("Volverás al menú principal.")
    return None
        

        

