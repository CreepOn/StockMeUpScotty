import os
from markets import *
#import json
from loadDataFunctions import *
#import numpy as np
from stockIndicators_emil import *
from plots import *
from dataobject import *
from pylab import *
from supplot_test import *

whiteFont="\033[0m"
greenFont="\033[92m"
redFont="\033[91m"

#os.system('clear')

ticker='HTRO.ST'

ld=getDataObject(ticker,100)


soo=SO(ld, 14, 3)

rsii=RSI(ld, 14)


smaa1=SMA(ld,2)


Plot(rsii, soo, smaa1)

#print SO(ld, 14,3).data[:,1:]
print "end"