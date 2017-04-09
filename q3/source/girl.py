class Girl:
	
	'defines a girl'

	def __init__(self,name,attr_rating,main_budget,intel_level,types):

		'intialises attributes'
		self.name = name
		"""@ivar: name of girl"""
		self.attr_rating = attr_rating
		"""@ivar: attractiveness rating."""
		self.main_budget = main_budget
		"""@ivar: maintainence budget."""
		self.intel_level = intel_level
		"""@ivar: intelligence level"""
		self.status = 's'
		"""@ivar: status of girl (single or committed."""
		self.bfname = ''
		"""@ivar: boyfriend name."""
		self.happiness = 0
		"""@ivar: happiness of girl"""
		self.types = types
		"""@ivar: type of girl."""


	def isElligible(self,boy):

		'test if a boy is elligible for a particular girl'
		
		flag = True
		if(self.main_budget > boy.budget):

			flag = False
			#print(self.name + " will not date " + boy.name)
			
		if (self.status == 'c'):

			flag = False
			#print(self.name + " is already commited")

		return flag

	def checkStatus(self):

		'check status of a girl'
		return self.status

	def changeStatus(self):

		'changes status of a girl'
		
		if(self.status == 's') :
			self.status = 'c'
		else :
			self.status = 's'
