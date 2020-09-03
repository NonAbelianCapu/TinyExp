import numpy as np 

""" 
Posible idea armar un stack para las expresiones para derivar y arrastrar las expresiones 
El problema es que necesito una estructure mas grande para guardar ese stack: esperar a armar la clase
de experimento .. 

"""


class Measure:

    def __init__(self, value, error, unit=None, instrument=None, error_dist = 'gaussian'):

        # hagamos un par de sanity checks 

        if unit is not None:

            if not isinstance(unit, str):

                raise TypeError("unit must be str")

            self.unit = unit

        else:
            self.unit = 'u'

        if not np.isscalar(value):
            raise TypeError("value must be a numpy scalar")

        if not np.isscalar(error):
            raise TypeError("error must be a numpy scalar")

        
        self.value = value
        self.error = error
        self.instrument = instrument

        if error_dist is not None:
            self.error_dist = error_dist

        self.error_dist == 'gaussian'


    def __repr__(self):
        
        return "({} +/- {}) {}".format(self.value, self.error, self.unit)

    def __add__(self, other):

        if isinstance(other, Measure):

            if self.error_dist == other.error_dist:
                if self.error_dist == 'gaussian':
                    
                    # si las dos muestras provienen de distibuciones gaussianas propagamos normalmente    
                                    
                    return Measure(self.value + other.value, np.sqrt(self.error**2 + other.error**2))
                    
            raise TypeError('Error sample distrubitions dont match')

        raise TypeError('Both objects must be a Measures')

    # aca faltaria agregar que pasa cuando las dsitribuciones no son gaussianas

    

    #  despues sigo sobre-escribiendo las clases
    #  tal vez pueda hace un arbol de expresiones
    #  para derivar simbolicamente 

    """ 
    
    Overlodeamos las operaciones basicas para comparar solo el valor y no el error, dado que estamos suponiendo que
    vienen de la misma distrubcion lo mas razonable es que el error no forme parte de la comparacion
    
    """

    def __eq__(self, other):
        
        if isinstance(other,Measure):
            if self.value == other.value:
                return True 
            return False 
        return False 

    def __ne__(self, other):
        
        if isinstance(other,Measure):
            if self.value != other.value:
                return True 
            return False 
        return False 


    def __lt__(self, other):
        
        if isinstance(other,Measure):
            if self.value < other.value:
                return True 
            return False 
        return False 

    def __gt__(self, other):
        
        if isinstance(other,Measure):
            if self.value > other.value:
                return True 
            return False 
        return False 


    def __le__(self, other):
        
        if isinstance(other,Measure):
            if self.value <= other.value:
                return True 
            return False 
        return False 

    def __ge__(self, other):
        
        if isinstance(other,Measure):
            if self.value >= other.value:
                return True 
            return False 
        return False



    def __mul__(self, other):

        if isinstance(other, Measure):

            prop_value = self.value*other.value

            prop_error = np.abs(self.value*other.value)*np.sqrt(self.error**2/self.value**2 + other.error**2*other.value**2)

            return Measure(prop_value, prop_error)   # cambiar la propagacion de errores aca luego
        


        elif np.isscalar(other):

            return Measure(self.value*other, np.abs(a)*self.error)


        raise TypeError('ver que carajo poner aca')


    def __truediv__(self, other):
        
        if isinstance(other, Measure):
            
            prop_value = self.value/other.value
            prop_error = np.abs(self.value/other.value)*np.sqrt(self.error**2/self.value**2 + other.error**2*other.value**2)

        elif np.isscalar(other):
            pass

        raise TypeError('')




    def __pow__(self):
        pass    
    

 
