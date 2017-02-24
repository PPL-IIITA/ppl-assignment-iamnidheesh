from girl import Girl
from boy import Boy
import csv

boycsv = open('boy.csv')
girlcsv = open('girl.csv')
readBoy = csv.reader(boycsv, delimiter = ',')
readGirl = csv.reader(girlcsv, delimiter = ',')
B = [ Boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[4]) for row in readBoy]
G = [ Girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]) for row in readGirl]
for g in  G:
	for b in  B:
		
		#print ("Trying  match :" + g.name + " with " + b.name)
		if(g.isElligible(b) and b.isElligible(g)):

			print("GirlFriend : " + g.name + ", BoyFriend : " + b.name)
			g.changeStatus()
			b.changeStatus()
			setattr(g,g.bfname,b.name)
			setattr(b,b.gfname,g.name)
			break

