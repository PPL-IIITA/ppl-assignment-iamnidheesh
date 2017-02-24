from random import randint
import csv

def writeToCsv(Data,filename):
	csv_file = open(filename,'wb')
	Writer = csv.writer(csv_file, delimiter=',') 
	for line in Data:
		Writer.writerow(line)


tb = ['Miser','Generous','Geeks']
tg = ['Choosy','Normal','Desperate']
gift = ['Essential','Luxury','Utiltiy']

boyData = [('Boy'+ str(i),randint(0,100),randint(0,2000),randint(0,100),randint(0,100),tb[randint(0,2)])
			for i in range(0,30)]

girlData = [('Girl'+ str(i),randint(0,100),randint(0,2000),randint(0,100),tg[randint(0,2)])
			for i in range(0,15)]

giftData = [('Gift'+ str(i),randint(0,100),randint(0,100),gift[randint(0,2)])
			for i in range(0,10)]

writeToCsv(boyData,'boy.csv')
writeToCsv(girlData,'girl.csv')
writeToCsv(giftData,'gift.csv')


