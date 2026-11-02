from abc import ABC, abstractmethod


class CuentaBancaria(ABC):

    def __init__(self, titular, cbu, saldo_inicial=0):
        self.titular = titular        # Atributo público
        self._cbu = cbu               # Atributo protegido (solo lectura)
        self.saldo = saldo_inicial    # Pasa por el setter, que valida el valor

    # ---------- CBU: solo lectura (tiene @property pero NO setter) ----------
    @property
    def cbu(self):
        return self._cbu

    # ---------- SALDO: lectura y escritura controlada ----------
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser menor a cero.")
        self._saldo = valor

    # ---------- Métodos concretos ----------
    def depositar(self, monto):
        if monto <= 0:
            print(f"Error: el monto a depositar debe ser mayor a 0 (se intentó ${monto}).")
            return False
        self._saldo += monto
        print(f"Depósito de ${monto:.2f} realizado en la cuenta de {self.titular}.")
        return True

    def __str__(self):
        # self.__class__.__name__ devuelve el nombre de la clase real del objeto
        tipo_cuenta = self.__class__.__name__
        return f"[{tipo_cuenta}] Titular: {self.titular} | CBU: {self._cbu} | Saldo: ${self._saldo:.2f}"

    # ---------- Método abstracto: cada hija define su propia regla ----------
    @abstractmethod
    def extraer(self, monto):
        pass
