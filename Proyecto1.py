"""
Su trabajo consiste en implementar una aplicación de escritorio para administrar el juego
utilizando el lenguaje Python. El sistema inicia con un Menú Principal donde se puede ingresar a
las:
• (I) Inventario,
• (F) Facturar
• (R) Reportes
• (S) Salir.
"""

def contenidoMenu():
    print(""" 
    
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║    Bienvenido al sistema de punto de venta                                                                               ║
        ║    Por favor digite un número para realizar una operacion del menú                                                       ║
        ║                                                                                                                          ║
        ║     Nombre del menu               |Funciones                                                                             ║ 
        ║    1= Inventario                  | Te permite agregar,modificar,eliminar productos dentro del inventario                ║     
        ║    2= Facturar                    | Facturar productos                                                                   ║
        ║    3= Reportes                    | Imprime los productos que estan en inventario, por categoria, producto y existencia  ║
        ║    4= Salir                       | Cierras la aplicacion                                                                ║
        ║                                                                                                                          ║
        ║                                                                                                       Version 1.0  ←     ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

def menu():
    salir= "4" or "Facturar" or "facturar"
    contenidoMenu()
    if password() == True:
        while funcion != salir:

            funcion = input("Digite la funcion que desea realizar")
            if funcion == 1 or funcion == "inventario" or funcion == "Inventario":
                print(inventario())
            elif funcion == 2 or funcion == "facturar" or funcion == "Facturar":
                print(facturar())
            elif funcion == 3 or funcion == "reportes" or funcion == "Reportes":
                print(reportes())
        return "Gracias por usar el programa " + exit()

def password():
    digitosusuario=""
    digitoscontraseña=""
    comprobar = open("Acceso.txt", mode="r", encoding="utf-8")
    lineas= comprobar.readlines()
    linea= comprobar.readline()
    comprobar.close()
    registro = input("¿Ya tienes cuenta? Por favor digite si o no ")
    if registro == "no" or registro == "No":
        comprobar= open("Acceso.txt", mode="a", encoding="utf-8")
        newUsuario= input("Digite un usuario")
        newContraseña= input("Digite una nueva contraseña")
        newCredenciales= newContraseña,newUsuario
        comprobar.write(newCredenciales)
        comprobar.close()
    else:
        credencialesUsuario = input("Digite su nombre de usuario ")
        credencialesContraseña = input("Digite su contraseña ")
        #while (digitosusuario != credencialesUsuario) and (digitoscontraseña != credencialesContraseña):
        digitosusuario = input("Digite el usuario ")
        digitoscontraseña = input("Digite la contraseña ")
        credenciales =  digitosusuario,digitoscontraseña
        for linea in comprobar:
            if (credenciales == linea):
                return True
        return "Error: contraseña o nombre de usuario invalidos"

def inventario():
    inventario = open("inventario.txt", mode="a",encoding ="utf-8")
    producto = nombre,categoria,preciounitario
def facturar():

def reportes():



def buscarEnTexto(texto, textoABuscar):
        # validar que sea tipo string
    if isinstance(texto, str) and isinstance(textoABuscar, str):
        if (texto != "") and (textoABuscar != 0):
            return buscarEnTexto_Aux(texto, textoABuscar)
        else:
            return "Error: el texto debe tener contenido"
    else:
        return "Error el texto no es tipo string"

def buscarEnTexto_Aux(texto, textoABuscar):

    if texto != textoABuscar:
        return "lo siento debe usar la funcion correspondiente"
        resultado = False
        largo = largoTexto(textoABuscar)
    else:
        while (texto != ""):
            textoCorte = texto[0: largo]
            if textoABuscar == textoCorte:
                resultado = True
                break
            else:
                texto = texto[1:]
        return resultado