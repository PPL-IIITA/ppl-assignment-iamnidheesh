from girl import Girl
from boy import Boy
from generate import generator
import csv
from logger import logger

generator()
boycsv = open('boy.csv')
girlcsv = open('girl.csv')
readBoy = csv.reader(boycsv, delimiter = ',')
readGirl = csv.reader(girlcsv, delimiter = ',')
B = [ Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5]) for row in readBoy]
G = [ Girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]) for row in readGirl]
for g in  G:
	for b in  B:
		
		if(g.isElligible(b) and b.isElligible(g)):

			print("GirlFriend : " + g.name + ", BoyFriend : " + b.name)
			g.changeStatus()
			b.changeStatus()
			logger(' commitment : ' + g.name + " and " + b.name)
			setattr(g,g.bfname,b.name)
			setattr(b,b.gfname,g.name)
			break

