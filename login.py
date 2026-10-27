import re

def crear_usuarios():
    try:
        archivo = open("login.csv", mode="rt")
    except FileNotFoundError:
        try:
            archivo = open("login.csv", mode="wt")
        except OSError:
            print("Error al crear el archivo.")
            return False
        else:
            archivo.write("usuario,clave\n")
            archivo.write("Administrador,Los perpetto\n")
            archivo.close()
            print("Archivo de usuarios creado correctamente.")
    except OSError:
        print("Error al abrir el archivo.")
        return False
    else:
        archivo.close()
    return True

def login():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su contraseña: ")
        if not re.fullmatch(r"[a-zA-Z0-9_]+", usuario):
            print("Formato de usuario inválido.")
        elif not re.fullmatch(r"[a-zA-Z0-9 ]+", clave):
            print("Formato de contraseña inválido.")
        else:
            try:
                archivo = open("login.csv", mode="rt")
            except OSError:
                print("Error al abrir el archivo de usuarios.")
                return False
            else:
                acceso = False
                archivo.readline()
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) == 2:
                        usuario_guardado, clave_guardada = datos
                        if usuario == usuario_guardado and clave == clave_guardada:
                            acceso = True
                            break
                archivo.close()
                if acceso:
                    print("Inicio de sesión exitoso.")
                    return True
                else:
                    print("Usuario o contraseña incorrectos.")
        intentos += 1
        print("Intentos restantes:", 3 - intentos)
    print("Se agotaron los intentos. Programa finalizado.")
    return False
