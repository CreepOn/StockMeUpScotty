import os
from markets import *
import json
from loadDataFunctions import *
import numpy as np
from stockIndicators import *
from plots import *
from dataobject import *
os.system('clear')


#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#printRawData(data)

listdata=dataobject('raw', JsonToMatrix(getHistoricalData('TSLA', 10)))

print listdata
print listdata.data[:,2]
#listdata=JsonToList(getHistoricalData('TSLA', 15))


#filtered=SMA(listdata,50)
#print "----------------------------------------------------"

#CandleStickPlotting(filtered)
#CandleStickPlotting(listdata)

#CandleStickPlotting(listdata)

