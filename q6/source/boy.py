class Boy:

	'defines a Boy'
	
	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement,types):

		'initialises attributes of Boy class'

		self.name = name
		"""@ivar: name of boy."""
		self.attr_rating = attr_rating
		"""@ivar: attractivness rating of boy."""
		self.budget  = budget
		"""@ivar: boy budget."""
		self.intel_level = intel_level
		"""@ivar: intelligence level of boy."""
		self.attr_requirement = attr_requirement
		"""@ivar: attractivness requirement of boy."""
		self.status = 's'
		"""@ivar: status of boy ( single or committed)."""
		self.gfname = ''
		"""@ivar: girl friend name"""
		self.happiness = 0
		"""@ivar: happiness of boy."""
		self.types = types
		"""@ivar: type of boy."""

	def isElligible(self,girl):

		'test if a girl is elligible for a particular boy'
		flag = True
		if(self.budget < girl.main_budget):

			flag = False
			#print(self.name + " will not date " + girl.name)

		if(self.attr_requirement > girl.attr_rating):

			flag = False
			#print(girl.name + ' does not meet attractiveness requirement for ' + self.name)

		if(self.status == 'c'):

			flag = False
			#print(self.name + ' is already commited')

		return flag

	def checkStatus(self):

		'check status of a boy'

		return self.status

	def changeStatus(self):

		'changes status of a girl'
		
		if(self.status == 's') :
			self.status = 'c'
		else :
			self.status = 's'	
