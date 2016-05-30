import numpy as np
import time

#Simple Moving Average - SMA

def movingAverage (values, timeFrame):
    # close price, no. of days
    weights = np.repeat(1.0, timeFrame)/timeFrame
    SMA = np.convolve(values,weights, 'valid')
    return SMA
'''
What is a 'Simple Moving Average - SMA'
A simple moving average (SMA) is a simple, or arithmetic, moving average that is calculated by adding the closing price
of the security for a number of time periods and then dividing this total by the number of time periods.
Short-term averages respond quickly to changes in the price of the underlying, while long-term averages are slow to react.
Read more: Simple Moving Average (SMA) Definition
http://www.investopedia.com/terms/s/sma.asp#ixzz49mYJCPtI 
'''
    
#Exponential Moving Average - EMA

def expMovingAverage(values, timeFrame):
    # close price, no. of days
    weights = np.exp(np.linspace(-1.,0.,timeFrame))
    weights /= weights.sum()

    EMA = np.convolve(values,weights, mode='full')[:len(values)]
    EMA[:timeFrame] = EMA[timeFrame]
    return EMA
'''
What is an 'Exponential Moving Average - EMA'
An exponential moving average (EMA) is a type of moving average that is similar to a simple moving average, except that more
weight is given to the latest data. The exponential moving average is also known as "exponentially weighted moving average". 
Read more: Exponential Moving Average (EMA) Definition
http://www.investopedia.com/terms/e/ema.asp#ixzz49mYwMDZT 
'''

#Accumulative Swing Index - ASI

def swingIndex(O1,O2,H1,H2,L1,L2,C1,C2,LM):
    # open1, open2, high1, high2, low1, low2, close1, close2, limitmove
    def calc_R(H2,C1,L2,O1,LM):
        x = H2-C1
        y = L2-C1
        z = H2-L2
        
        if z < x > y:
            R = (H2-C1)-(.5*(L2-C1))+(.25*(C1-O1))
            return R
        elif x < y > z:
            R = (L2-C1)-(.5*(H2-C1))+(.25*(C1-O1))
            return R
        elif x < z > y:
            R = (H2-L2)+(.25*(C1-O1))
            return R
            
    def calc_K(H2,L2,C1):
        x = H2-C1
        y = L2-C1

        if x > y:
            K=x
            return K
        elif x < y:
            K=y
            return K
    L = LM
    R = calc_R(H2,C1,L2,O1,LM)
    K = calc_K(H2,L2,C1)

    ASI = 50*((C2-C1+(.5*(C2-O2))+(.25*(C1-O1)))/R)*(K/L)
    return ASI
'''
DEFINITION of 'Accumulative Swing Index - ASI'
A indicator used by traders to gauge a security's long-term trend by comparing bars which contain its opening, closing, high
and low prices throughout a specific period of time. When the ASI is positive, it suggests that the long-term trend will be
higher, and when the ASI is negative, it suggests that the long-term trend will be lower. 
The ASI is often cited as being developed by Welles Wilder.

BREAKING DOWN 'Accumulative Swing Index - ASI'
While the ASI is most often used for futures trading, it can be used for analyzing the price trends of other assets as well.
The ASI may be used in conjunction with price charts in order to confirm trendline breakouts, because the same trendline
would be penetrated in both situations. 
http://www.investopedia.com/terms/a/asi.asp#ixzz49myf5e7Z 
'''

#True Range - TR

def TR(D,C,H,L,O,YC):
    # date,close,high,low,open,yesterdays close
    x = H-L
    y = abs(H-YC)
    z = abs(L-YC)
    
    if y <= x >= z:
        TR = x
    elif x <= y >= z:
        TR = y   
    elif x <= z >= y:
        TR = z

    return D,TR
'''
The true range indicator is the greatest of the following:
 -current high less the current low.
 -the absolute value of the current high less the previous close.
 -the absolute value of the current low less the previous close.
'''

#Average True Range - ATR
    
def ATR(TrueRanges,timeFrame):

    atr = expMovingAverage(TrueRanges,timeFrame)
    
    return atr

'''
What is the 'Average True Range - ATR'
The average true range (ATR) is a measure of volatility introduced by Welles Wilder in his book: New Concepts in
Technical Trading Systems.
The average true range is a moving average (generally 14-days) of the true ranges.
BREAKING DOWN 'Average True Range - ATR'
Wilder originally developed the ATR for commodities but the indicator can also be used for stocks and indexes.
Simply put, a stock experiencing a high level of volatility will have a higher ATR, and a low volatility stock
will have a lower ATR.
http://www.investopedia.com/terms/a/atr.asp#ixzz49nHk82hh 
'''

#Average Directional Index - ADX

def DM(d,o,h,l,c,yo,yh,yl,yc):
    #date, open, high, low, close, yesterdays open, yesterdays high, yesterdays low, yesterdays close
    moveUp = h-yh
    moveDown = yl-l

    if 0 < moveUp > moveDown:
        PDM = moveUp
    else:
        PDM = 0
    if 0 < moveDown > moveUp:
        NDM = moveDown
    else:
        NDM = 0
   
    return d,PDM,NDM

def CalcDIs(timeFrame):
    x = 1
    TRDates = []
    TrueRanges = []
    PosDMs = []
    NegDMs = []

    while x < len(date):
        #TR(d,c,h,l,o,yc)
        TRDate,TrueRange = TR(date[x],closep[x],highp[x],lowp[x],openp[x],closep[x-1])
        TRDates.append(TRDate)
        TrueRanges.append(TrueRange)
        
        #DM(d,o,h,l,c,yo,yh,yl,yc)
        DMdate,PosDM,NegDM = DM(date[x],openp[x],highp[x],lowp[x],closep[x],openp[x-1],highp[x-1],lowp[x-1],closep[x-1])
        PosDMs.append(PosDM)
        NegDMs.append(NegDM)
        x+=1
    
    expPosDM = expMovingAverage(PosDMs,timeFrame)
    expNegDM = expMovingAverage(NegDMs,timeFrame)
    ATR = expMovingAverage(TrueRanges,timeFrame)

    xx = 0
    PDIs = []
    NDIs = []

    while xx < len(ATR):
        PDI = 100*(expPosDM[xx]/ATR[xx])
        PDIs.append(PDI)

        NDI = 100*(expNegDM[xx]/ATR[xx])
        NDIs.append(NDI)

        xx += 1
       
    
    return PDIs,NDIs

def ADX(timeFrame):
    PositiveDI,NegativeDI = CalcDIs(timeFrame)

    xxx = 0
    DXs = []

    while xxx < len(date[1:]):
        DX = 100*((abs(PositiveDI[xxx]-NegativeDI[xxx])/(PositiveDI[xxx]+NegativeDI[xxx])))

        DXs.append(DX)
        xxx += 1

    ADX = expMovingAverage(DXs, timeFrame)

    return PositiveDI,NegativeDI,ADX
'''
What is the 'Average Directional Index - ADX'
The average directional index (ADX) is an indicator used in technical analysis as an objective value for the
strength of trend. ADX is non-directional so it will quantify a trend's strength regardless of whether it is
up or down. ADX is usually plotted in a chart window along with two lines known as the DMI
(Directional Movement Indicators). ADX is derived from the relationship of the DMI lines.
BREAKING DOWN 'Average Directional Index - ADX'
Analysis of ADX is a method of evaluating trend and can help traders to choose the strongest trends and also
how to let profits run when the trend is strong.
http://www.investopedia.com/terms/a/adx.asp#ixzz49npZTOgu 
'''


# Aroon + Aroon Oscillator

def aroon(timeFrame):

    AroonUp = []
    AroonDown = []
    AroonDate = []
    AroonOscillator = []

    x = timeFrame

    while x < len(date):
        Aroon_Up = ((highp[x-timeFrame:x].tolist().index(max(highp[x-timeFrame:x])))/float(timeFrame))*100
        Aroon_Down = ((lowp[x-timeFrame:x].tolist().index(max(lowp[x-timeFrame:x])))/float(timeFrame))*100
        Aroon_Osc = Aroon_Up - Aroon_Down
        
        AroonOscillator.append(Aroon_Osc)

        AroonUp.append(Aroon_Up)
        AroonDown.append(Aroon_Down)
        AroonDate.append(date[x])

        x+=1

    return AroonDate, AroonUp, AroonDown, AroonOscillator
'''
What is the 'Aroon Indicator'
The Aroon indicator is a technical indicator used for identifying trends in an underlying security and the
likelihood that the trends will reverse. It is made up of two lines: one line is called "Aroon up", which
measures the strength of the uptrend, and the other line is called "Aroon down", which measures the
downtrend. The indicator reports the time it is taking for the price to reach, from a starting point, the
highest and lowest points over a given time period, each reported as a percentage of total time.
BREAKING DOWN 'Aroon Indicator'
The Aroon indicator was developed by Tushar Chande in 1995. Both the Aroon up and the Aroon down fluctuate
between zero and 100, with values close to 100 indicating a strong trend, and zero indicating a weak trend.
The lower the Aroon up, the weaker the uptrend and the stronger the downtrend, and vice versa. The main
assumption underlying this indicator is that a stock's price will close at record highs in an uptrend, and
record lows in a downtrend.This indicator is very similar to the directional movement index (DMI) that was
developed by Welles Wilder, which is also a very popular indicator used to measure the strength of a given
trend.
http://www.investopedia.com/terms/a/aroon.asp#ixzz49stgbJe5 


DEFINITION of 'Aroon Oscillator'
A trend-following indicator that uses aspects of the Aroon indicator ("Aroon up" and "Aroon down") to gauge
the strength of a current trend and the likelihood that it will continue. The Aroon oscillator is
calculated by subtracting Aroon down from Aroon up. Readings above zero indicate that an uptrend is present,
while readings below zero indicate that a downtrend is present. 
BREAKING DOWN 'Aroon Oscillator'
Aroon up and Aroon down are the two components that comprise the Aroon indicator. The notion is that an
asset is trending up when a stock is trading near the high of its range. Aroon up is used to measure the
strength of the uptrend, while Aroon down is used to measure the strength of the downtrend. Many traders will
watch for a cross above the zero line to suggest the beginning of a new uptrend. Conversely, a cross below
zero would indicate the start of a downtrend. Readings near zero suggest that a security may be trending
sideways and that this period of consolidation could continue. 
http://www.investopedia.com/terms/a/aroonoscillator.asp#ixzz49sw64f5j 

'''

# Standard Deviation

def standardDeviation(timeFrame,price):
    sd = []
    sddate = []
    x = timeFrame

    while x < len(date):
        array2consider = price[x-timeFrame:x]
        standev = array2consider.std()
        sd.append(standev)
        sddate.append(date[x])
        x+=1

    return sddate,sd

'''
What is 'Standard Deviation'
Standard deviation is a measure of the dispersion of a set of data from its mean. The more spread apart
the data, the higher the deviation. Standard deviation is calculated as the square root of variance.
2. In finance, standard deviation is applied to the annual rate of return of an investment to measure
the investment's volatility. Standard deviation is also known as historical volatility and is used by
investors as a gauge for the amount of expected volatility.
BREAKING DOWN 'Standard Deviation'
Standard deviation is a statistical measurement that sheds light on historical volatility. For example,
a volatile stock will have a high standard deviation while the deviation of a stable blue chip stock
will be lower. A large dispersion tells us how much the return on the fund is deviating from the expected
normal returns.
http://www.investopedia.com/terms/s/standarddeviation.asp#ixzz49t0jywFh 

'''
################################# HAR EN FEJL HER ##########################
# Bollinger Band

def bollingerBands(multi,timeFrame2):
    bdate = []
    topBand = []
    bottomBand = []
    midBand = []

    x = timeFrame2

    while x < len(date):
        curSMA = movingAverage(closep[x-timeFrame2:x],timeFrame2)[-1]
        d,curSD = standardDeviation(timeFrame2,closep[0:timeFrame2])
########################################
        curSD = curSD[1] #  DETTER ER ORGINAL KODE  " curSD = curSD[-1] "
########################################
        
        TB = curSMA + (curSD*multi)
        BB = curSMA - (curSD*multi)
        D = date[x]
        
        bdate.append(D)
        topBand.append(TB)
        bottomBand.append(BB)
        midBand.append(curSMA)
        x+=1

    return bdate, topBand, bottomBand, midBand

'''
What is a 'Bollinger Band'
A Bollinger Band is a band plotted two standard deviations away from a simple moving average, developed by
famous technical trader John Bollinger.
BREAKING DOWN 'Bollinger Band'
Because standard deviation is a measure of volatility, Bollinger Bands adjust themselves to the market
conditions. When the markets become more volatile, the bands widen (move further away from the average), and
during less volatile periods, the bands contract (move closer to the average). The tightening of the bands is
often used by technical traders as an early indication that the volatility is about to increase sharply.
This is one of the most popular technical analysis techniques. The closer the prices move to the upper band,
the more overbought the market, and the closer the prices move to the lower band, the more oversold the market.
http://www.investopedia.com/terms/b/bollingerbands.asp#ixzz49tLzOJZd 

'''

# Center of Gravity 

def centerOfGravity(dates, data, timeFrame):
    cog = []
    x = timeFrame

    while x < len(dates):
        consider = data[x-timeFrame:x]
        multipliers = range(1,timeFrame+1)

        topFrac = 0
        botFrac = 0

        reversedOrder = reversed(consider)
        ordered = []
        for eachItem in reversedOrder:
            ordered.append(eachItem)

        for eachM in multipliers:
            addMe = eachM*ordered[eachM-1]
            addMe2 = ordered[eachM-1]

            topFrac += addMe
            botFrac += addMe2

        CeofGr = -(topFrac/float(botFrac))

        cog.append(CeofGr)

        x +=1
    return dates[timeFrame:],cog












'''
x = 1
TRDates = []
TrueRanges = []
timeFrame = 14

while x < len(date):
    TRDate,TrueRange = TR(date[x],closep[x],highp[x],lowp[x],openp[x],closep[x-1])
    TRDates.append(TRDate)
    TrueRanges.append(TrueRange)
    #print TrueRange
    x += 1

'''

 
timeFrame = 14
#print movingAverage(closep,20)
#print '-----------------------'
#print expMovingAverage(closep,20)
#print '-----------------------'
#print swingIndex(open1, open2, high1, high2, low1, low2, close1, close2, limitmove)
#print '-----------------------'
#print print ATR(TrueRanges,timeFrame)
#print '-----------------------'
#print TR(date,close1,high1,low1,open1,close2)
#print '-----------------------'
#print ADX(timeFrame)
#print '-----------------------'
#print aroon(20)
#print '-----------------------'
#print standardDeviation(timeFrame)   
#print '-----------------------'
#print bollingerBands(2,20)
print '-----------------------'
print centerOfGravity(date,closep,10)
print '-----------------------'
print '#######################'

