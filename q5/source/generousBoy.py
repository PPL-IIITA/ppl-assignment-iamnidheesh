from boy import Boy

class Generous(Boy):

	'defines generous boy'

	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement,types):
		'initialises attributes of Generous class'
		Boy.__init__(self,name,attr_rating,budget,intel_level,attr_requirement,types)

	def giftGenerous(self,girl,gift):
		
		"calculates returns gifts that a generous boy will give"
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
	