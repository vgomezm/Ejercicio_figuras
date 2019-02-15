class Figura():

    def __init__ (self):
        pass

    def get_area(self):
        pass
    def get_perimetro(self):
        pass


class Cuadrado (Figura):

    def __init__ (self, lado):
        self.lado=lado

    def get_area(self):
        area=self.lado*self.lado
        return area

    def get_perimetro(self):
        perimetro=self.lado*4
        return perimetro
    
class Rectángulo (Figura):
    
    def __init__(self, lado1, lado2):
        self.lado1=lado1
        self.lado2=lado2
    def get_area(self):
        area=self.lado1*self.lado2
        return area
    def get_perimetro(self):
        perimetro=(2*self.lado1)+(2*self.lado2)

valor=Cuadrado(3)
print(valor.get_area())
print(valor.get_perimetro())
        
