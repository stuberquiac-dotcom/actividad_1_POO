import math


class Circulo:
    def __init__(self, radio: float):
        self.__radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.__radio ** 2)

    def calcular_longitud(self) -> float:
        return 2 * math.pi * self.__radio


r = float(input("Ingrese el radio del círculo: "))

c = Circulo(r)

print(f"Radio ingresado: {r}")
print(f"Área del círculo: {c.calcular_area():.4f}")
print(f"Longitud de la circunferencia: {c.calcular_longitud():.4f}")
