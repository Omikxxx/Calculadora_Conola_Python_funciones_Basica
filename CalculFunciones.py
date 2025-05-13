import colorama
import datetime
colorama.init()

def ingreso():
    global a,b
    a=float(input("Ingrese el primer numero:"))
    b=float(input("Ingrese el segundo numero:"))

def suma():

    print(f" {colorama.Fore.GREEN}ELIGIO LA OPCION DE SUMA{colorama.Style.RESET_ALL}")
    print(f" {colorama.Fore.BLUE}EL RESULTADO ES:{colorama.Style.RESET_ALL}", a+b)

def resta():
    print(f" {colorama.Fore.GREEN}ELIGIO LA OPCIÓN DE RESTA{colorama.Style.RESET_ALL}")
    print(f" {colorama.Fore.BLUE}EL RESULTADO ES:{colorama.Style.RESET_ALL}", a-b)
def multiplicacion():
    print(f" {colorama.Fore.GREEN}ELIGIO LA OPCION DE MULTIPLICACIÓN{colorama.Style.RESET_ALL}")
    print(f" {colorama.Fore.BLUE}EL RESULTADO ES:{colorama.Style.RESET_ALL}", a*b)
def division():
    print(f" {colorama.Fore.GREEN}ELIGIO LA OPCIÓN DE DIVISIÓN{colorama.Style.RESET_ALL}")
    print(f" {colorama.Fore.BLUE}EL RESULTADO ES:{colorama.Style.RESET_ALL}", a/b)
def salir():
    quit()



while(True):

    print("*********** |CALCULADORA CON FUNCIONES|*********")
    print("************|ELIJA UNA OPCIÓN:| *****************")

    print("SUMA(1)")
    print("RESTA(2)")
    print("MULTIPLICACIÓN(3)")
    print("DIVISIÓN(4)")
    print("SALIR (5)")
    opcion=int(input("INGRESE UNA OPCIÓN:"))
    if(opcion>5):
        print(f" {colorama.Fore.RED}¡¡¡INGRESE UNA OPCIÓN CORRECTA!!!{colorama.Style.RESET_ALL}")

    if(opcion==1):
        ingreso()
        suma()

    elif(opcion==2):
        ingreso()
        resta()
    elif(opcion==3):
        ingreso()
        multiplicacion()
    elif(opcion==4):
        ingreso()
        division()
    elif(opcion==5):
        salir()


