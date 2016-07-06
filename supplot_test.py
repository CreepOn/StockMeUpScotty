
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
from dataobject import *
from loadDataFunctions import *
from stockIndicators_emil import *

class Plot_feature:
	def __init__(self):
		self.rsi_count = 0
		self.top_count = 0
		self.so_count = 0
		self.amount = 0
		self.types = 0
		self.sub_plot_types = 0

	def reset(self):
		self.ave_count = 0
		self.raw_count = 0		

	def amount_of_plot(self):
		self.amount = self.top_count + self.rsi_count + self.so_count 

	def rsi_plot(self):
		self.types+=1 
		self.rsi_count+=1
		self.sub_plot_types+=1
	
	def top_plot(self):
		if self.top_count == 0:
			self.types+=1
		self.top_count+=1

	def so_plot(self):
		self.types+=1
		self.so_count+=1
		self.sub_plot_types+=1

	def plot_get(self, *args):
		for i in args:
			switcher = {'rsi': self.rsi_plot, 'mov avg': self.top_plot}
			switcher[i.category]()
		self.amount_of_plot()

def plot_single_data(Pfeat,*args):
	#Generating avg figure 

	#Pfeat = Plot_feature()

	#Pfeat.plot_get(*args)
	
	ax = []
	ax_count = 0 
	fig = plt.figure()
	plt.suptitle(args[0].ticker, size=14)
	if (Pfeat.types - Pfeat.sub_plot_types) > 0:
		ax.append(plt.subplot2grid((3+Pfeat.sub_plot_types,1), (0,0), rowspan=3, colspan=1))
		plt.setp(ax[0].get_xticklabels(), visible=False)
	#print len(ax)
	for i in range(0,Pfeat.amount):
		if 'rsi' in args[i].category:
			if (Pfeat.types - Pfeat.sub_plot_types) > 0:
				ax_count+=1
				ax.append(plt.subplot2grid((3+Pfeat.sub_plot_types,1), (ax_count+2,0), rowspan=1,colspan=1, sharex=ax[0]))
			else:
				if len(ax) == 0:
					ax.append(plt.subplot2grid((Pfeat.sub_plot_types,1), (ax_count,0), rowspan=1,colspan=1))
				else:
					ax_count+=1
					ax.append(plt.subplot2grid((Pfeat.sub_plot_types,1), (ax_count,0), rowspan=1,colspan=1, sharex=ax[0]))
			ax[ax_count].grid(b=True, which='major', color='#dddddd', linestyle='-')
			ax[ax_count].set_title(args[i].category, size=10)
			#linemax = [70] * len(args[i].data[:,0])
			#linemin = [30] * len(args[i].data[:,0])
			ax[ax_count].axhline(y=70,ls='--',color='r')
			ax[ax_count].axhline(y=30,ls='--',color='c')
			#ax[ax_count].plot(args[i].data[:,0],linemax,'--r',args[i].data[:,0],linemin,'--c')
			ax[ax_count].plot(args[i].data[:,0],args[i].data[:,1],'-g')
			ax[ax_count].set_ylim((0,100))
			

		if 'mov avg' in args[i].category:
			#linemax = [250] * len(args[i].data[:,0])
			#linemin = [220] * len(args[i].data[:,0])
			ax[0].grid(b=True, which='major', color='#dddddd', linestyle='-')
			ax[0].plot(args[i].data[:,0],args[i].data[:,1],'r')
					


	
	print len(ax)
	xt = ax[len(ax)-1].get_xticks()
	new_xticks = []
	ds = [date.fromordinal(int(d)) for d in xt]
	for ele in ds:
		new_xticks.append(ele.strftime("%d.%m.%y"))
	
	ax[len(ax)-1].set_xticklabels(new_xticks,rotation=0, horizontalalignment='right')
	#plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
	#plt.tight_layout()
	savefig(args[0].ticker+'_single_data'+'.pdf', facecolor='gray', edgecolor='gray')#fig.get_facecolor()

def Plot(*args):

	Pfeat = Plot_feature()

	Pfeat.plot_get(*args)
	
	plot_single_data(Pfeat,*args)
	#print Pfeat.amount
	#print Pfeat.ave_count
	#print Pfeat.raw_count
	#print len(args)
	#candledata = JsonToList(args[1])
	#mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
	#alldays    = DayLocator()              # minor ticks on the days
	#weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
	#dayFormatter = DateFormatter('%d')      # e.g., 12
	#and then following the official example. 



ticker='TSLA'

listdataavg10=dataobject(ticker, 'raw', JsonToMatrix(getHistoricalData(ticker,100)))
listdataavg10=SMA(listdataavg10,10)
listdataavg20=dataobject(ticker, 'raw', JsonToMatrix(getHistoricalData(ticker,100)))
listdataavg20=SMA(listdataavg20,20)
listdataavg50=dataobject(ticker, 'raw', JsonToMatrix(getHistoricalData(ticker,100)))
listdataavg50=SMA(listdataavg50,50)
listdata=dataobject(ticker, 'rsi', JsonToMatrix(getHistoricalData(ticker,100)))

Plot(listdata)#, listdataavg10, listdataavg20, listdataavg50)
#print listdata
#print
print 'Done'
'''
	# set the position of ax2 so that it is short (y2=0.32) but otherwise the same size as ax
	#ax2.set_position(matplotlib.transforms.Bbox([[0.125,0.1],[0.9,0.32]]))
	fig.subplots_adjust(bottom=0.2)
	ax[0].xaxis.set_major_locator(mondays)
	ax[0].xaxis.set_minor_locator(alldays)
	ax[0].xaxis.set_major_formatter(weekFormatter)

	#if ave1:
	SP = len(ala[:,0])
	candlestick_ochl(ax[2], candledata, width=0.6, colorup='#00ff00',colordown='#ff0000', alpha=0.4)
	#volume_overlay3(ax, plotdata, colorup='#00ff00', colordown='#ff0000', width=0.6, alpha=0.4)
	ax[2].plot( ala[:,0], ala[:,2], 'g-', linewidth=0.4)
	ax[3].plot( ala[:,0], ala[:,2], 'g-', linewidth=0.4)

	# shift y-limits of the candlestick plot so that there is space at the bottom for the volume bar chart
	#pad = 0.25
	#yl = ax.get_ylim()
	ax[0].yaxis.tick_right()
	ax[1].yaxis.tick_left()
	
	# make bar plots and color differently depending on up/down for the day
	dates = np.squeeze(np.asarray(np.transpose(ala[:,0])))
	vol = np.squeeze(np.asarray(np.transpose(ala[:,5])))
	pos = ala[:,1]-ala[:,2]<0
	neg = ala[:,1]-ala[:,2]>0
	pos = np.squeeze(np.asarray(pos))
	neg = np.squeeze(np.asarray(neg))
	
	ax[0].bar(dates[pos],vol[pos],color='green',alpha=0.8)#,width=1,align='center')
	ax[0].bar(dates[neg],vol[neg],color='#df3a01',alpha=0.8)#,width=1,align='center')
	#x = np.arange(0.0, 2, 0.01)
	#y1 = np.sin(2*np.pi*x)
	#print np.squeeze(np.asarray(np.transpose(ala[:,0])))
	#ax.bar(ala[:,0],ala[:,5],color='cyan', alpha=0.4)#width=1,align='center'
	#ax.fill_between(np.squeeze(np.asarray(np.transpose(ala[:,0]))), np.squeeze(np.asarray(np.transpose(ala[:,5]))), 0,color='blue')#,color='blue', alpha=0.4)
	
	#scale the x-axis tight
	#ax.set_xlim(min(ala[:,0]),max(ala[:,0]))
	plt.setp(ax[0].get_xticklabels(), visible=False)
	ax[0].set_ylim(0, 3*max(ala[:,5]))
	ax[0].set_yticks([0,max(ala[:,5])])
	# the y-ticks for the bar were too dense, keep only every third one
	#yticks = ax2.get_yticks()
	#ax2.set_yticks(yticks[::3])

	ax[0].yaxis.set_label_position("right")
	ax[0].set_ylabel('Volume', size=12)

	ax[1].yaxis.set_label_position("left")
	ax[1].set_ylabel('Price', size=12)

	# format the x-ticks with a human-readable date. 
	xt = ax[2].get_xticks()
	new_xticks = [datetime.date(num2date(d)) for d in xt]
	ax[2].set_xticklabels(new_xticks,rotation=45, horizontalalignment='right')
	
	ax[0].patch.set_facecolor('gray')
	
	#plt.tight_layout()
	plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
	'''
	#plt.hold(True)
	#plt.show()


#x = Plot_feature()
#print x.ave_count	
#x.plot_get('ave','ave','ave','ave','ave','candle');
#print x.ave_count
'''
fig = plt.figure()
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])
plt.hold(True)
plt.plot([5,2,8])

savefig('hest.pdf', facecolor='gray', edgecolor='gray')#fig.get_facecolor()
#plt.show()
'''
