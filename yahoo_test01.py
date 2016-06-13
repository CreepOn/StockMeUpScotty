import os
from markets import *
#import json
from loadDataFunctions import *
import numpy as np
from stockIndicators_emil import *
from plots import *
from dataobject import *
os.system('clear')


#tickers=get_C20()
#for i in range(0,len(tickers)):
#	data=getHistoricalData(tickers[i], 4)
#printRawData(data)

ticker='TSLA'

#listdata=dataobject(ticker, 'raw', JsonToMatrix(getHistoricalData(ticker,25)))

#print listdata

timeFrame=10

weights = np.exp(np.linspace(-1.,0.,timeFrame))
weights /= weights.sum()

print weights
