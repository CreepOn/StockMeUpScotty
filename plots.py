from pylab import *
import matplotlib.pyplot as plt
import time
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import candlestick,\
     plot_day_summary, candlestick2

def CandleStickPlotting(plotdata):
	mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
	alldays    = DayLocator()              # minor ticks on the days
	weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
	dayFormatter = DateFormatter('%d')      # e.g., 12

	title = 'Candlestick diagram'
	#and then following the official example. 
	fig, ax = plt.subplots()
	fig.subplots_adjust(bottom=0.2)
	ax.xaxis.set_major_locator(mondays)
	ax.xaxis.set_minor_locator(alldays)
	ax.xaxis.set_major_formatter(weekFormatter)
	candlestick(ax, plotdata, width=0.6)

	ax.xaxis_date()
	ax.autoscale_view()
	fig.suptitle(title, fontsize=12)
	plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

	savefig('foo.pdf')
