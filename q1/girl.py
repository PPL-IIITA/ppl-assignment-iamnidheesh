class Girl:
	
	'defines a girl'
	
	girl_number = 0
	status = 's'

	def __init__(self,name,attr_rating,main_bugdet,intel_level):

		'intialises attributes'
		self.name = name
		self.attr_rating = attr_rating
		self.main_bugdet = main_bugdet
		self.intel_level = intel_level

	def isElligible(self,boy):

		'test if a boy is elligible for a particular girl'
		
		if(self.main_bugdet > boy.budget):

			print(self.name + " will not date " + self.name)
			return 0

		else :

			return 1

	def checkStatus(self):

		'check status of a girl'

		return self.status

	def changeStatus(self):

		'changes status of a girl'
		
		if(self.status == 's') :
			self.status = 'c'
		else :
			self.status = 's'