import datetime
import sys
import ProcesoCajero as proceso
#Clase principal 
datetime_object = datetime.datetime.now()
print(datetime_object)
cadena1 = "Ingresa el PIN: "
intento = 1
while intento <=3:
    cadena = f"PIN Incorrecto\n(Intento {intento}) {cadena1}" if intento>1 else cadena1
    print(cadena)
    pin = input()
    if pin == "1234":
        break
    else:
        intento = intento + 1

if intento > 3:
    print("PIN INCORRECTO\nSe terminaron los intentos")
    sys.exit(1)

proceso.procesoCajero()