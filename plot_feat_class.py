class Plot_feature:
	def __init__(self):
		self.ave_count = 0
		self.candle_count = 0

	def avex(self):
		self.ave_count+=1
	
	def candlex(self):
		self.candle_count+=1

	def plot_get(self, *args):
		for i in args:
			switcher = {'ave': self.avex, 'candle': self.candlex}
			switcher[i]()
