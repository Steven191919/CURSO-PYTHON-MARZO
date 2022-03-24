"""Operaciones con Tuplas"""

tupla1 = ("a", "1", "1")
tupla2 = ("a", "b", "c")

print(tupla1 + tupla2)
print(tupla1 * 2)
print(tupla1<tupla2)

lista =[1,1,3]
print(type(lista))

tupla = tuple(lista)
print(type(tupla))
print(type(tupla))
print(tupla)

for x in tupla:
  print(x)

  print(tupla.count(1))

  #print(tupla.index(5))

