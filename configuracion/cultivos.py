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