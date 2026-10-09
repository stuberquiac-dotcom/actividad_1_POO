class Persona:
    def __init__(self, nombre, apellidos, numero_documento_identidad, anio_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = str(numero_documento_identidad)
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.numero_documento_identidad}")
        print(f"Año de nacimiento = {self.anio_nacimiento}\n")


def main():
    persona1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    persona2 = Persona("Luis", "León", "1053223344", 2001)
    persona1.imprimir()
    persona2.imprimir()


if __name__ == "__main__":
    main()
