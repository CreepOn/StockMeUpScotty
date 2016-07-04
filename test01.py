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

ld=getDataObject(ticker,300)

rss=RSI(ld, 14)
print rss.data[:,1]
#print SO(ld, 14,3).data[:,1:]
