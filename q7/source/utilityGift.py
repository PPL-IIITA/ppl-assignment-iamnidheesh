from gift import Gift

class Utility(Gift) :
	'defines a Utility gift'
	utilclass = 0
	"""@ivar: utility class."""
	utilval = 0;
	"""@ivar: utility value."""
	def __init__(self,name,price,value,types,utilval,utilclass):
		'initialises attributes of Utility class'
		Gift.__init__(self,name,price,value,types)
		self.utilval = utilval
		self.utilclass = utilclass
