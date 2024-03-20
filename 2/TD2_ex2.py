class Fraction():
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

    def add(self,other_fraction):
        if type(other_fraction)!=type(self):
            raise ValueError('Other fraction must be a fraction')
            
        add_numerator=(self.__numerator*other_fraction.__denominator + 
                       self.__denominator*other_fraction.__numerator)
        add_denominator=self.__denominator*other_fraction.__denominator
        return(Fraction(add_numerator,add_denominator))
    
    def mult(self,other_fraction):
        if type(other_fraction)!=type(self):
            raise ValueError('Other fraction must be a fraction')
        
        mult_numerator=self.__numerator*other_fraction.__numerator
        mult_denominator=self.__denominator*other_fraction.__denominator
        return(Fraction(mult_numerator,mult_denominator))
        
    def simplify(self):
        if self.__numerator>=self.__denominator:
            biggest_number=self.__numerator
            smallest_number=self.__denominator
        else:
            biggest_number=self.__denominator
            smallest_number=self.__numerator
            
        for number in range(smallest_number,0,-1):
            if smallest_number % number == 0:
                if biggest_number % number == 0:
                    return(Fraction(self.__numerator//number,self.__denominator//number))
        return(Fraction(self.__numerator,self.__denominator))
        
        
    def __eq__(self,other_fraction):
        if type(other_fraction)!=type(self):
            raise ValueError('Other fraction must be a fraction')
        return(self.__numerator/self.__denominator == 
            other_fraction.__numerator/other_fraction.__denominator)


if __name__=='__main__':
    fraction_1=Fraction(8,2)
    fraction_2=Fraction(2,3)
    fraction_1.add(fraction_2)
    fraction_1.mult(fraction_2)
    fraction_1.simplify()

