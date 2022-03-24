"""Operaciones con Diccionarios"""

from webbrowser import get


diccionario = {"nombre":"Juan", "apellido":"Perez", "cedula":1718960303, "f_nacimiento": "12/02/2000"}
lisita1 = ["Juan", "Pedro", "Jova"]
lisita2 = ["persona1", "persona2", "persona3"]

#lisita3 = [("persona1", "Juan"),
           #("persona2", "Lucas")
           #("persona3", "Jova")]

#print(dict(lisita3))
#print(type(dict(lisita3)))

variable1=zip(lisita1, lisita2)
print(variable1)

#print(diccionario.get("nombre"))
#print(diccionario.get("cedula"))
#print(diccionario.pop("f_nacimiento"))

diccionario.update({"f_nacimiento":"16/04/2000"})
print(diccionario)
