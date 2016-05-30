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

listdata=JsonToList(getHistoricalData('TSLA', 365))

CandleStickPlotting(SMA(listdata,50))
#CandleStickPlotting(listdata)
