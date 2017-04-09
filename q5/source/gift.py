class Gift :

	'defines a gift'
	name = ''
	"""@ivar: name of gift"""
	price = 0
	"""@ivar: price of gift"""
	value = 0
	"""@ivar: value of gift"""
	types = ''
	"""@ivar: type of gift."""
	def __init__(self,name,price,value,types):
		'initialises attributes of Gift class'
		self.name = name
		self.price = price
		self.value = value
		self.types = types

