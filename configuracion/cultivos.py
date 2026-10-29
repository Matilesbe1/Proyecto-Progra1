def AbrirArchivoRangos():
    try:
        arch=open('Documentacion/rango_cultivos.csv', mode='wt')
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
        arch=open('Documentacion/lista_cultivos.csv', mode='wt')
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