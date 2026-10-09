
from math import hypot, pi


class Circulo:
    def __init__(self, radio):
        if radio < 0:
            raise ValueError("El radio no puede ser negativo.")
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        if base < 0 or altura < 0:
            raise ValueError("La base y la altura no pueden ser negativas.")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        if lado < 0:
            raise ValueError("El lado no puede ser negativo.")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def calcular_hipotenusa(self):
        return hypot(self.base, self.altura)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        lados = (self.base, self.altura, self.calcular_hipotenusa())
        iguales = sum(1 for i in range(3) for j in range(i + 1, 3)
                      if abs(lados[i] - lados[j]) < 1e-9)
        if iguales == 3:
            return "Equilátero"
        if iguales > 0:
            return "Isósceles"
        return "Escaleno"


def main():
    circulo = Circulo(2)
    rectangulo = Rectangulo(1, 2)
    cuadrado = Cuadrado(3)
    triangulo = TrianguloRectangulo(3, 5)

    figuras = (
        ("Círculo", circulo), ("Rectángulo", rectangulo),
        ("Cuadrado", cuadrado), ("Triángulo rectángulo", triangulo),
    )
    for nombre, figura in figuras:
        print(f"{nombre}: área = {figura.calcular_area():.2f}, "
              f"perímetro = {figura.calcular_perimetro():.2f}")
    print(f"Hipotenusa = {triangulo.calcular_hipotenusa():.2f}")
    print(f"Tipo de triángulo = {triangulo.determinar_tipo_triangulo()}")


if __name__ == "__main__":
    main()
