"""Ejemlos de Operaciones con listas"""

lista = ["a", "e", "i", "o", "u"]
print("La cantidad de valores de la lista es:", len(lista))
print(lista[4])
lista2 = (lista[0:3])
print(lista2)

#Se agrega

lista.append("j")
print(lista)

#Se remueve

lista.remove("j")
print("La cantidad de valores de lista es:", len(lista))
print(lista)

lista.insert(4, "Geovanny")
print(lista)

print(lista.index("u"))

lista3 = lista +lista2
print(lista3)

