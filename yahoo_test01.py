import os
from markets import *
#import json
from loadDataFunctions import *
import numpy as np
from stockIndicators_emil import *
from plots import *
from dataobject import *
os.system('clear')

def movAveAna(obj, slowMovDays, fastMovDays):
	slow=SMA(obj, slowMovDays)
	fast=SMA(obj, fastMovDays)
	
	lendiff=len(fast.data)-len(slow.data)
	diff=[];
	goldenCross=[];
	deathCross=[];
	for i in range(0,len(slow.data)):
		if slow.data[i,0]==fast.data[lendiff+i,0]:
			diff.append([slow.data[i,0],slow.data[i,1]-fast.data[lendiff+i,1]])
	print np.diff(np.matrix(diff)[:,1][0])
	#return dataobject(obj.ticker, 'diff', np.matrix(diff))
					


#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#printRawData(data)

ticker='TSLA'

listdata=dataobject(ticker, 'raw', JsonToMatrix(getHistoricalData(ticker,50)))
#print listdata

#ema=EMA(listdata,11)

movAveAna(listdata,20,5)


#print ema.data[:,1]
