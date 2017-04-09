from girl import Girl
from boy import Boy
from gift import Gift
from miserBoy import Miser
from generousBoy import Generous
from geekBoy import Geek
from desperateGirl import Desperate
from normalGirl import Normal
from choosyGirl import Choosy
from luxuryGift import Luxury
from essentialGift import Essential
from utilityGift import Utility
from random import randint
from generate import generator
from logger import logger
import csv

def calGift(girl,boy,gift):

	'returns gift list for a particular couple'
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

	"calculates girl's hapiness"
	if(girl.types == 'Choosy'):
		girl.happinessChoosy(gift)
	if(girl.types == 'Normal'):
		girl.happinessNormal(gift)
	if(girl.types == 'Desperate'):
		girl.happinessDesperate(gift)

def calBoyHappiness(girl,boy,gift) :

	"calculate boy's happiness"
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
B = []
G = []
gift = []

for row in readBoy :
	if(row[5] == 'Miser'):
		 B.append(Miser(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]))
	elif(row[5] == 'Generous'):
		 B.append(Generous(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]))
	elif(row[5] == 'Geeks'):
		 B.append(Geek(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]))

for row in readGirl :
	if(row[4] == 'Normal'):
		G.append(Normal(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]))
	elif(row[4] == 'Desperate'):
		G.append(Desperate(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]))
	elif(row[4] == 'Choosy'):
		G.append(Choosy(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]))

for row in readGift :

	if(row[3] == 'Essential'):
		gift.append(Essential(row[0],int(row[1]),int(row[2]),row[3]))
	elif(row[3] == 'Utility'):
		gift.append(Utility(row[0],int(row[1]),int(row[2]),row[3],row[4],row[5]))
	else :
		gift.append(Luxury(row[0],int(row[1]),int(row[2]),row[3],row[4],row[5]))

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
			logger(' commitment : ' + g.name + " and " + b.name)
			setattr(b,b.gfname,g.name)
			setattr(g,g.bfname,b.name)
			giftlist = calGift(g,b,gift)
			logger(' gifting :) : ' + b.name + ' ----->> ' + g.name + ' ' + ' '.join([i.name for i in giftlist]))
			calGirlHappiness(g,giftlist)
			calBoyHappiness(b,g,giftlist)
			coupleCompat = b.budget- g.main_budget + abs(b.attr_rating - g.attr_rating) + abs(g.intel_level - b.intel_level)
			coupleHappiness = float(b.happiness) + float(g.happiness)		
			C += [(b,g,giftlist,coupleHappiness,coupleCompat)]
			break

k = randint(0,count)
C = sorted(C,key = lambda x : x[3], reverse = True)
breakUp = []
print '------------------------------------------'
logger('***************************************************')
for i in range(0,k) :
	breakUp.append((C[0][1],C[0][0]))
	print("OOPs !!! break up between"  + C[0][1].name +" and " + C[0][0].name)
	logger("Break UP :(  :"  + C[0][1].name +" and " + C[0][0].name)
	C[0][1].changeStatus()
	C[0][0].changeStatus()
	C.pop(0)

logger(' *************************************************')
count -= k
for g in breakUp :
	for b in  B:
		
		#print ("Trying  match :" + g.name + " with " + b.name)
		if(g[0].isElligible(b) and b.isElligible(g[0]) and b != g[1]):
			count += 1
			print(" New Couple " + " GirlFriend : " + g[0].name + ", BoyFriend : " + b.name)
			g[0].changeStatus()
			b.changeStatus()
			logger(' commitment : ' + g[0].name + " and " + b.name)
			setattr(b,b.gfname,g[0].name)
			setattr(g[0],g[0].bfname,b.name)
			giftlist = calGift(g[0],b,gift)
			logger(' gifting :) : ' + b.name + ' ----->> ' + g[0].name + ' ' + ' '.join([i.name for i in giftlist]))
			calGirlHappiness(g[0],giftlist)
			calBoyHappiness(b,g[0],giftlist)
			coupleCompat = b.budget- g[0].main_budget + abs(b.attr_rating - g[0].attr_rating) + abs(g[0].intel_level - b.intel_level)
			coupleHappiness = float(b.happiness) + float(g[0].happiness)		
			C += [(b,g[0],giftlist,coupleHappiness,coupleCompat)]
			break
logger('*********************************************************')
