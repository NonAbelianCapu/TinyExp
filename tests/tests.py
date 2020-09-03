import core.measure as measure
import core.dataset as dataset

import unittest
import numpy as np 



class MeasureTesting(unittest.TestCase):

	
	def setUp(self):
	
		self.data_1 = [x for x in np.random.rand(1000)]
		self.measures_1 = [measure.Measure(x,x/10, unit='kg', instrument='pesa') for x in self.data_1]

		self.data_2 = [x for x in np.random.rand(1000)]
		self.measures_2 = [measure.Measure(x,x/10, unit='kg', instrument='pesa') for x in self.data_2]


	def test_sum(self):
		
		sum_12 = [x + y for (x,y) in zip(self.data_1, self.data_2)]
		sum_12_measures = [x + y for (x,y) in zip([x.value for x in self.measures_1], 
												  [x.value for x in self.measures_2])]

		sum_pairs = [(x,y) for (x,y) in zip(sum_12,sum_12_measures)]
		
		for pair in sum_pairs:
			s,m = pair[0], pair[1]

			self.assertEqual(pair[0],pair[1])



	def test_product(self):
		
		prod_12 = [x*y for (x,y) in zip(self.data_1, self.data_2)]
		prod_12_measures = [x*y for (x,y) in zip([x.value for x in self.measures_1], 
												  [x.value for x in self.measures_2])]

		prod_pairs = [(x,y) for (x,y) in zip(prod_12, prod_12_measures)]
		
		for pair in prod_pairs:
			s,m = pair[0], pair[1]

			self.assertEqual(pair[0],pair[1])


	def test_truediv(self):
		
		div_12 = [x/y for (x,y) in zip(self.data_1, self.data_2)]
		div_12_measures = [x/y for (x,y) in zip([x.value for x in self.measures_1], 
												  [x.value for x in self.measures_2])]

		div_pairs = [(x,y) for (x,y) in zip(div_12, div_12_measures)]
		
		for pair in div_pairs:
			s,m = pair[0], pair[1]

			self.assertEqual(pair[0],pair[1])


	def test_ord(self):

		zip_12 = [(x,y) for (x,y) in zip(self.data_1, self.data_2)]
		ord_12 = []

		for p in zip_12:

			if p[0] <= p[1]:
				ord_12.append('less')

			elif p[0] == p[1]:
				ord_12.append('eq')

			elif p[0] >=  p[1]:
				ord_12.append('gr')








if __name__ == '__main__':
	
	unittest.main()