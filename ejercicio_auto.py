
from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"


class TipoAutomovil(Enum):
    CIUDAD = "Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"


class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0

    
    def get_marca(self): return self.marca
    def set_marca(self, valor): self.marca = valor
    def get_modelo(self): return self.modelo
    def set_modelo(self, valor): self.modelo = valor
    def get_motor(self): return self.motor
    def set_motor(self, valor): self.motor = valor
    def get_tipo_combustible(self): return self.tipo_combustible
    def set_tipo_combustible(self, valor): self.tipo_combustible = valor
    def get_tipo_automovil(self): return self.tipo_automovil
    def set_tipo_automovil(self, valor): self.tipo_automovil = valor
    def get_numero_puertas(self): return self.numero_puertas
    def set_numero_puertas(self, valor): self.numero_puertas = valor
    def get_cantidad_asientos(self): return self.cantidad_asientos
    def set_cantidad_asientos(self, valor): self.cantidad_asientos = valor
    def get_velocidad_maxima(self): return self.velocidad_maxima
    def set_velocidad_maxima(self, valor): self.velocidad_maxima = valor
    def get_color(self): return self.color
    def set_color(self, valor): self.color = valor
    def get_velocidad_actual(self): return self.velocidad_actual

    def set_velocidad_actual(self, velocidad):
        if not 0 <= velocidad <= self.velocidad_maxima:
            print("La velocidad debe estar entre 0 y la velocidad máxima permitida.")
            return
        self.velocidad_actual = velocidad

    def acelerar(self, incremento):
        if incremento <= 0:
            print("El incremento debe ser mayor que cero.")
        elif self.velocidad_actual + incremento > self.velocidad_maxima:
            print("No se puede superar la velocidad máxima del automóvil.")
        else:
            self.velocidad_actual += incremento

    def desacelerar(self, decremento):
        if decremento <= 0:
            print("El decremento debe ser mayor que cero.")
        elif self.velocidad_actual - decremento < 0:
            print("No se puede disminuir a una velocidad negativa.")
        else:
            self.velocidad_actual -= decremento

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia_km):
        if distancia_km < 0:
            raise ValueError("La distancia no puede ser negativa.")
        if self.velocidad_actual == 0:
            raise ValueError("El automóvil está detenido; no se puede estimar el tiempo.")
        return distancia_km / self.velocidad_actual 

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor (L) = {self.motor}")
        print(f"Tipo de combustible = {self.tipo_combustible.name}")
        print(f"Tipo de automóvil = {self.tipo_automovil.name}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima}")
        print(f"Color = {self.color.name}")
        print(f"Velocidad actual = {self.velocidad_actual}")


def main():
    auto = Automovil("Ford", 2018, 3.0, TipoCombustible.DIESEL,
                     TipoAutomovil.EJECUTIVO, 5, 6, 250, Color.NEGRO)
    auto.imprimir()
    auto.set_velocidad_actual(100)
    print(f"Velocidad actual = {auto.get_velocidad_actual()}")
    auto.acelerar(20)
    print(f"Velocidad actual = {auto.get_velocidad_actual()}")
    auto.desacelerar(50)
    print(f"Velocidad actual = {auto.get_velocidad_actual()}")
    auto.frenar()
    print(f"Velocidad actual = {auto.get_velocidad_actual()}")


if __name__ == "__main__":
    main()
