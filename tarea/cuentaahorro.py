from .cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):

    TASA_INTERES = 0.001  # 0.1 %

    def extraer(self, monto):
        if monto <= 0:
            print("Error: el monto a extraer debe ser mayor a 0.")
            return False
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Extracción de ${monto:.2f} realizada en la Caja de Ahorro de {self.titular}.")
            return True
        print(f"Extracción rechazada: saldo insuficiente en la Caja de Ahorro de {self.titular}.")
        return False

    def aplicar_interes(self):
        interes = self._saldo * self.TASA_INTERES
        self._saldo += interes
        print(f"Interés aplicado a la cuenta de {self.titular}: ${interes:.2f}")
