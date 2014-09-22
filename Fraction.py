import Tools

class Fraction:
    def __init__(self,n,d):
        test = n*d
        self.num= abs(int(n))
        self.den= abs(int(d))
        if test > 0:
            self.sign = 1
        else:
            self.sign = -1
        self.reduce()

    def __add__(self,other):
        try:
            num = self.sign * self.num * other.den + other.sign * self.den * other.num
            den = self.den * other.den
            return Fraction(num,den)
        except AttributeError:
            if float(other).is_integer():
                return self + Fraction(other,1)
            else:
                raise TypeError("Only add by Fractions or int-likes")
    def __radd__(self,other):
        return self + other
    def __neg__(self):
        return Fraction(-1*self.num, self.den)
    def __sub__(self,other):
        return self+ (-other)
    def __rsub__(self,other):
        return self - other
    def __mul__(self,other):
        try:
            num = self.num * other.num
            den = self.den * other.den
            return Fraction(num, den)
        except AttributeError:
            if float(other).is_integer():
                return Fraction(other*self.num, self.den)
            else:
                raise TypeError("Only multipy by Fractions or int-likes")
    def __rmul__(self,other):
        return self * other
    def __div__(self,other):
        return self * other.reciprocal()
    def __rdiv__(self,other):
        return self.reciprocal() * other
    def __float__(self):
        return float(self.num)/float(self.den)
    def __str__(self):
        return str(self.sign*self.num) + "/" + str(self.den)
    def __repr__(self):
        return "Fraction(" + str(self.sign*self.num) + ', ' + str(self.den) + ")"
    def reduce(self):
        gcd = Tools.gcd(self.num, self.den)
        self.num /= gcd
        self.den /= gcd
    def reciprocal(self):
        return Fraction(self.sign*self.den, self.num)




