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


def hay_guardado_pendiente():
    """No permite usar los archivos si quedó un guardado sin completar."""
    try:
        with open("Documentacion/guardado_pendiente.txt", "rt", encoding="utf-8") as archivo:
            pendiente = archivo.readline().strip()
    except FileNotFoundError:
        return False
    except OSError as error:
        print("No se pudo comprobar el estado del último guardado:", error)
        return True
    return pendiente != ""


def registrar_guardado_pendiente(pendiente):
    """Escribe el indicador antes del guardado y lo vacía al terminar."""
    try:
        with open("Documentacion/guardado_pendiente.txt", "wt", encoding="utf-8") as archivo:
            if pendiente:
                archivo.write("pendiente\n")
            else:
                archivo.write("")
    except OSError as error:
        print("No se pudo actualizar el estado del guardado:", error)
        return False
    return True


def extraccionMatriz(rangos=None):
    """Lee filas correspondientes de ambos CSV y devuelve matriz, códigos y cultivos."""
    if hay_guardado_pendiente():
        print("Inicio cancelado: hay un guardado anterior pendiente de recuperación.")
        print("Revise mediciones_respaldo.csv y lista_cultivos_respaldo.csv antes de usar los datos.")
        return None, None, None
    if rangos is None:
        rangos = pasar_a_dic_cultivos()
    if rangos is None:
        return None, None, None
    matriz = []
    lst_codigos = []
    lst_cultivos = []
    try:
        with open("Documentacion/mediciones.csv", "rt", encoding="utf-8") as file:
            try:
                with open("Documentacion/lista_cultivos.csv", "rt", encoding="utf-8") as arch:
                    line = file.readline()
                    linea = arch.readline()
                    numero_fila = 0
                    while line or linea:
                        numero_fila += 1
                        codigo = linea.strip().upper()
                        cultivo = obtener_cultivo(codigo, rangos)
                        valores = line.strip().split(",")
                        error = ""
                        if not line or not linea:
                            error = "falta la fila correspondiente en uno de los dos archivos"
                        elif not re.match(r"^[0-9]{3}-[A-Z]{3}$", codigo):
                            error = "el código debe tener el formato 123-PAP"
                        elif codigo in lst_codigos:
                            error = "el sector está repetido"
                        elif cultivo == "":
                            error = "las letras del código no corresponden a un cultivo definido"
                        elif len(valores) != 12:
                            error = "debe haber 12 humedades"
                        elif len(lst_codigos) == 50:
                            error = "se alcanzó el máximo de 50 sectores"
                        else:
                            try:
                                lst_humedades = [int(valor) for valor in valores]
                            except ValueError:
                                error = "las humedades deben ser números enteros"
                            else:
                                for humedad in lst_humedades:
                                    if humedad < -1 or humedad > 100:
                                        error = "las humedades deben ser -1 o estar entre 0 y 100"
                        if error != "":
                            print(f"Fila {numero_fila} ignorada: {error}.")
                        else:
                            lst_codigos.append(codigo)
                            lst_cultivos.append(cultivo)
                            matriz.append(lst_humedades)
                        # Avanzan juntos, incluso cuando la fila es inválida.
                        line = file.readline()
                        linea = arch.readline()
            except FileNotFoundError:
                print("Inicio cancelado: existe mediciones.csv, pero falta lista_cultivos.csv.")
                print("No se pueden asociar las mediciones a sus sectores. Recupere el archivo de códigos.")
                return None, None, None
            except OSError as error:
                print("No se pudieron leer los datos de los sectores:", error)
                return None, None, None
    except FileNotFoundError:
        print("No existe mediciones.csv. El sistema inicia sin sectores.")
    except OSError as error:
        print("No se pudieron leer las mediciones:", error)
        return None, None, None
    return matriz, lst_codigos, lst_cultivos


def copiar_archivo(origen, destino, permitir_faltante=False):
    """Copia texto con las operaciones de archivo vistas en clase."""
    contenido = ""
    try:
        with open(origen, "rt", encoding="utf-8") as archivo:
            for linea in archivo:
                contenido += linea
    except FileNotFoundError:
        if not permitir_faltante:
            print("No se encontró el archivo que se debía copiar:", origen)
            return False
    except OSError as error:
        print("No se pudo leer el archivo para copiarlo:", error)
        return False
    try:
        with open(destino, "wt", encoding="utf-8") as archivo:
            archivo.write(contenido)
    except OSError as error:
        print("No se pudo completar la copia del archivo:", error)
        return False
    return True


def guardarMediciones(matriz, lst_codigos):
    """Respalda ambos archivos y guarda códigos y humedades en el mismo orden."""
    if len(matriz) != len(lst_codigos):
        print("No se guardaron los datos: la cantidad de sectores y filas no coincide.")
        return False
    respaldo_mediciones = "Documentacion/mediciones_respaldo.csv"
    respaldo_codigos = "Documentacion/lista_cultivos_respaldo.csv"
    if hay_guardado_pendiente():
        print("No se guardaron los cambios: hay un guardado anterior pendiente de recuperación.")
        print("Los respaldos se conservaron:", respaldo_mediciones, respaldo_codigos)
        return False

    if not copiar_archivo("Documentacion/mediciones.csv", respaldo_mediciones, True):
        print("No se guardaron los cambios. No se modificaron los archivos originales.")
        return False
    if not copiar_archivo("Documentacion/lista_cultivos.csv", respaldo_codigos, True):
        print("No se guardaron los cambios. No se modificaron los archivos originales.")
        return False

    # El indicador protege los respaldos si el programa se interrumpe o falla la restauración.
    if not registrar_guardado_pendiente(True):
        print("No se guardaron los cambios. No se modificaron los archivos originales.")
        return False

    try:
        with open("Documentacion/mediciones.csv", "wt", encoding="utf-8") as file:
            with open("Documentacion/lista_cultivos.csv", "wt", encoding="utf-8") as arch:
                for i in range(len(lst_codigos)):
                    linea = ""
                    for j in range(len(matriz[i])):
                        if j > 0:
                            linea += ","
                        linea += str(matriz[i][j])
                    file.write(linea + "\n")
                    arch.write(lst_codigos[i] + "\n")
    except OSError as error:
        print("No se pudieron guardar los datos:", error)
        restaurado_mediciones = copiar_archivo(respaldo_mediciones, "Documentacion/mediciones.csv")
        restaurado_codigos = copiar_archivo(respaldo_codigos, "Documentacion/lista_cultivos.csv")
        if restaurado_mediciones and restaurado_codigos:
            print("Se restauraron los datos anteriores.")
            registrar_guardado_pendiente(False)
        else:
            print("No se pudo completar la restauración. Conserve estos respaldos:")
        print(respaldo_mediciones)
        print(respaldo_codigos)
        return False
    if not registrar_guardado_pendiente(False):
        print("Los datos se escribieron, pero no se pudo confirmar el cierre del guardado.")
        print("Se conservaron los respaldos. Revise los archivos antes de volver a guardar.")
        return False
    print("Sectores y mediciones guardados correctamente.")
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

