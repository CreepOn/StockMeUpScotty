import os
from markets import *
import json
from loadDataFunctions import *
os.system('clear')

tickers=get_C20();
print len(tickers)
for i in range(0,len(tickers)):
	data=getHistoricalData(tickers[i], 2)
	printRawData(data)
	


