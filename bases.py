class Number():
    def __init__(self, dijs=[], base=10, sign=1):
        self.sign = sign
        self.dijs = dijs
        self.base = base
        if not self.verify(): raise ValueError('Digits to not fit within base')

    @classmethod
    def num(self, num, base=10):
        sign = 1
        if num < 0:
            sign = -1
            num *= -1
        fr_dijs = [int(x) for x in str(num)]
        fr_base = base
        return self(dijs=fr_dijs, base=fr_base, sign=sign)

    def verify(self):
        for dij in self.dijs:
            if dij > self.base: return False
        return True

    def inbase(self, base):
        n = int(self) if int(self) > 0 else int(self) * -1
        new = Number(dijs=[], base=base, sign=self.sign)
        while n > 0:
            new.dijs.insert(0, n % base)
            n  = n // base
        return new

    def __add__(self, other):
        sum = int(self) + int(other)
        return self.num(sum, 10).inbase(self.base)

    def __sub__(self, other):
        dif = int(self) - int(other)
        return self.num(dif, 10).inbase(self.base)

    def __mul__(self, other):
        prod = int(self) - int(other)
        return self.num(prod, 10).inbase(self.base)

    def __truediv__(self, other):
        div = int(self) - int(other)
        return self.num(div, 10).inbase(self.base)

    def __repr__(self):
        return str(self.dijs) + ' in base ' + str(self.base) + ' * ' + str(self.sign)

    def __int__(self):
        di_sum = 0
        di_val = 1
        for dij in self.dijs[::-1]:  # reversed dijs
            di_sum += dij * di_val
            di_val = di_val * self.base
        return di_sum * self.sign

class N(Number): pass