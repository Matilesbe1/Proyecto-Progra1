import funciones
import configuracion.login as login
import configuracion.cultivos as cultivos

def main():
    matriz, lst_codigos = cultivos.extraccionMatriz()
    tpl_meses = cultivos.extrer_tpl_meses()
    if login.crear_usuarios():
        if login.login():
            funciones.menuPrincipal(matriz, lst_codigos, tpl_meses)
main()