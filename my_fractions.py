def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

class Fraction:
    def __init__(self, top, bottom):
        if type(top) != int or type(bottom) != int:
            raise RuntimeError("top and bottom must be integers.")
        
        common = gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __repr__(self):
        return "Fraction(%d, %d)" % (self.num, self.den)
    def get_num(self):
        return self.num
    def get_den(self):
        return self.den
    def __eq__(self, other):
        return self.num * other.den == self.den * other.num
    def __ne__(self, other):
        return self.num * other.den != self.den * other.num
    def __lt__(self, other):
        return self.num * other.den < self.den * other.num
    def __le__(self, other):
        return self.num * other.den <= self.den * other.num
    def __gt__(self, other):
        return self.num * other.den > self.den * other.num
    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num
    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    __radd__ = __add__
    def __iadd__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        self.num = new_num
        self.den = new_den
        return self
    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)
    def __floordiv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)
    
        
