class CalculoPotencias:
    def __init__(self, numero: float):
        self.__numero = numero

    def calcular_cuadrado(self) -> float:
        return self.__numero ** 2

    def calcular_cubo(self) -> float:
        return self.__numero ** 3


num = float(input("Ingrese un número: "))

potencias = CalculoPotencias(num)

print(f"Número ingresado: {num}")
print(f"Cuadrado: {potencias.calcular_cuadrado()}")
print(f"Cubo: {potencias.calcular_cubo()}")
