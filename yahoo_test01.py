import os
from markets import *
import json
from loadDataFunctions import *
import numpy as np
from stockIndicators import *
from plots import *
os.system('clear')

#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#	printRawData(data)

listdata=JsonToMatrix(getHistoricalData('TSLA', 15))

print listdata[:,2]

filtered=SMA(listdata,3)
print "----------------------------------------------------"
print filtered[:,2]
#CandleStickPlotting(filtered)
#CandleStickPlotting(listdata)


