import os
from markets import *
import json
from loadDataFunctions import *
import numpy as np
from stockIndicators import *
os.system('clear')

#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#	printRawData(data)
	
data=getHistoricalData('TSLA', 365)

listdata=matrix(JsonToList(data))

#print listdata[0:,0]
sma=movingAverage(map(float, listdata[0:,1]),10)

print "list: " + str(len(listdata)) + "  SMA: " + str(len(sma))

#CandleStickPlotting(listdata)
