class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} {self.imaginary}i"
        return f"{self.real} + {self.imaginary}i"


comp_num_1 = ComplexNumber(3, 1)
comp_num_2 = ComplexNumber(2, -2)

print(comp_num_1 + comp_num_2)
print(comp_num_1 * comp_num_2)
