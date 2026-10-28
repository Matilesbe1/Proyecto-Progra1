def AbrirArchivoRangos():
    arch=open('Documentacion/rango_cultivos.csv', mode='rt')
    return arch


def cerrarArchivoRangos(arch):
    arch.close()

def abrirArchivoLstCultivos():
    arch=open('Documentacion/lista_cultivos.csv', mode='at')
    return arch

def abrirArchivoLstCultivosR():
    arch=open('Documentacion/lista_cultivos.csv', mode='rt')
    return arch

def cerrarArchivoLstCultivos(arch):
    arch.close()