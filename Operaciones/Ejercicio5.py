"""Ejercio 5"""

nombre = input ("Como te llamas ?")
edad = input ("Cual es tu edad?")
direccion = input ("Donde vives ?")
telefono = input ("Cual es tu numero de telefono?")
codigo = input ("Cual es tu codigo postal?")
persona = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono, "codigopostal": codigo}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'su número de teléfono es', persona['telefono'], 'y su codigo postal es', persona['codigopostal'])