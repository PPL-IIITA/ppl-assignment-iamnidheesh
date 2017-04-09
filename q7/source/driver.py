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
from bisect import bisect_left
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

def findGirl1(b,BG) :
	"algo 1 : find girl for a particular boy"	
	flag = 0
	girl = ''
	for i in BG :
		if( b == i[0]) :
			flag = 1
			girl = i[1]
			break
	if(flag == 0) :
		print( b  + " is not commited")
	else :
		print( b + " is commited to " + girl)

def findGirl2(x, a):
    "algo 2 (binary search) : find girl for a particular boy"
    hi = len(a)
    pos = bisect_left(a, x, 0, hi)  
    return (pos if pos != hi and a[pos] == x else -1)

def findGirl3(b,hashtable) :
	"algo 3 (hash) : find girl for a particular boy"
	if( hash(b) in hashtable) :
		print (b + " is commited to " + hashtable[hash(b)])
	else :
		print b + " is not commited"

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
			logger(' gifting : ' + b.name + ' ----->> ' + g.name + ' ' + ' '.join([i.name for i in giftlist]))
			calGirlHappiness(g,giftlist)
			calBoyHappiness(b,g,giftlist)
			coupleCompat = b.budget- g.main_budget + abs(b.attr_rating - g.attr_rating) + abs(g.intel_level - b.intel_level)
			coupleHappiness = float(b.happiness) + float(g.happiness)		
			C += [(b,g,giftlist,coupleHappiness,coupleCompat)]
			break
print('Choosing random choice of implementaion (1-3) :)')
choice = randint(1,3)
print("choice = " + str(choice))
k = randint(1,count)
boys = ['Boy' +str(i) for i in range(0,k+1)]
BG = [(i[0].name,i[1].name) for i in C]

bins_bg = sorted([i[0] for i in BG] , key = lambda x : x[0])

hashtable = {}
for c in C :
	hashtable.update({hash(c[0].name) : c[1].name})


for b in boys :

	if( choice == 1) :
		findGirl1(b,BG)
	if(choice == 2) :
		pos = findGirl2(b,bins_bg)
		if(pos != -1) :
			print(b + " is commited to " + BG[pos][1])
		else:
			print(b + " is not commited")
	if(choice == 3) :
			findGirl3(b,hashtable)

