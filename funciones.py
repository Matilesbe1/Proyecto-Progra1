
def menuPrincipal():

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

    try: 
        n = int(input('\n Ingrese una opción: '))
        SubOpciones(n)

    except ValueError:
        print(' ERROR: Ocurrió un error en el programa')


def SubOpciones(n):

    if n == 1:

        print('\n╔══════════════════════════════════════╗')
        print('║        🌾 GESTIÓN DE SECTORES        ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Dar de alta un sector            ║')
        print('║  2. Buscar sector por ID             ║')
        print('║  3. Mostrar todos los sectores       ║')
        print('║  4. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')

        num = int(input('\n Ingrese una opción: '))

        while num != 4:
            pass


    elif n == 2:

        print('\n╔══════════════════════════════════════╗')
        print('║       💧 GESTIÓN DE MEDICIONES       ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Cargar / actualizar medición     ║')
        print('║  2. Consultar medición de un sector  ║')
        print('║  3. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')

        num = int(input('\n Ingrese una opción: '))

        while num != 3:
            pass


    elif n == 3:

        print('\n╔══════════════════════════════════════╗')
        print('║             🔎 CONSULTAS             ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Consultar un sector              ║')
        print('║  2. Consultar mediciones de un mes   ║')
        print('║  3. Consultar estado de humedad      ║')
        print('║  4. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')

        num = int(input('\n Ingrese una opción: '))

        while num != 4:
            pass


    elif n == 4:

        print('\n╔══════════════════════════════════════╗')
        print('║        💧 ANÁLISIS DE HUMEDAD        ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Calcular promedio de un sector   ║')
        print('║  2. Calcular promedio de un mes      ║')
        print('║  3. Calcular promedio general        ║')
        print('║  4. Obtener mayor medición           ║')
        print('║  5. Obtener menor medición           ║')
        print('║  6. Contabilizar sectores            ║')
        print('║  7. Sectores que requieren atención  ║')
        print('║  8. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')

        num = int(input('\n Ingrese una opción: '))

        while num != 8:
            pass


    elif n == 5:

        print('\n╔══════════════════════════════════════╗')
        print('║             📄 INFORMES              ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Informe general del campo        ║')
        print('║  2. Informe de un sector             ║')
        print('║  3. Informe mensual                  ║')
        print('║  4. Sectores que requieren atención  ║')
        print('║  5. Ranking mensual de humedad       ║')
        print('║  6. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')

        num = int(input('\n Ingrese una opción: '))

        while num != 6:
            pass


    else:

        print('\n╔══════════════════════════════════════╗')
        print('║             🚪 SALIR                 ║')
        print('╠══════════════════════════════════════╣')
        print('║  1. Confirmar salida                 ║')
        print('║  2. Volver al menú principal         ║')
        print('╚══════════════════════════════════════╝')

        num = int(input('\n Ingrese una opción: '))

