import os
from markets import *
import json
from loadDataFunctions import *
import numpy as np
from stockIndicators import *
from plots import *
from dataobject import *
os.system('clear')

def SMA(obj, timeFrame):
	returnlist=[]
	datalist=[]
	if isinstance(obj, dataobject):
		if obj.category == "raw" or obj.category == "candlestick":
			datalist=obj.data[:,2].transpose().tolist()[0]			
		else:
			datalist=obj.data[:,2].transpose().tolist()[0]
		
		returnlist=movingAverage(datalist, timeFrame)
		returnmatrix=np.concatenate((obj.data[(timeFrame-2):-1,0], np.matrix(returnlist).transpose()),axis=1)
		
		return dataobject('mov avg', returnmatrix)
	else:
		print "Data is not of type 'dataobject'"

#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#printRawData(data)

#listdata=dataobject('raw', JsonToMatrix(getHistoricalData('TSLA', 10)))
listdata=dataobject('raw', np.matrix([[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]))

print isinstance(listdata, dataobject)
print listdata.data[:,2]
#listdata=JsonToList(getHistoricalData('TSLA', 15))


print SMA(listdata,3)
#filtered=SMA(listdata,50)
#print "----------------------------------------------------"

#CandleStickPlotting(filtered)
#CandleStickPlotting(listdata)

#CandleStickPlotting(listdata)

