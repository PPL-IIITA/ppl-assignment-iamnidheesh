from girl import Girl
from boy import Boy
from gift import Gift
from random import randint
from generate import generator
import csv

def calGift(girl,boy,gift):

	gift = sorted(gift,key = lambda x : x.price)
	g = []
	if(boy.types == 'Miser'):
		g = boy.giftMiser(girl,gift)
	if(boy.types == 'Generous'):
		g = boy.giftGenerous(girl,gift)
	if(boy.types == 'Geeks'):
		g = boy.giftGeeks(girl,gift)
	return g

def calGirlHappiness(girl,gift):

	if(girl.types == 'Choosy'):
		girl.happinessChoosy(gift)
	if(girl.types == 'Normal'):
		girl.happinessNormal(gift)
	if(girl.types == 'Desperate'):
		girl.happinessDesperate(gift)

def calBoyHappiness(girl,boy,gift) :

	if(boy.types == 'Miser'):
		setattr(boy,boy.happiness,boy.budget - sum([i.price for i in gift]))
	if(boy.types == 'Generous'):
		setattr(boy,boy.happiness,girl.happiness)
	if(boy.types == 'Geeks'):	
		setattr(boy,boy.happiness,girl.intel_level)	

generator()
boycsv = open('boy.csv')
girlcsv = open('girl.csv')
giftcsv = open('gift.csv')
readBoy = csv.reader(boycsv, delimiter = ',')
readGirl = csv.reader(girlcsv, delimiter = ',')
readGift = csv.reader(giftcsv, delimiter = ',')
B = [ Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5])
	 for row in readBoy]
G = [ Girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4])
	 for row in readGirl]
gift = [ Gift(row[0],int(row[1]),int(row[2]),row[3])
	 for row in readGift]
C = []
count = 0
for g in  G:
	for b in  B:
		
		#print ("Trying  match :" + g.name + " with " + b.name)
		if(g.isElligible(b) and b.isElligible(g)):
			count += 1
			print("GirlFriend : " + g.name + ", BoyFriend : " + b.name)
			g.changeStatus()
			b.changeStatus()
			setattr(b,b.gfname,g.name)
			setattr(g,g.bfname,b.name)
			giftlist = calGift(g,b,gift)
			calGirlHappiness(g,giftlist)
			calBoyHappiness(b,g,giftlist)
			coupleCompat = b.budget- g.main_budget + abs(b.attr_rating - g.attr_rating) + abs(g.intel_level - b.intel_level)
			coupleHappiness = float(b.happiness) + float(g.happiness)		
			C += [(b,g,giftlist,coupleHappiness,coupleCompat)]
			break

k = randint(0,count)
C = sorted(C,key = lambda x : x[3], reverse =True)
print '------------------------------------------'
for c in C[0:k] :
	print 'GF : ' + c[1].name + ' BF : ' + c[0].name + ' happiness ' + str(c[3])
C = sorted(C,key = lambda x : x[4],reverse = True)
print '------------------------------------------'
for c in C[0:k] :
	print 'GF : ' + c[1].name + ' BF : ' + c[0].name + ' compatibility ' + str(c[4])
print '------------------------------------------'
for c in C:
	print c[1].name + " Gifted " + c[0].name + " ---->>>>"
	for g in c[2]:
		print g.name + ' ',
	print '\n***********\n'