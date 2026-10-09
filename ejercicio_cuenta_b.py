
from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = str(numero_cuenta)
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.value}")
        print(f"Saldo = ${self.saldo:,.2f}")

    def consultar_saldo(self):
        print(f"El saldo actual es = ${self.saldo:,.2f}")
        return self.saldo

    def consignar(self, valor):
        if valor <= 0:
            print("El valor a consignar debe ser mayor que cero.")
            return False
        self.saldo += valor
        print(f"Se ha consignado ${valor:,.2f}. El nuevo saldo es ${self.saldo:,.2f}")
        return True

    def retirar(self, valor):
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero.")
            return False
        if valor > self.saldo:
            print("No se puede retirar un valor superior al saldo actual.")
            return False
        self.saldo -= valor
        print(f"Se ha retirado ${valor:,.2f}. El nuevo saldo es ${self.saldo:,.2f}")
        return True

def main():
    cuenta = CuentaBancaria("Pedro", "Pérez", "123456789", TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    cuenta.consultar_saldo()

if __name__ == "__main__":
    main()
