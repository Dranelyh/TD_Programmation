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

    def add(self,other_fraction):
        """
        Parameter
        ----------
        other_fraction : TYPE Fraction
            DESCRIPTION : The fraction that you want to add to self

        Return
        -------
        Type Fraction
        Return a new fraction with the value of the addition of self with 
        other_fraction
        """
        if type(other_fraction)!=type(self):
            raise ValueError('Other fraction must be a fraction')
            
        add_numerator=(self.__numerator*other_fraction.__denominator + 
                       self.__denominator*other_fraction.__numerator)
        add_denominator=self.__denominator*other_fraction.__denominator
        return(Fraction(add_numerator,add_denominator))
    
    def mult(self,other_fraction):
        """
        Parameter
        ----------
        other_fraction : TYPE Fraction
            DESCRIPTION : The fraction that you want to multiply by self

        Return
        -------
        Type Fraction
        Return a new fraction with the value of the multiplication of self with 
        other_fraction
        """
        if type(other_fraction)!=type(self):
            raise ValueError('Other fraction must be a fraction')
        
        mult_numerator=self.__numerator*other_fraction.__numerator
        mult_denominator=self.__denominator*other_fraction.__denominator
        return(Fraction(mult_numerator,mult_denominator))
        
    def simplify(self):
        """
        Returns
        -------
        Return a new fraction which the simplification of self

        """
        if abs(self.__numerator)>=abs(self.__denominator):
            biggest_number=abs(self.__numerator)
            smallest_number=abs(self.__denominator)
        else:
            biggest_number=abs(self.__denominator)
            smallest_number=abs(self.__numerator)
            
        #Euclide algorithme to find the greatest common denominator
        while smallest_number>0:
            biggest_number, smallest_number = (smallest_number, 
            biggest_number % smallest_number)
        return(Fraction(self.__numerator//biggest_number,
                        self.__denominator//biggest_number))
        
        
    def __eq__(self,other_fraction):
        if type(other_fraction)!=type(self):
            raise ValueError('Other fraction must be a fraction')
        return(self.__numerator/self.__denominator == 
            other_fraction.__numerator/other_fraction.__denominator)

###############################################################################
if __name__=='__main__':
    fraction_1=Fraction(2,4)
    fraction_2=Fraction(2,3)
    fraction_3=fraction_1.add(fraction_2)
    fraction_4=fraction_1.mult(fraction_2)
    
    assert fraction_1.add(fraction_2)==Fraction(14,12)
    assert fraction_1.mult(fraction_2)==Fraction(4,12)
    assert fraction_1.simplify()==Fraction(1,2)

