import matplotlib

# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg') #only used on raspberry
import json
import numpy as np
from pylab import *
from Tkinter import *
from datetime import datetime
from datetime import date
#import datetime
import time
import matplotlib.pyplot as plt
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import candlestick_ochl,\
     volume_overlay3 #plot_day_summary, candlestick2,
from yahoo_finance import Share

def JsonToList(hist):
	data = []
	for i in hist:
		Date1 = date2num(datetime.strptime(i['Date'], "%Y-%m-%d"))
		data.append((Date1,float(i['Open']),float(i['Close']),float(i['High']),float(i['Low']),int(i['Volume'])))
	return data

def CandleStickPlotting(plotdata):
	mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
	alldays    = DayLocator()              # minor ticks on the days
	weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
	dayFormatter = DateFormatter('%d')      # e.g., 12

	title = 'Candlestick diagram'
	#and then following the official example. 

	
	ala=np.matrix(plotdata)

	#print SP
	fig = plt.figure()
	#fig, ax = plt.subplot2grid((6,1), (0,0), rowspan=2, colspan=1)
	ax = plt.subplot2grid((6,1), (0,0), rowspan=3, colspan=1)
	plt.title('DSV stocks')
	ax2 = ax.twinx()
	ax3 = plt.subplot2grid((6,1), (3,0), rowspan=2,colspan=1, sharex=ax)

	# set the position of ax2 so that it is short (y2=0.32) but otherwise the same size as ax
	#ax2.set_position(matplotlib.transforms.Bbox([[0.125,0.1],[0.9,0.32]]))
	fig.subplots_adjust(bottom=0.2)
	ax.xaxis.set_major_locator(mondays)
	ax.xaxis.set_minor_locator(alldays)
	ax.xaxis.set_major_formatter(weekFormatter)

	#if ave1:
	SP = len(ala[:,0])
	candlestick_ochl(ax2, plotdata, width=0.6, colorup='#00ff00',colordown='#ff0000', alpha=0.4)
	#volume_overlay3(ax, plotdata, colorup='#00ff00', colordown='#ff0000', width=0.6, alpha=0.4)
	ax3.plot( ala[:,0], ala[:,2], 'g-', linewidth=0.4)

	# shift y-limits of the candlestick plot so that there is space at the bottom for the volume bar chart
	#pad = 0.25
	#yl = ax.get_ylim()
	ax.yaxis.tick_right()
	ax2.yaxis.tick_left()
	
	# make bar plots and color differently depending on up/down for the day
	dates = np.squeeze(np.asarray(np.transpose(ala[:,0])))
	vol = np.squeeze(np.asarray(np.transpose(ala[:,5])))
	pos = ala[:,1]-ala[:,2]<0
	neg = ala[:,1]-ala[:,2]>0
	pos = np.squeeze(np.asarray(pos))
	neg = np.squeeze(np.asarray(neg))
	
	ax.bar(dates[pos],vol[pos],color='green',alpha=0.8)#,width=1,align='center')
	ax.bar(dates[neg],vol[neg],color='#df3a01',alpha=0.8)#,width=1,align='center')
	#x = np.arange(0.0, 2, 0.01)
	#y1 = np.sin(2*np.pi*x)
	#print np.squeeze(np.asarray(np.transpose(ala[:,0])))
	#ax.bar(ala[:,0],ala[:,5],color='cyan', alpha=0.4)#width=1,align='center'
	#ax.fill_between(np.squeeze(np.asarray(np.transpose(ala[:,0]))), np.squeeze(np.asarray(np.transpose(ala[:,5]))), 0,color='blue')#,color='blue', alpha=0.4)
	
	#scale the x-axis tight
	#ax.set_xlim(min(ala[:,0]),max(ala[:,0]))
	plt.setp(ax.get_xticklabels(), visible=False)
	ax.set_ylim(0, 3*max(ala[:,5]))
	ax.set_yticks([0,max(ala[:,5])])
	# the y-ticks for the bar were too dense, keep only every third one
	#yticks = ax2.get_yticks()
	#ax2.set_yticks(yticks[::3])

	ax.yaxis.set_label_position("right")
	ax.set_ylabel('Volume', size=12)

	ax2.yaxis.set_label_position("left")
	ax2.set_ylabel('Price', size=12)

	# format the x-ticks with a human-readable date. 
	xt = ax3.get_xticks()
	new_xticks = [datetime.date(num2date(d)) for d in xt]
	ax3.set_xticklabels(new_xticks,rotation=45, horizontalalignment='right')
	
	ax.patch.set_facecolor('gray')
	
	#plt.tight_layout()
	plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
	
	#plt.hod(True)
	#plt.show()
	savefig('foo.pdf', facecolor='gray', edgecolor='gray')#fig.get_facecolor()


DSV_hist = DSV.get_historical('2016-01-01', '2016-05-29')
#print DSV_hist
CandleStickPlotting(JsonToList(DSV_hist))