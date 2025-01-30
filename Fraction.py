class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError
        if isinstance(numerator, str):
            splitStr = numerator.split('/')
            try:
                self.numerator = int(splitStr[0])
                self.denominator = int(splitStr[1])
            except ValueError:
                self.numerator = 0
                self.denominator = 1
        elif numerator%1 == 0 and denominator%1 == 0:
            self.numerator = numerator
            self.denominator = denominator
        pass

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
        if self.numerator == 0 or self.denominator == 0:
            return '0'
        nume_isNegative = True if '-' in self.get_numerator() else False
        deno_isNegative = True if '-' in self.get_denominator() else False
        absFraction = f"{abs(int(self.get_numerator()))}/{abs(int(self.get_denominator()))}"
        if (nume_isNegative and not deno_isNegative) or (not nume_isNegative and deno_isNegative):
            return "-" + absFraction
        return absFraction