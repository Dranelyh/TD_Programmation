class Fraction():
    """
    class : Fraction(numerator,denominator)
    arguments:
        numerator : int
        denominator: int
    Automatically print the fraction as (numerator / denominator)
    """
    
    def __init__(self,numerator,denominator):
        if type(numerator)!=int or type(denominator)!=int:
            raise ValueError('Values must be integer')
        if denominator==0:
            raise ValueError('Denominator must not be zero')
        self.__numerator=numerator
        self.__denominator=denominator
        print('('+str(self.__numerator) +' / '+ str(self.__denominator)+')')
    
    def numerator(self):
        return self.__numerator
    
    def denominator(self):
        return self.__denominator
    
###############################################################################
if __name__=='__main__':
    fraction_1=Fraction(1,2)

        
