# Author: Victor Mamontov
# Make class for operation on complex numbers

class Complex:
    """:param a: real part and b - imaginary part, class returns result as a+bi"""
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __add__(self, other):
        real = self.a + other.a
        imaginary = self.b + other.b
        return Complex(real, imaginary)

    def __sub__(self, other):
        real = self.a - other.b
        imaginary = self.b - other.b
        return Complex(real, imaginary)
    
    def __mul__(self, other):
        real = self.a * other.a - self.b * other.b
        imaginary = self.a * other.b + self.b * other.a
        return Complex(real, imaginary)

    def __truediv__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        if d < 0:
            real = (a * c - b * abs(d))/(c * c + d * d)
            imaginary = (a * abs(d) + b * c)/(c * c + d * d)
            return Complex(real, imaginary)
        else:
            real = (a * c + b * d)/(c * c + d * d)
            imaginary = (a * (-d) + b * c)/(c * c + d * d)
            return Complex(real, imaginary)

    def __str__(self):
        if self.b > 0:
            return f'{self.a} + {self.b}i'
        else:
            return f'{self.a} - {abs(self.b)}i'


number_1 = Complex(1, 0)
number_2 = Complex(1, -1)
print(number_1 / number_2)
print(number_2 * number_2)
number_3 = Complex(2, 2)
print(number_1 - number_2)
