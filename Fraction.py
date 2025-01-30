class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            splitStr = numerator.split('/')
            self.numerator = int(splitStr[0])
            self.denominator = int(splitStr[1])
        elif numerator%1 == 0 and denominator%1 == 0:
            self.numerator = numerator
            self.denominator = denominator
        pass

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass