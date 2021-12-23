class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    
    def __add__(self, c):
        return Complex(self.real+c.real, self.imaginary+c.imaginary)

    def __str__(self):
        return f"{self.real} + i{self.imaginary}"

c1 = Complex(87, 4)
c2 = Complex(2, 689)
print(c1+c2)