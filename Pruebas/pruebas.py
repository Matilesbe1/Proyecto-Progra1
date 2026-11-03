from opciones.gestionSectores import *
from configuracion.cultivos import *
from opciones.gestionSectores import *
from unittest.mock import patch
from configuracion.login import *
from opciones.analisisHumedad import *

#TESTEO VALIDAR CODIGO
def test_validar_codigo_correcto():
    assert valida_codigo("123-PAP", [], [], ['Soja', 'Trigo', 'Papa', 'Zanahoria', 'Batata']) ==True

def test_validar_codigo_incorrecto():
    assert valida_codigo("123-ABC", [], [], ['Soja', 'Trigo', 'Papa', 'Zanahoria', 'Batata'])==None

def test_validar_codigo_vacio():
    assert valida_codigo("", [], [], ['Soja', 'Trigo', 'Papa', 'Zanahoria', 'Batata'])==False

#TESTEO LOGIN
def test_login_correcto():
    with patch("builtins.input", side_effect=["Administrador", "Los perpetto"]):
        assert login() == True

def test_login_incorrecto():
    with patch("builtins.input", side_effect=["Admin", "123", "Admin", "123", "Admin", "123"]):
        assert login() == False

def test_login_vacio():
    with patch("builtins.input", side_effect=["", "", "", "", "", ""]):
        assert login() == False


#TESTEO BUSCA ID
def test_busca_id_existente():
    matriz = []
    lst_codigos = ["123-PAP", "456-ZAN"]
    tpl_meses = ()

    with patch("builtins.input", side_effect=["123-PAP", "", "1"]): #PONE EL CODIGO QUE PONDRIA EL USUARIO, EL ENTER CON "" Y EL 1 PARA DECIR QUE NO QUIERE BUSCAR MAS CODIGOS
        with patch("funciones.SubOpciones"):
            assert busca_id(matriz, lst_codigos, tpl_meses) == None

def test_busca_id_inexistente():
    matriz = []
    lst_codigos = ["123-PAP", "456-ZAN"]
    tpl_meses = ()

    with patch("builtins.input", side_effect=["999-XYZ", "1"]):
        with patch("funciones.SubOpciones"):
            assert busca_id(matriz, lst_codigos, tpl_meses) == None

def test_busca_id_vacio():
    matriz = []
    lst_codigos = ["123-PAP", "456-ZAN"]
    tpl_meses = ()
    with patch("builtins.input", side_effect=["", "1"]):  #ver
        with patch("funciones.SubOpciones"):
            assert busca_id(matriz, lst_codigos, tpl_meses) == None

#TESTEO CALCULAR PROMEDIO GENERAL
def test_promedio_general_sin_valor():
    assert calcularPromedioGeneral([[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]])==False

def test_promedio_general_con_valor():
    assert calcularPromedioGeneral([[1, 2, -1, -1, 79, -1, 100, -1, 60, -1, 50, -1]])==True

def test_promedio_general_vacio():
    assert calcularPromedioGeneral([])==False

#python -m pytest Pruebas/pruebas.py -v