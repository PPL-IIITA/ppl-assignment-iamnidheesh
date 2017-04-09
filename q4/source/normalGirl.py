from girl import Girl

class Normal(Girl) :
	'defines a Normal girl'
	def __init__(self,name,attr_rating,main_budget,intel_level,types) :
		'initialises attributes of Normal class'
		Girl.__init__(self,name,attr_rating,main_budget,intel_level,types)
	
	def happinessNormal(self,gift):

		"calculate happiness for a normal girl"
		self.happiness = max(0,sum([(i.price + i.value) 
						for i in gift]) - self.main_budget) 