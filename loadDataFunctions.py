from yahoo_finance import Share
from pylab import *
from datetime import *
import numpy as np
import json
from dataobject import *

whiteFont="\033[0m"
greenFont="\033[92m"
redFont="\033[91m"

def getDataObject(ticker, days):
	return dataobject(ticker, 'raw', JsonToMatrix(getHistoricalData(ticker,days)))


def JsonToList(hist):
	data = []
	for i in hist:
		Date1 = date2num(datetime.strptime(i['Date'], "%Y-%m-%d"))
		temp = Date1, float(i['Open']), float(i['Close']), float(i['High']), float(i['Low']), float(i['Volume'])
		data.append(temp)
	return data

def JsonToMatrix(hist):
	try:
		for ele in hist:
			Date1 = date2num(datetime.strptime(ele['Date'], "%Y-%m-%d"))
			temp = matrix([Date1, float(ele['Open']), float(ele['Close']), float(ele['High']), float(ele['Low']), float(ele['Volume'])])
			if 'data' in locals():
				data=np.r_[data, temp]
			else:
				data=temp
		return data
	except:
		print redFont+"Stock does not exist"+whiteFont
		return matrix([])

def today():
	datotid=datetime.now()
	today = str(datotid)[0:10]
	return today

def dateDaysAgo(timeGone):
	datotid=datetime.now()
	then=str(datotid - timedelta(days=int(timeGone)))[0:10]
	return then

def getHistoricalData(ticker, daysAgo):
	try:
		yahoo = Share(ticker)
	except ValueError:
		print "Error occured" + str(ValueError)
		
	data=yahoo.get_historical(dateDaysAgo(daysAgo), today())
	try:
		empty={}
		#element={'Volume': yahoo.get_volume(), 'Symbol': ticker, 'High': yahoo.get_days_high(), 'Low': yahoo.get_days_low(), 'Open': yahoo.get_open(), 'Close': yahoo.get_prev_close(), 'Date': yahoo.get_trade_datetime()[0:10]}
	except ValueError:
		print "LALALA"
	
	if len(data) > 0:
		data = sorted(data, key=lambda k: k['Date'], reverse=False) #Sort by Date of json element

		#try:
		#	if data[-1]['Date'] != element['Date']:
		#		data.append(element)
		#except ValueError:
		#	print "DOH"
		#data = sorted(data, key=lambda k: k['Date'], reverse=False) #Sort by Date of json element
	
	return data
	
def printRawData(data):
	if len(data)>0:
		try:
			datalength=len(data)
			for i in range(0,datalength):
				if data[0]['Open'] > data[i]['Close']:
					print redFont
				else:
					print greenFont
				print "-----------------------------------"
				print "Symbol: " + data[i]['Symbol']
				print "Date: " +data[i]['Date']
				print "Volume: " +data[i]['Volume']
				print "-----------------------------------"
				print "High: " +data[i]['High']
				if data[0]['Open'] > data[i]['Close']:
					print "Open: " +data[i]['Open']
					print "Close: " +data[i]['Close']
				else:
					print "Close: " +data[i]['Close']
					print "Open: " +data[i]['Open']
				print "Low: " +data[i]['Low']
				print "-----------------------------------"
			print whiteFont
		except ValueError:
			print "NONONO"


#get_price()
#get_change()
#get_volume()
#get_prev_close()
#get_open()
#get_avg_daily_volume()
#get_stock_exchange()
#get_market_cap()
#get_book_value()
#get_ebitda()
#get_dividend_share()
#get_dividend_yield()
#get_earnings_share()
#get_days_high()
#get_days_low()
#get_year_high()
#get_year_low()
#get_50day_moving_avg()
#get_200day_moving_avg()
#get_price_earnings_ratio()
#get_price_earnings_growth_ratio()
#get_price_sales()
#get_price_book()
#get_short_ratio()
#get_trade_datetime()
#get_historical(start_date, end_date)
#get_info()
#refresh()
