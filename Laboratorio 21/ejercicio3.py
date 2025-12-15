import math
class Figura:
    id = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Figura.id += 1
        self.id = Figura.id
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    def mostrar_datos(self):
        print(f"\n--- {self.nombre} (ID: {self.id}) ---")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro():.2f}")
    def mostrar_longitudes(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    def mostrar_longitudes(self):
        print(f"Base: {self.base}\nAltura: {self.altura}") 

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3, base, altura):
        super().__init__("Triángulo")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    def mostrar_longitudes(self):
        print(f"Base: {self.base}\nAltura: {self.altura}") 
        print(f"Lado 1: {self.lado1}\nLado 2: {self.lado2}\nLado 3: {self.lado3}") 

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    def mostrar_longitudes(self):
        print(f"Radio: {self.radio}") 

figuras = [
        Rectangulo(base=5, altura=3),
        Triangulo(lado1=3, lado2=4, lado3=5, base=4, altura=3),
        Circulo(radio=4)
    ]

print("=" * 35)
print("CÁLCULO DE ÁREAS Y PERÍMETROS")
print("=" * 35) 
for figura in figuras:
    figura.mostrar_datos()
    figura.mostrar_longitudes()