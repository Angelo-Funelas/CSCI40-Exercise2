class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        pass

    def gcd(a, b):
        '''
        @fn gcd returns the greatest common divisor between two integers.

        '''
        if a == 0 or b == 0:
            return 0
        if a%b == 0 or b%a == 0:
            return min(a,b)
        for num in range(min(a,b),0,-1):
            if a%num == 0 and b%num == 0:
                return num
        

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass