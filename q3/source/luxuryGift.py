from gift import Gift

class Luxury(Gift) :
	'defines a luxury gift'

	luxrating = 0
	"""@ivar: luxury rating."""
	diff = 0
	"""@ivar: difficulty to obtain gift."""
	def __init__(self,name,price,value,types,luxrating,diff):
		'initialises attributes of Luxury class'
		Gift.__init__(self,name,price,value,types)
		self.luxrating = luxrating
		self.diff = diff