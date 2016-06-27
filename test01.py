import os
from markets import *
#import json
from loadDataFunctions import *
import numpy as np
from stockIndicators_emil import *
from plots import *
from dataobject import *
from pylab import *

whiteFont="\033[0m"
greenFont="\033[92m"
redFont="\033[91m"

os.system('clear')

ticker='TSLA'

ld=dataobject(ticker, 'raw', JsonToMatrix(getHistoricalData(ticker,100)))

print SO(ld, 14,3).data[:,1:]
