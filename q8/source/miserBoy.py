from boy import Boy

class Miser(Boy):

	'defines miser boy'

	def __init__(self,name,attr_rating,budget,intel_level,attr_requirement,types):

		Boy.__init__(self,name,attr_rating,budget,intel_level,attr_requirement,types)

	def giftMiser1(self,girl,gift) :


		"algo 1 : calculates returns gifts that a miser boy will give"
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

	def giftMiser2(self,girl,gift):
		
		"algo 2 :calculates returns gifts that a miser boy will give"
		s = 0
		g = []
		fu = False
		fe = False
		fl = False
		for i in gift :
			if(i.types == 'Utility' and not fg) :
				g.append(i)
				fg = not fg
			if(i.types == 'Luxury' and not fl) :
				g.append(i)
				fl = not fl
			if(i.types == 'Essential' and  not fe) :
				g.append(i)
				fe = not fe
		for i in gift:
			if(s < girl.main_budget and i not in g):
				s += i.price
				g += [i]
			else:
				break
		self.budget = max(self.budget,s)
		return g	