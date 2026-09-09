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


def alta_sector(lst_codigos,matriz):
    '''Recibe por parametro la lista de codigos y la matriz.
        Se pide al usuario que ingrese el codigo, se valida llamando a la funcion valida_codigo() y en caso correcto, se da por alta en la matriz y en la lista.En caso invalido, se pide que se vuelva a ingresar.
        Las condiciones de corte son: que se ingrese -1 o qeu se llegue al limite de 50 sectores.'''
    
    print("IMPORTANTE: EL código debe estar compuesto por: tres números, un guión (-) y tres letras.")
    print("Por ejemplo: 123-ABC")
    codigo = input("Ingrese el codigo (-1 finaliza): ").upper()
    cant = 0
    while codigo != "-1" and cant <= 50:
        if valida_codigo(codigo):
            print(f"El sector {cant+1} se ha dado de alta con el codigo {codigo}.")
            cant += 1
            lst_codigos.append(codigo.upper())
            matriz.append([-1 for humedad in range(12)])
        else:
            print("El código ingresado es inválido. Vuelva a intentarlo.")
        codigo = input("Ingrese el codigo (-1 finaliza): ").upper()

    return None


def busca_id(lst_codigos):
    '''Recibe la lista de codigos.
    Pide al usuario que ingrese un ID a buscar. 
    Informa al usuario si el ID buscado se encuentra registrado. Permite realizar más de una búsqueda.
    Retorna None'''
    print("Recuerde que los IDs tienen el siguiente formato: 123-ABC")
    opcion = 0
    while opcion == 0:
        id_buscado = input("Ingrese el ID del sector que quiere buscar: ").upper()
        if id_buscado in lst_codigos:
            print(f"El sector con ID {id_buscado} se encuentra registrado en el sistema.")
        else:
            print(f"No se econtró ningún sector con el ID: {id_buscado}")
        print("Desea realizar una nueva busqueda?: ")
        opcion = int(input("Ingrese 0 para SI y 1 para NO: "))
        while opcion != 0 and opcion != 1:
            print("Opción inválida. Vuelva a intentar")
            opcion = int(input("Ingrese 0 para SI y 1 para NO: "))
    return None


        
        
