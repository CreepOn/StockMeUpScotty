import os
from markets import *
#import json
from loadDataFunctions import *
import numpy as np
from stockIndicators_emil import *
from plots import *
from dataobject import *
from pylab import *

whiteFont="\033[0m"
greenFont="\033[92m"
redFont="\033[91m"

os.system('clear')

def movAveAna(obj, slowMovDays, fastMovDays):
	startup=0
	try:
		slow=SMA(obj, slowMovDays)
		startup+=1
	except:
		print redFont+"History not long enough for slow window."+whiteFont
	try:
		fast=EMA(obj, fastMovDays)#SMA(obj, fastMovDays)
		startup+=1
	except:
		print redFont+ "History not long enough for fast window"+whiteFont
	if startup==2:
		lendiff=len(fast.data)-len(slow.data)
		diff=[];
		goldenCross=[];
		deathCross=[];
		for i in range(0,len(slow.data)):
			if slow.data[i,0]==fast.data[lendiff+i,0]:
				diff.append([slow.data[i,0],slow.data[i,1]-fast.data[lendiff+i,1]])
		diff=np.matrix(diff)
		for i in range(0,len(diff)-1):
			if diff[i,1]*diff[i+1,1]<0:
				if diff[i,1]<0:
					goldenCross.append(diff[i+1, 0].tolist())
				elif diff[i+1,1]<0:
					deathCross.append(diff[i, 0].tolist())
		return np.matrix(goldenCross), np.matrix(deathCross), dataobject(obj.ticker, 'diff', np.matrix(diff))
	return np.matrix([]), np.matrix([]), dataobject(obj.ticker, 'diff', np.matrix([]))
					


#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#printRawData(data)

#ticker='DENERG.CO'

tickers=get_C20()
for i in range(0,len(tickers)):
	listdata=dataobject(tickers[i], 'raw', JsonToMatrix(getHistoricalData(tickers[i],400)))

	gc,dc,df=movAveAna(listdata,200,50)

	print "           "+'-'*(len(df.ticker) +4)
	print "           "+"| " + str(df.ticker) + " |"
	print "           "+'-'*(len(df.ticker) +4)

	if len(gc.tolist())>0:
		print "golden cross: "
		for ele in gc:
			try:
				hel=int(ele)
				print str(num2date(int(hel)))
			except:
				print "empty"
	if len(dc)>0:
		
		print "death cross: "
		for ele in dc:
			try:
				hel=int(ele)
				print str(num2date(int(hel)))
			except:
				print "empty"
	print "---------------------------------------"

