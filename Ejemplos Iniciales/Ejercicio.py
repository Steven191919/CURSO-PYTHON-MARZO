"""Encontrar el mayor de 3 numeros ingresados por el usuario"""

x = input("Por favor ingrese el primer numero:")
y = input("Por favor ingrese el segundo numero:")
z = input("Por favor ingrese el tercer numero:")

if x > y and x > z:
    print("El mayor es:", x)
elif y > x and y > z:
    print("El mayor es:", y)
elif z > x and z > y:
    print("El mayor es:", z)
else: 
    print ("Los valores son iguales o no son valores enteros")
    