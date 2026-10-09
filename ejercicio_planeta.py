
from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"


class Planeta:
    
    UA_EN_MILLONES_KM = 149.597870
    LIMITE_PLANETA_EXTERIOR = 3.4 * UA_EN_MILLONES_KM

    def __init__(self, nombre=None, cantidad_satelites=0, masa=0.0, volumen=0.0,
                 diametro=0, distancia_sol=0, tipo=TipoPlaneta.TERRESTRE,
                 observable=False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa  
        self.volumen = volumen  
        self.diametro = diametro  
        self.distancia_sol = distancia_sol 
        self.tipo = tipo
        self.observable = observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta (kg) = {self.masa:g}")
        print(f"Volumen del planeta (km³) = {self.volumen:g}")
        print(f"Diámetro (km) = {self.diametro}")
        print(f"Distancia media al Sol (millones de km) = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable a simple vista = {self.observable}")

    def calcular_densidad(self):
        if self.volumen == 0:
            raise ValueError("No se puede calcular la densidad con volumen cero.")
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        return self.distancia_sol > self.LIMITE_PLANETA_EXTERIOR


def main():
    tierra = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 149.6,
                     TipoPlaneta.TERRESTRE, True)
    jupiter = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820, 778.5,
                      TipoPlaneta.GASEOSO, True)
    for planeta in (tierra, jupiter):
        planeta.imprimir()
        print(f"Densidad (kg/km³) = {planeta.calcular_densidad():.4g}")
        print(f"Es planeta exterior = {planeta.es_planeta_exterior()}\n")


if __name__ == "__main__":
    main()
