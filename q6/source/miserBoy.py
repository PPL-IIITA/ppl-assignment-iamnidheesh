from boy import Boy

class Miser(Boy):

	'defines miser boy'

	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement,types):
		'initialises attributes of Boy class'
		Boy.__init__(self,name,attr_rating,budget,intel_level,attr_requirement,types)

	def giftMiser(self,girl,gift):
		
		"calculates returns gifts that a miser boy will give"
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