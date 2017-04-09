from gift import Gift

class Luxury(Gift) :
	'defines a luxury gift'
	
	def __init__(self,name,price,value,types,luxrating,diff):
		'initialises attributes of Luxury class'
		Gift.__init__(self,name,price,value,types)
		self.luxrating = luxrating
		"""@ivar: luxury rating."""
		self.diff = diff
		"""@ivar: difficulty to obtain gift."""