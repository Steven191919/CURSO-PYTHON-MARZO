from turtle import color


class Veterinaria:

    def __init__(self, nombre, edad, color, ojos, raza, sexo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.ojos = ojos
        self.raza = raza
        self.sexo = sexo

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años es de color {self.color} sus ojos son {self.ojos} su raza es {self.raza} y su genero es {self.sexo}"

gato_1 = Veterinaria("Kiti","10","blanco","azules","Persa","Hembra")
print(gato_1)

gato_2 = Veterinaria("Luis","12","negro","marron","Bengala","Macho")
print(gato_2)

