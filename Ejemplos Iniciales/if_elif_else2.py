"""Saber el rango de edad de una persona"""

edad = int (input("Por favor ingrese su edad:"))

if edad <= 12:
    print ("Es un niño")
elif edad <= 17:
    print("Es un joven")
elif edad > 60:
    print("Es un adulto mayor")
elif edad > 105:
    print ("Ustes es un robot ?")
