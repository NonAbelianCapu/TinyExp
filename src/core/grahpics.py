import measure
import dataset
import enums 

class Plot:

    def __init__(self, x, y, name, g_type):


    	# agregar type checking a x e y y los enums para g_type 


        self.x = x
        self.y = y

        if not name:
			
			self.name = enums.PlotType.default
		
		elif isinstance(name, str):
			self.name = name

		else:
			raise TypeError('Types dont match')

        self.type = g_type

        self.__show_errors = True

        self.fig, self.ax = plt.subplots()



    def set_title(self):
    	pass 

    def set_xlabel(self):
    	pass 

    def set_ylabel(self):
    	pass


    def run(self):
    	pass 

    	# no se como carajo llamarle a la funcion es ta que plotee


    


