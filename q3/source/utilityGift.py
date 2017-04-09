from gift import Gift

class Utility(Gift) :
	'defines a Utility gift'
	def __init__(self,name,price,value,types,utilval,utilclass):
		'initialises attributes of Utility class'
		Gift.__init__(self,name,price,value,types)
		self.utilval = utilval
		"""@ivar: utility class."""
		self.utilclass = utilclass
		"""@ivar: utility value."""
