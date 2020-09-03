import dataset
import measure


def check_types(data):

	if (isinstance(data, [measure.Measure, dataset.Dataset]) or np.isscalar(data)):
		return (True, type(data)) 



def arccos(data):

	if check_types(data)[0]:
		continue
	else:
		raise TypeError('')


def arcsin(data):

	if check_types:
		continue
	else:
		raise TypeError('')
	

def sin(data):

	if check_types:
		continue
	else:
		raise TypeError('')


def cos(data):

	if check_types:
		continue
	else:
		raise TypeError('')



def tan(data):

	if check_types:
		continue
	else:
		raise TypeError('')

def exp(data):

	if check_types:
		continue
	else:
		raise TypeError('')


# toma un measure o un dataset y lo manda a dos arrays 

def to_arrays(obj):
	pass 