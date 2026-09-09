import funciones

def main():
    matriz = [[1, 2, 0, 4, 5], [10, 20, 30, 40, 1000], [1, 2, 3, 4, 5],  [0]]
    lst_codigos = ["100-BUE","101-TDF","102-COR","103-NQN","104-JUJ","105-SJN"]
    tpl_meses = [(1,"Ene"),(2,"Feb"),(3,"Mar"),(4,"Abr"),(5,"May"),(6,"Jun"),(7,"Jul"),(8,"Ago"),(9,"Sep"),(10,"Oct"),(11,"Nov"),(12,"Dic")]
    funciones.menuPrincipal(matriz, lst_codigos,tpl_meses)
    
main()