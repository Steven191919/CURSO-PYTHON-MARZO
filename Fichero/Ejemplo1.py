""" 
Crear ficheros o archivos
"""

from io import open

archivo_texto = open("E:/CURSO PYTHON MARZO/archivo.txt", "w")

frase = "Esto es una frase escrita desde Python \n Esto es otra linea \n esto es una tercera linea"

archivo_texto.write(frase)

archivo_texto.close()