from boy import Boy

class Geek(Boy):

	'defines geek boy'

	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement,types):
		'initialises attributes of Geek class'
		Boy.__init__(self,name,attr_rating,budget,intel_level,attr_requirement,types)

	def giftGeeks(self,girl,gift):

		"calculates returns gifts that a geek boy will give"
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
				if (i.types == 'Luxury') and ((self.budget - s) >= i.price) and (i not in g):
					s += i.price
					g += [i]
					break

		return g
