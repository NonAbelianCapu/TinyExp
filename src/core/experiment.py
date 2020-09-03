import measure
import dataset

class Experiment:
    
    def __init__(self, data, graphics, name, instruments):
        
        self.__data = data # convendria hacer un diccionario? 
        self.__instruments = instruments
        self.__graphics = graphics 
        self.__name = name 


    @property
    def data(self):
    	return self.__data
     
    @property
    def name(self):
        return self.__name

    @property
    def instruments(self):
        return self.__instruments

    @property
    def graphics(self):
        return self. graphics
    


    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value  
        else:
            return TypeError('Name must be str')

    def add_data(self, data):

        if isinstance(data, dataset.Dataset):

            self.__data.append(data) 
        

    def add_instrument(self):
    	pass 

    def add_graphics(self):
    	pass 

    def set_name(self):
    	pass 

        
