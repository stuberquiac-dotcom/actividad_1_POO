class CalculoEdades:
    def __init__(self, edad_juan: float):
        self.__edad_juan = edad_juan
        self.__edad_alberto = 0.0
        self.__edad_ana = 0.0
        self.__edad_mama = 0.0

    def calcular_edades(self) -> None:
        self.__edad_alberto = (2 / 3) * self.__edad_juan
        self.__edad_ana = (4 / 3) * self.__edad_juan
        self.__edad_mama = self.__edad_juan + self.__edad_alberto + self.__edad_ana

    def get_edad_alberto(self) -> float:
        return self.__edad_alberto

    def get_edad_ana(self) -> float:
        return self.__edad_ana

    def get_edad_mama(self) -> float:
        return self.__edad_mama


edad_juan = float(input("Ingrese la edad de Juan: "))

calculo = CalculoEdades(edad_juan)
calculo.calcular_edades()

print(f"Edad de Juan: {edad_juan:.1f} años")
print(f"Edad de Alberto: {calculo.get_edad_alberto():.1f} años")
print(f"Edad de Ana: {calculo.get_edad_ana():.1f} años")
print(f"Edad de la Mamá: {calculo.get_edad_mama():.1f} años")
