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
	i=1
	while i<5:
		temp=matrix(movingAverage(map(float, listdata[0:,i]),samples)).transpose()
		i+=1
		sma=np.c_[sma, array(temp)]
	listen=[]
	for ele in sma:
		listen.append(tuple(ele.tolist()[0]))
	return listen

#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#	printRawData(data)
	
data=getHistoricalData('TSLA', 365)

listdata=matrix(JsonToList(data))

#sma=movingAverage(map(float, listdata[0:,1]),10)


#sma=movingAverage(listdata.row(1),10)


#CandleStickPlotting(SMA(listdata,5))
CandleStickPlotting(listdata)
