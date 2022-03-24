""" 
Ejercico 1
"""

from io import open

nombre_texto = open("E:/CURSO PYTHON MARZO/nombre.txt", "w")

frase = "Geovanny \n Elsa \n Alejandro \n Mafer \n Elizabeth  "

nombre_texto.write(frase)

nombre_texto.close()

archivo_texto = open("E:/CURSO PYTHON MARZO/archivo.txt", "r")

texto = archivo_texto.readlines()

archivo_texto.close()

print(texto)