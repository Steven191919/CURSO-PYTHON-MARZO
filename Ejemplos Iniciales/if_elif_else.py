"""Ejemplos con if,elif,else"""

numero = int (input("Por favor ingrese un valor numerico: "))

#print(type(numero))
if numero > 0:
    print("Es un valor positivo")
elif numero < 0:
    print("Es un valor negativo")
else:
    print("Por favor ingrese un entero")