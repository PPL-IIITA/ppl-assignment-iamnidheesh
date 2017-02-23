class Boy:

	'defines a Boy'

	boy_number = 0
	status = 's'

	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement):

		'initialises attributes'

		self.name = name
		self.attr_rating = attr_rating
		self.budget  =budget
		self.intel_level = intel_level
		self.attr_requirement = attr_requirement

	def isElligible(self,girl):

		'test if a girl is elligible for a particular boy'
		flag = 1
		if(self.bugdet < girl.main_budget):

			flag = 0
			print(self.name + " will not date " + girl.name)

		if(self.attr_requirement > girl.attr_rating):

			flag = 0
			print(girl.name + 'does not meet attractiveness requirement for' + self.name)

		return flag

	def checkStatus(self):

		'check status of a boy'

		return self.status

	def changeStatus(self):

		'changes status of a girl'
		
		if(self.status == 's')
			self.status = 'c'
		else
			self.status = 's'
			