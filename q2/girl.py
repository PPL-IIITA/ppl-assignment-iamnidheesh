from math import log,exp

class Girl:
	
	'defines a girl'
	
	girl_number = 0

	def __init__(self,name,attr_rating,main_budget,intel_level,types):

		'intialises attributes'
		self.name = name
		self.attr_rating = attr_rating
		self.main_budget = main_budget
		self.intel_level = intel_level
		self.status = 's'
		self.bfname = ''
		self.happiness = 0
		self.types = types


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

	def happinessChoosy(self,gift):

		s_gift = sum([i.price+2*i.value if (i.types == 'Luxury') else i.price+i.value
				 for i in gift]) 
		if(s_gift > self.main_budget):
			self.happiness = log(s_gift - self.main_budget)
		else:
			self.happiness = 0

	def happinessNormal(self,gift):

		self.happiness = max(0,sum([(i.price + i.value) 
						for i in gift]) - self.main_budget) 

	def happinessDesperate(self,gift):

		self.happiness = max(0,int(exp(sum([i.price for i in gift]))) - self.main_budget)
