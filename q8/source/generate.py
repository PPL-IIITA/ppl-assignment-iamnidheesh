from random import randint
import csv

def writeToCsv(Data,filename):
	' writes to a csv file'
	
	csv_file = open(filename,'wb')
	Writer = csv.writer(csv_file, delimiter=',') 
	for line in Data:
		Writer.writerow(line)

def generator():

	'generates random data to be written to csv file'
	
	tb = ['Miser','Generous','Geeks']
	tg = ['Choosy','Normal','Desperate']
	gift = ['Essential','Luxury','Utiltiy']

	boyData = [('Boy'+ str(i),randint(0,10),randint(0,200),randint(0,10),randint(0,10),tb[randint(0,2)])
				for i in range(0,30)]

	girlData = [('Girl'+ str(i),randint(0,10),randint(0,200),randint(0,10),tg[randint(0,2)])
				for i in range(0,15)]

	giftData = []
	for i in range(0,10) :
		giftType = gift[randint(0,2)]
		if(giftType == 'Essential') :
			giftData.append(('Gift'+ str(i),randint(0,10),randint(0,10),giftType))
		else :
			giftData.append(('Gift'+ str(i),randint(0,10),randint(0,10),giftType,randint(0,11),randint(0,11)))

	writeToCsv(boyData,'boy.csv')
	writeToCsv(girlData,'girl.csv')
	writeToCsv(giftData,'gift.csv')


