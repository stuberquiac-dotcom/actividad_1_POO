class PruebaEscritorio:
    def __init__(self):
        self.__suma = 0.0
        self.__x = 20.0
        self.__y = 40.0

    def ejecutar_pasos(self) -> None:
        self.__suma = self.__suma + self.__x
        self.__x = self.__x + (self.__y ** 2)
        self.__suma = self.__suma + (self.__x / self.__y)

    def get_suma(self) -> float:
        return self.__suma

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y


prueba = PruebaEscritorio()
prueba.ejecutar_pasos()

print(f"El valor final de SUMA es: {prueba.get_suma()}")
print(f"El valor final de X es: {prueba.get_x()}")
print(f"El valor final de Y es: {prueba.get_y()}")
