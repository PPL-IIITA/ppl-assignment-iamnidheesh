class Boy:

	'defines a Boy'

	boy_number = 0

	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement,types):

		'initialises attributes'

		self.name = name
		self.attr_rating = attr_rating
		self.budget  = budget
		self.intel_level = intel_level
		self.attr_requirement = attr_requirement
		self.status = 's'
		self.gfname = ''
		self.happiness = 0
		self.types = types

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
	
	def giftMiser(self,girl,gift):
	
		s = 0
		g = []
		for i in gift:
			if(s < girl.main_budget):
				s += i.price
				g += [i]
			else:
				break
		self.budget = max(self.budget,s)
		return g		

	def giftGenerous(self,girl,gift):
		
		s = 0
		g = []
		flag = False
		for i in gift:
				if(s + i.price <= self.budget):
					s += i.price
					g += [i]
					flag = True
				else:
					break
		if(not flag):
			self.budget = gift[0].price
			g = g + [gift[0]]
		return g
	
	def giftGeeks(self,girl,gift):

		s = 0
		g = []
		for i in gift:
			if(s < girl.main_budget):
				s += i.price
				g += [i]
			else:
				break
		self.budget = max(self.budget,s)
		
		if( s < self.budget):
			for i in gift:
				if (i.types == 'Luxury') and ((self.budget - s) >= i.price):
					s += i.price
					g += [i]
					break

		return g

