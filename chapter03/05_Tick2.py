# 结合日期
from pylab import *
import matplotlib as mpl
import datetime

fig = figure()

# get current axis
ax = gca()

start = datetime.datetime(2018, 7, 1)
stop = datetime.datetime(2018, 12, 31)
delta = datetime.timedelta(days=1)
dates = mpl.dates.drange(start, stop, delta)

values = np.random.rand(len(dates))
ax = gca()

ax.plot_date(dates, values, linestyle='-', marker='')
date_format = mpl.dates.DateFormatter('%Y-%m-%d')

ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()
savefig('test305.png')
show()



