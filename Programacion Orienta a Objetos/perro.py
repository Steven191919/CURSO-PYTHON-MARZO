class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} de {self.edad} años"

perro_1 = Perro("Negro","15")
print(perro_1)

perro_2 = Perro ("Orito","2")
print(perro_2)