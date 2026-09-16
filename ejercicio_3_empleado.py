class Empleado:
    def __init__(self, horas_trabajadas: float, valor_hora: float, porcentaje_retencion: float):
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora
        self.__porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self) -> float:
        return self.__horas_trabajadas * self.__valor_hora

    def calcular_retencion(self) -> float:
        return self.calcular_salario_bruto() * (self.__porcentaje_retencion / 100.0)

    def calcular_salario_neto(self) -> float:
        return self.calcular_salario_bruto() - self.calcular_retencion()


horas = float(input("Ingrese las horas trabajadas en el mes: "))
valor = float(input("Ingrese el valor por hora: "))
retencion = float(input("Ingrese el porcentaje de retención en la fuente (%): "))

emp = Empleado(horas, valor, retencion)

print(f"Salario Bruto: ${emp.calcular_salario_bruto():,.2f}")
print(f"Retención en la Fuente: ${emp.calcular_retencion():,.2f}")
print(f"Salario Neto a Pagar: ${emp.calcular_salario_neto():,.2f}")
