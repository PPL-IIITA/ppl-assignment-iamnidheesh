from gift import Gift

class Essential(Gift) :
	'defines Essential gift'
	def __init__(self,name,price,value,types):
		'initialises attributes of Essential class'
		Gift.__init__(self,name,price,value,types)