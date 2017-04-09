from girl import Girl
from math import log

class Choosy(Girl) :
	'defines a choosy girl'
	def __init__(self,name,attr_rating,main_budget,intel_level,types) :
		'initialises attributes of Choosy class'

		Girl.__init__(self,name,attr_rating,main_budget,intel_level,types)

	def happinessChoosy(self,gift):

		"calculate happiness for a choosy girl"
		s_gift = sum([i.price+2*i.value if (i.types == 'Luxury') else i.price+i.value
				 for i in gift]) 
		if(s_gift > self.main_budget):
			self.happiness = log(s_gift - self.main_budget)
		else:
			self.happiness = 0