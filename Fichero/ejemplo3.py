""" 
Leer ficheros o archivos
"""

from io import open

archivo_texto = open("E:/CURSO PYTHON MARZO/archivo.txt", "r")

texto = archivo_texto.readlines()

archivo_texto.close()

print(texto)