class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        '''
        @constructor checks if arguments are valid. If invalid, the numerator is 
        set to 0, causing the fraction to be equal to 0.

        '''
        if denominator == 0:
            raise ZeroDivisionError
        
        if isinstance(numerator, str):
            splitStr = numerator.split('/')

            if len(splitStr) > 2:
                self.numerator = 0
                return
            
            try:
                self.numerator = int(splitStr[0])
                self.denominator = int(splitStr[1])

            except ValueError:
                self.numerator = 0

        elif numerator%1 == 0 and denominator%1 == 0:
            self.numerator = numerator
            self.denominator = denominator

        else:
            self.numerator = 0

    def gcd(a, b):
        '''
        @fn gcd returns the greatest common divisor between two integers.

        '''
        if a == 0 or b == 0:
            return 0
        
        if a%b == 0 or b%a == 0:
            return min(abs(a),abs(b))
        
        for num in range(min(abs(a),abs(b)),0,-1):
            if a%num == 0 and b%num == 0:
                return num
        
    def get_numerator(self):
        '''
        @fn get_numerator returns the numerator in lowest terms.

        '''   
        sign = "" if self.numerator//self.denominator>-1 else "-"
        
        if self.numerator % self.denominator == 0:
            return sign + str(abs(self.numerator//self.denominator))
        
        return sign + str(abs(self.numerator//Fraction.gcd(self.numerator,self.denominator)))

    def get_denominator(self):
        '''
        @fn get_denominator returns the denominator in lowest terms.

        '''  
        if self.numerator % self.denominator == 0:
            return "1"
        
        return str(abs(self.denominator//Fraction.gcd(self.numerator,self.denominator)))

    def get_fraction(self):
        '''
        @fn get_fraction returns the numerator and denominator in lowest terms.

        '''
        if self.numerator == 0:
            return '0'
        
        return f"{self.get_numerator()}/{self.get_denominator()}"
