from collections.abc import Iterable
from tabulate import tabulate

import measure
import enums 
import numpy as np 
import matplotlib.pyplot as plt 

class Dataset:

    def __init__(self, data=None, unit=None, instrument=None , name = None, error_dist='gaussian'):

        self.__data = [] 

      

        if not unit: 
            self.__unit = enums.Units.default 
        else: 
            self.__unit = unit 
        
        if not instrument: 
            self.__instrument = 'default_instrument' 
        else: 
            self.__instrument = instrument
        
        if not name: 
            self.__name = 'default_name'
        else:
            self.__name = name                    # esto va a haber que corregirlo sacarlo del pool de experimetno

        
        if isinstance(self.__data, Iterable):

            
            for d in data:

                data_type = type(d)


                if data_type == measure.Measure:
                    self.__data.append(d)
                
                elif (data_type == tuple and len(d) == 2):
                    self.__data.append(measure.Measure(d[0], d[1], self.__unit, self.__instrument, self.__name))

                elif (data_type == list and len(d) == 2):
                    self.__data.append(measure.Measure(d[0], d[1], self.__unit, self.__instrument, self.__name))

                elif np.isscalar(d):
                    self.__data.append(measure.Measure(d[0],0, self.__unit, self.__instrument, self.__name))

        else:

            raise TypeError('object is not Iterable')



        self.__size = len(self.__data)




        """ 

        No olvidarme de chequear el tema de como manejar los intrumentos
        las unidades y que no haya colisiones, avisar al user que esta usando
        dos cosas al mimso timepo


        """



        """ 
        Overloadeamos las operaciones basicas como hicimos en Measure
        ahora basta con hacer chequeos basicos ya que el trabaojo esta
        hecho en Measure. 
        
        """


    @property
    def unit(self):
        return self.__unit

    @property
    def name(self):
        return self.__name
    
    @property
    def instrument(self):
        return self.__instrument

    @property
    def values(self):

        values = [x.value for x in self.__data]

        return values 

    @property
    def errors(self):
        
        values = [x.value for x in self.__data]

        return values

    @property
    def size(self):
        return self.__size


    @unit.setter
    def unit(self):
        return self.__unit

    @name.setter
    def name(self):
        return self.__name
    
    @instrument.setter 
    def instrument(self):
        return self.__instrument

    @values.setter
    def values(self, idx):
        
        pass



    def __add__(self, other):

        if isinstance(Dataset, other):

            if self.__size == other.__size:
                temp_data = []

                for idx,data in enumerate(self.data):
                    temp_data.append(self.data[i] +  other.data[i])

            raise IndexError('Sizes of Datasets dont match')



    def __mul__(self, other):

        if isinstance(Dataset, other):
            
            if self.__size == other.__size:
                temp_data = []

                for idx,data in enumerate(self.data):
                    temp_data.append(self.data[i]*other.data[i])

            raise IndexError('Sizes of Datasets dont match')



    def __truediv__(self, other):
        
        if isinstance(Dataset, other):
            
            if self.__size == other.__size:
                temp_data = []

                for idx,data in enumerate(self.data):
                    
                    if other.data[i] != 0:
                        temp_data.append(self.data[i]/other.data[i])
                    else:
                        raise ZeroDivisionError('Denominator must be != 0')
            else:

                raise IndexError('Sizes of Datasets dont match')
        
        return Dataset(temp_data)

    def __getitem__(self, idx):

        if isinstance(idx,int):
            
            try:
                return self.__data[idx]
            except IndexError:
                raise IndexError('Index out of range')

        else:

            raise TypeError('Index must be integer ')



    def __setitem__(self, idx, value):

        if isinstance(idx,int):
            
            if isinstance(value, measure.Measure):

                try:
                    self.__data[i] == value

                except IndexError:
                    raise IndexError('Index out of range')

            else:

                raise TypeError('Value must be a measure object') # aflojar esto un poco para que puedan poner tuples, etc ... 

        else:

            raise TypeError('Index must be integer ')

        

    def __pow__(self, other):
        
        if np.isscalar(other):
            pass

        raise TypeError('Exponent must be a scalar')


    def pprint(self):

        print_table = tabulate([[i, x.value, x.error, x.unit, x.instrument] for (i,x) in enumerate(self.__data)],
                                headers = ['Values', 'Errors', 'Unit', 'instrument'], tablefmt="fancy_grid")

        print(print_table)


    def plot_data(self):

        x_plot = range(len(self.values()))
        y_plot = self.values()
        
        plt.title('Values')
        plt.xlabel('#')
        plt.ylabel(self.__name)
        plt.plot(x_plot, y_plot)
        plt.show()

        
        

    def plot_errors(self):
        
        x_plot = range(len(self.errors()))
        y_plot = self.errors()
        
        plt.title('Errors')
        plt.xlabel('#')
        plt.ylabel(self.__name)
        plt.plot(x_plot, y_plot)
        plt.show()

        


    def plot_data_dist(self, bins=False , normed=False):
        
        
        if self.__name:
            hist_name = self.__name
        else:
            hist_name = 'data_hist'

        if not bins:
            # estimo el numero de bins con la regla de Struge 
            hist_bins = int(round(1 + 3.322*np.log(self.__size)))
            print('hist_bins', hist_bins)

        else:

            hist_bins = bins

        if normed: 
            plt.ylabel('Probability')
            
        else:
            plt.ylabel('Counts')

        plt.title(self.__name)
        plt.hist(self.get_values(), bins = hist_bins)
        plt.show()

        

    def plot_error_dist(self, bins = False, normed=False):
        
        if self.__name:
            hist_name = self.__name
        else:
            hist_name = 'error_hist'

        if not bins:
            # estimo el numero de bins con la regla de Struge 
            hist_bins = int(round(1 + 3.322*np.log(self.__size)))

        else:

            hist_bins = bins

        if normed: 
            plt.ylabel('Probability')
        else:
            plt.ylabel('Counts')

        plt.title(self.__name)
        plt.hist(self.errors(), bins = hist_bins)
        plt.show()







