from .cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            print("Error: el monto a extraer debe ser mayor a 0.")
            return False
        total = monto + self.costo_emision
        if total <= self._saldo:
            self._saldo -= total
            print(f"Cheque de ${monto:.2f} emitido por {self.titular} "
                f"(costo de emisión: ${self.costo_emision:.2f}).")
            return True
        print(f"Extracción rechazada: {self.titular} no tiene saldo para cubrir "
                f"${monto:.2f} + ${self.costo_emision:.2f} de costo de emisión.")
        return False
