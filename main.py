import funciones
import configuracion.login as login
import configuracion.cultivos as cultivos

def main():
    dicc = cultivos.pasar_a_dic_cultivos()
    if dicc is None:
        return
    matriz, lst_codigos= cultivos.extracciones()
    tpl_meses = cultivos.extrer_tpl_meses()
    if matriz is None or tpl_meses is None:
        print("No se pudo iniciar el sistema. Revise los archivos antes de volver a intentar.")
        return
    if login.crear_usuarios():
        if login.login():
            funciones.menuPrincipal(matriz, lst_codigos, tpl_meses, dicc)
main()


""" 
informes/sectores_atencion --> agarrar los rangos de humedad dependiendo el sector
Gestion de Sectores --> Mostrar todos los sectores
Gestion de mediciones --> Actualizar medicion
Consultas --> Consultar estado de humedad
AnalisisHumedad --> Contar estados por mes
AnalisisHumedad --> Atencion por mes y cultivo
Informes --> Informe de un sector e informe mensual (error en la palabra Critico)
Informes --> Sectores que requieren atencion

"""