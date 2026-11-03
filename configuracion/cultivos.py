def abrirArchivoRangos():
    try:
        arch=open('Documentacion/rango_cultivos.csv', mode='rt')
    except OSError as error:
        print("Error al abrir el archivo:", error)
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        return arch

def cerrarArchivoRangos(arch):
    try:
        arch.close()
    except OSError:
        print("Error al cerrar el archivo")

def abrirArchivoLstCultivos():
    try:
        arch=open('Documentacion/lista_cultivos.csv', mode='rt')
    except OSError as error:
        print("Error al abrir el archivo:", error)
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        return arch

def cerrarArchivoLstCultivos(arch):
    try:
        arch.close()
    except OSError:
        print("Error al cerrar el archivo")

def aperturaArchivo(archivo, modo):
    try:
        arch=open(archivo, mode=modo)
    except OSError as error:
        print("Error al abrir el archivo:", error)
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        return arch

def extraccionMatriz():
    '''No recibe parámetros.
    Lee y extrae los datos necesarios para traer a memoria la matriz de mediciones y la lista de códigos.
    Retorna una tupla con (matriz,lst_codigos)'''
    matriz = []
    lst_codigos = []
    file = aperturaArchivo("./Documentacion/mediciones.csv","rt")

    if file is None: # chequea que no haya habido un error en la apertura del archivo
        return None,None
    
    line = file.readline()
    while line:
        codigo,humedades = line.strip().split(";")
        # como humedades es un string, creo una lista de enteros
        lst_humedades = [int(i) for i in humedades.split(",")] 

        lst_codigos.append(codigo)
        matriz.append(lst_humedades)

        line = file.readline()
    file.close()
    return matriz,lst_codigos
def pasar_a_dic_cultivos():
    diccionario = {}
    try:
        archivo = open("Documentacion/rango_cultivos.csv", mode="rt", encoding="utf-8")
    except OSError:
        print("Error al abrir el archivo")
    else:
        archivo.readline()
        for linea in archivo:
            cultivo, nivel, minimo, maximo = linea.strip().split(",")
            if cultivo not in diccionario:
                diccionario[cultivo] = {}
            diccionario[cultivo][nivel] = [int(minimo), int(maximo)]
        archivo.close()
        return diccionario
