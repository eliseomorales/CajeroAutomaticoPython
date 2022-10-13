import datetime

class Movimiento:
    def __init__(self, saldo, cantidad_retirada):
        self.saldo = saldo
        self.cantidad_retirada = cantidad_retirada
        self.datetime_object = datetime.datetime.now()

    def imprimir(self):
        print(f"Movimiento [fecha={self.datetime_object}, Saldo Anterior={self.saldo}, Cantidad Retirada={self.cantidad_retirada}]")