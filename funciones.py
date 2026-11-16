import configuracion.cultivos
import opciones.informes
import opciones.analisisHumedad
import opciones.consultas
import opciones.gestionMediciones
import opciones.gestionSectores

def pide_opcion(minimo,maximo):
    while True:
        try:
            op = int(input(f"Ingrese una opción (entre {minimo}-{maximo}): "))
            if op > maximo or op < minimo:
                print(f"ERROR. Ingrese una opción entre {minimo}-{maximo}.")
            else:
                return op
        except ValueError:
            print("ERROR. Ha ingresado un valor inválido. Intente nuevamente.")


def menuPrincipal(matriz, lst_codigos,tpl_meses, dicc):

    print('\n╔══════════════════════════════════════╗')
    print('║        🌱 SISTEMA DE GESTIÓN 🌱      ║')
    print('╠══════════════════════════════════════╣')
    print('║  1. Gestión de sectores              ║')
    print('║  2. Gestión de mediciones            ║')
    print('║  3. Consultas                        ║')
    print('║  4. Análisis de humedad              ║')
    print('║  5. Informes                         ║')
    print('║  6. Salir                            ║')
    print('╚══════════════════════════════════════╝')

    n = pide_opcion(1,6)
    SubOpciones(n, matriz, lst_codigos,tpl_meses, dicc)
    

def SubOpciones(n, matriz, lst_codigos,tpl_meses, dicc):
    if n == 1:
        print('\n╔══════════════════════════════════════╗')
        print('║        🌾 GESTIÓN DE SECTORES        ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Dar de alta un sector            ║')
        print('║  2. Buscar sector por ID             ║')
        print('║  3. Mostrar todos los sectores       ║')
        print('║  4. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')
        
        num = pide_opcion(1,4)
        if num==4:
            menuPrincipal(matriz, lst_codigos,tpl_meses, dicc)
        else:
            opciones.gestionSectores.llamarFunciones(num,matriz,lst_codigos,tpl_meses, dicc)

    elif n == 2:
        print('\n╔══════════════════════════════════════╗')
        print('║       💧 GESTIÓN DE MEDICIONES       ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Cargar / actualizar medición     ║')
        print('║  2. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')
        num = pide_opcion(1,2)
        if num==2:
            menuPrincipal(matriz, lst_codigos,tpl_meses, dicc)
        else:
            opciones.gestionMediciones.cargar_medicion(matriz,lst_codigos,tpl_meses, dicc)

    elif n == 3:
        print('\n╔══════════════════════════════════════╗')
        print('║             🔎 CONSULTAS             ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Consultar un sector              ║')
        print('║  2. Consultar mediciones de un mes   ║')
        print('║  3. Consultar estado de humedad      ║')
        print('║  4. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')
        num = pide_opcion(1,4) 
        if num==4:
            menuPrincipal(matriz, lst_codigos,tpl_meses, dicc)
        else:
            opciones.consultas.llamarfunciones(lst_codigos, matriz, num,tpl_meses, dicc)

    elif n == 4:
        print('\n╔══════════════════════════════════════╗')
        print('║        💧 ANÁLISIS DE HUMEDAD        ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Calcular promedio de un sector   ║')
        print('║  2. Calcular promedio de un mes      ║')
        print('║  3. Calcular promedio general        ║')
        print('║  4. Obtener mayor medición           ║')
        print('║  5. Obtener menor medición           ║')
        print('║  6. Contar estados por mes           ║')
        print('║  7. Atención por mes y cultivo       ║')
        print('║  8. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')
        num = pide_opcion(1,8)
        if num==8:
            menuPrincipal(matriz, lst_codigos,tpl_meses, dicc)
        else:
            opciones.analisisHumedad.llamarFunciones(num, matriz, lst_codigos, tpl_meses, dicc)
            
    elif n == 5:  
        print('\n╔══════════════════════════════════════╗')
        print('║             📄 INFORMES               ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Informe general del campo        ║')
        print('║  2. Informe de un sector             ║')
        print('║  3. Informe mensual                  ║')
        print('║  4. Sectores que requieren atención  ║')
        print('║  5. Ranking mensual de humedad       ║')
        print('║  6. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')
        num = pide_opcion(1,6)
        if num==6:
            menuPrincipal(matriz, lst_codigos,tpl_meses, dicc)
        else:
            opciones.informes.llamarFunciones(num,matriz,lst_codigos,tpl_meses, dicc)

    else:
        print('\n╔══════════════════════════════════════╗')
        print('║             🚪 SALIR                 ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Confirmar salida                 ║')
        print('║  2. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')
        num = pide_opcion(1,2)
        if num==2:
            menuPrincipal(matriz, lst_codigos,tpl_meses, dicc)
        elif num==1:
            if configuracion.cultivos.guardarMediciones(matriz, lst_codigos):
                print('¡Gracias!')
            else:
                print('El guardado no se completó. Puede volver a intentar la salida.')
                menuPrincipal(matriz, lst_codigos, tpl_meses, dicc)
