from collections import namedtuple

class Rational(namedtuple('Rational', ['num', 'denom'])):
    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be null')
        if denom < 0:
            num, denom = -num, -denom

        factor = Rational.gcd(denom, num)

        return super().__new__(cls, num // factor, denom // factor)

    @staticmethod
    def gcd(denom, num):
        x = abs(num)
        y = abs(denom)
        while x:
            x, y = y % x, x
        factor = y
        return factor

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)