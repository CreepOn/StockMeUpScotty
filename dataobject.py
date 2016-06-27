import numpy as np
from datetime import datetime
from datetime import date
import time

class dataobject:
	def __repr__(self):
		return self.category
	def __str__(self):
		return "ticker: "+ self.ticker +  "\ncategory: " + self.category + '\ndescription: ' + str(list(self.description)) + '\ndata: ' + str(self.data)
		
	def __init__(self, Ticker, Category):
		self.ticker = Ticker
		self.category=Category
		self.description = self.get_description(Category)		
		self.data = np.matrix([])
	
	def __init__(self, Ticker, Category, mat):
		self.ticker = Ticker
		self.category=Category
		self.description = self.get_description(Category)		
		self.data = mat
		self.log = ""
		
	def get_description(self, cat):
		choose={'tr': '1','asi': '1', 'rsi': '1', 'mov avg': '1', 'exp mov avg':'1', 'aroon-oscillator': '1', 'volume': '1',
						'aroon': '2',
						'Yet to be defined!!!': '3',
						'candlestick':'4',
						'raw': '4',
						'sto osc': '5'}
		chosen_desription={'0':{'Category is unknown'},
											'1':{'time, filter-output'},
											'2':{'time, aroon-up, aroon-down'},
											'3':{'time, Open, Close, High, Low'},
											'4':{'time, Open, Close, High, Low, Volume'},
											'5':{'time, fast, slow'}}
		val='0'
		try:
			val=choose[cat]
		except KeyError: 
			pass	
		return chosen_desription[val]
