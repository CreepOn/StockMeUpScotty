import numpy as np

class dataobject:
	def __repr__(self):
		return self.category
	def __str__(self):
		return "category: " + self.category + '\ndescription: ' + str(list(self.description)) + '\ndata: ' + str(self.data)
	def __init__(self, Category):
		self.category=Category
		self.description = self.get_description(Category)		
		self.data = np.matrix([])
	
	def __init__(self, Category, mat):
		self.category=Category
		self.description = self.get_description(Category)		
		self.data = mat
		self.log = ""
		
	def get_description(self, cat):
		choose={'rsi': '1', 'mov avg': '1', 'exp mov avg':'1', 'aroon-oscillator': '1', 'volume': '1',
						'aroon': '2', 
						'candlestick':'3',
						'raw': '4'}
		chosen_desription={'0':{'Category is unknown'},
											'1':{'time', 'filter-output'},
											'2':{'time', 'aroon-up', 'aroon-down'},
											'3':{'time', 'Open', 'Close', 'High', 'Low'},
											'4':{'time', 'Open', 'Close', 'High', 'Low', 'Volume'}}
		val='0'
		try:
			val=choose[cat]
		except KeyError: 
			pass	
		return chosen_desription[val]
