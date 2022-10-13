import sys

from Movimiento import Movimiento

listMovimientos = []
def imprimirMovimientos():
    for obj in listMovimientos:
        obj.imprimir()
    input("\n\tPRESIONE ENTER PARA REGRESAR AL MENU...")

def crearMovimiento(saldo):
    saldoFinal = 0
    input_monto = input("Ingrese el monto a retirar: ")
    try:
        cantidad = float(input_monto)
    except:
        print("!INGRESE UNA CANTIDAD VALIDA!")
        input("\n\tPRESIONE ENTER PARA REGRESAR AL MENU...")
        return saldo
    if cantidad == 0:
        print("!INGRESE UNA CANTIDAD VALIDA!")
        input("\n\tPRESIONE ENTER PARA REGRESAR AL MENU...")
        return saldo
    if cantidad > saldo :
        print("Fondos insuficientes!")
        input("\n\tPRESIONE ENTER PARA REGRESAR AL MENU...")
        saldoFinal = saldo
    else :
        saldoFinal = saldo - cantidad
        m1 = Movimiento(saldo, cantidad)
        listMovimientos.append(m1)
        print("¡OPERACION EXITOSA!")
        input("\n\tPRESIONE ENTER PARA REGRESAR AL MENU...")

    return saldoFinal

def procesoCajero():
    saldo = 1000.0
    opcion = 0
    print("¡BIENVENIDO ELISEO!")
    while opcion != 4:
        print("\nSelecciona la opción deseada:");
        print("1. Consultar Saldo");
        print("2. Retirar Saldo");
        print("3. Historico de movimientos");
        print("4. Cerrar sesión");
        input_a = input()
        try:
            opcion = int(input_a)
        except:
            print("Opcion Incorrecta")
            opcion = 0

        if opcion == 1:
            print(f"El saldo es {saldo}")
            input("\n\tPRESIONE ENTER PARA REGRESAR AL MENU...")
        elif opcion == 2:
            saldo = crearMovimiento(saldo)
        elif opcion == 3:
            imprimirMovimientos()
        elif opcion == 4:
            print("Se cerró la sesión")
            sys.exit()
