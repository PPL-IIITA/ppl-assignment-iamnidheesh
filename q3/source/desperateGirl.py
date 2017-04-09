from girl import Girl
from math import exp

class Desperate(Girl) :
	'defines a Desperate girl'
	def __init__(self,name,attr_rating,main_budget,intel_level,types) :
		'initialises attributes of Desperate class'
		Girl.__init__(self,name,attr_rating,main_budget,intel_level,types)
	
	def happinessDesperate(self,gift):

		"calculate happiness for a desperate girl"
		self.happiness = max(0,int(exp(sum([i.price for i in gift]))) - self.main_budget)