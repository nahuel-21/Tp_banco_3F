from .cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
        super().__init__(titular, cbu, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            print("Error: el monto a extraer debe ser mayor a 0.")
            return False
        if monto <= self._saldo + self.limite_descubierto:
            # Se modifica _saldo directamente (y no a través del setter)
            # porque la cuenta corriente puede quedar en negativo usando
            # el descubierto. El setter sigue protegiendo el saldo frente
            # a asignaciones externas inválidas.
            self._saldo -= monto
            print(f"Extracción de ${monto:.2f} realizada en la Cuenta Corriente de {self.titular}.")
            return True
        print(f"Extracción rechazada: se supera el límite de descubierto de {self.titular}.")
        return False
