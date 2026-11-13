import re

def aperturaArchivo(archivo, modo):
    try:
        arch=open(archivo, mode=modo)
    except OSError as error:
        print("Error al abrir el archivo:", error)
    except FileNotFoundError:
        print("El archivo no existe")
    else:
        return arch

def obtener_cultivo(codigo, rangos):
    """Obtiene el cultivo usando las tres letras del código del sector."""
    cultivo = ""
    for nombre in rangos:
        if codigo[4:7].upper() == nombre[:3].upper():
            cultivo = nombre
    return cultivo

def extracciones():
    lst_codigos = []
    arch_codigos = aperturaArchivo('./Documentacion/lista_cultivos.csv', 'rt')
    for linea in arch_codigos:
        lst_codigos.append(linea.strip())
    lst_matriz = []
    arch_matriz = aperturaArchivo('./Documentacion/mediciones.csv', 'rt')
    for linea in arch_matriz:
        fila = linea.strip().replace('[', '').replace(']', '').replace(',', ' ')
        fila = fila.split()
        fila = [int(valor) for valor in fila]
        lst_matriz.append(fila)
    arch_codigos.close()
    arch_matriz.close()
    return lst_matriz, lst_codigos


def guardarMediciones(matriz, lst_codigos):
    arch_matriz = aperturaArchivo('./Documentacion/mediciones.csv', 'wt')
    for fila in matriz:
        for valor in fila:
            arch_matriz.write(str(valor)+ ',' )
        arch_matriz.write('\n')
    arch_matriz.close()
    arch_codigos = aperturaArchivo('./Documentacion/lista_cultivos.csv', 'wt')
    for codigo in lst_codigos:
        arch_codigos.write(str(codigo) + '\n')
    arch_codigos.close()
    return True


def pasar_a_dic_cultivos():
    diccionario = {}
    try:
        archivo = aperturaArchivo("./Documentacion/rango_cultivos.csv", "rt")
    except OSError:
        print("Error al abrir el archivo")
    else:
        if archivo is None:
            return None
        archivo.readline()
        for linea in archivo:
            cultivo, nivel, minimo, maximo = linea.strip().split(",")
            if cultivo not in diccionario:
                diccionario[cultivo] = {}
            diccionario[cultivo][nivel] = [int(minimo), int(maximo)]
        archivo.close()
        return diccionario

def extrer_tpl_meses():
    '''No recibe parametros.
    Lee y extrae los datos necesarios para traer a memoria la lista de tuplas de los meses.
    Retorna una lista de tuplas'''
    tpl_meses = []
    file = aperturaArchivo("./Documentacion/meses.csv","rt")

    if file == None:
        return None

    line = file.readline()
    while line:
        nro,mes = line.strip().split(";")
        tpl_meses.append((nro,mes))
        line = file.readline()
    file.close()
    return tpl_meses

