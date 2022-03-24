class Figuras:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Yo soy la clase Figuras, mi nombre es {self.nombre}"
    
    def leyenda(self):
        return f"Las figuras como tal nos permite identificar alguna particularidad propia en una de otras"
    
class FigurasCuadradas:
    
    def __init__(self, nombre, lados):
        self.nombre = nombre
        self.lados = lados
    
    def __str__(self):
        return f" Yo soy la clase Figuras Cuadradas, mi nombre es {self.nombre}"
    
class FigurasCirculares:
    
    def __init__(self, nombre, figura):
        self.nombre = nombre
        self.figura = figura
    
    def __str__(self):
        return f"Yo soy la clase Figuras Circulares, mi nombre es {self.nombre}"
    
class Cuadrado(FigurasCuadradas, Figuras):
    
    def __init__(self, nombre, lados):
        super().__init__(nombre, lados)
        
    def __str__(self):
        return f"Yo soy la clase Cuadrado, mi nombre es {self.nombre}"
    
Rombo = Cuadrado("Rombo", [2,2,2,2])
print(Rombo.lados)
print(Rombo)
print(Rombo.leyenda())