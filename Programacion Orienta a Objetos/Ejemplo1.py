class Monster:

    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria 

    def myFunc(self):
        print("Hey, yo soy "+ self.nombre)

mounstrito = Monster("Sullivan","Lloron")
print(mounstrito.nombre)
print(mounstrito.categoria)
mounstrito.myFunc()