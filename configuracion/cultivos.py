def AbrirArchivoRangos():
    arch=open('rango_cultivos.csv', mode='rt')
    return arch


def cerrarArchivoRangos(arch):
    arch.close()

def abrirArchivoLstCultivos():
    arch=open('lista_cultivos.csv', mode='wt')
    return arch

def cerrarArchivoLstCultivos(arch):
    arch.close()