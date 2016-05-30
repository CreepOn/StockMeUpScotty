import os
from markets import *
import json
from loadDataFunctions import *
import numpy as np
from stockIndicators import *
from plots import *
os.system('clear')

def SMA(listdata, samples):
	sma=listdata[(samples-1):,0]
	#i=0
	#while i<5:
	#	temp=movingAverage(map(float, listdata[0:,i]),samples)
	#	i+=1
	#	sma=[sma,array(temp)]
	return sma

#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#	printRawData(data)
	
data=getHistoricalData('TSLA', 365)

listdata=matrix(JsonToList(data))

#print listdata[0:,0]

sma=movingAverage(map(float, listdata[0:,1]),10)

print SMA(listdata,5)

#CandleStickPlotting(SMA(listdata,5))
