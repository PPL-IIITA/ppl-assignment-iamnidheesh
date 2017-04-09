from boy import Boy

class Generous(Boy):

	'defines generous boy'

	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement,types):

		Boy.__init__(self,name,attr_rating,budget,intel_level,attr_requirement,types)

	def giftGenerous1(self,girl,gift):
		
		"algo 1: calculates returns gifts that a generous boy will give"
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
	
	def giftGenerous2(self,girl,gift) :

		"algo 2 :calculates returns gifts that a generous boy will give"
		s = 0
		g = []
		fu = False
		fe = False
		fl = False
		for i in gift :
			if(i.types == 'Utility' and  not fg) :
				g.append(i)
				fg = not fg

			if(i.types == 'Luxury' and not fl) :
				g.append(i)
				fl = not fl
			if(i.types == 'Essential' and  not fe) :
				g.append(i)
				fe = not fe

		flag = False
		for i in gift:
				if((s + i.price <= self.budget) and (i not in g)):
					s += i.price
					g += [i]
					flag = True
				else:
					break
		if(not flag):
			self.budget = gift[0].price
			g = g + [gift[0]]
		return g