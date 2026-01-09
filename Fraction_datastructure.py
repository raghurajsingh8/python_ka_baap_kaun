from math import gcd

class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be zero")

        g = gcd(n, d)
        self.num = n // g
        self.den = d // g

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)


# ---- Usage ----
x = Fraction(3, 4)
y = Fraction(7, 8)

print(x)
print(y)

print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "*", y, "=", x * y)
print(x, "/", y, "=", x / y)
