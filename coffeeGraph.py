import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.ndimage.filters import gaussian_filter1d
import numpy as np

CVS_NAME = 'coffee.cvs'
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')

x = []
y = []
with open(CVS_NAME, 'r') as coffeeCVS:
    entries = coffeeCVS.readlines()
    prevDate = entries[0].split(" ")[0]
    cnt = 0
    for line in entries:
        date = line.split(" ")[0]
        if date == prevDate:
            cnt += 1
        else:
            x.append(prevDate)
            y.append(cnt)
            cnt = 1
        prevDate = date
xAvg = []
yAvg = []
with open(CVS_NAME, 'r') as coffeeCVS:
    entries = coffeeCVS.readlines()
    prevDate = entries[0].split(" ")[0]
    totCups = 0
    totDays = 0
    for line in entries:
        date = line.split(" ")[0]
        if date != prevDate:
            totDays += 1
            xAvg.append(prevDate)
            yAvg.append(float(totCups / totDays))
        totCups += 1
        prevDate = date

fig, ax = plt.subplots(tight_layout=True)
# ax.plot(x, y, label='cups')
ysmoothed = gaussian_filter1d(y, sigma=1)
ax.plot(x, ysmoothed, label='gaussian_cups')
ax.plot(xAvg, yAvg, label='avg')

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

# labels
plt.xlabel('date')
plt.ylabel('nCups')
plt.title('Coffe consumption\ntotal:' + str(totCups) + " | avg:{0:.2f}".format(totCups/totDays))

# display graph between these dates & format
datemin = np.datetime64(x[0], 'D')
datemax = np.datetime64(x[-1], 'D')
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.set_xlim(str(datemin), str(datemax))

# nasty xaxis date label calculation & auto-rotate
xplots = [a if int(a[-2:]) % 30 == 0 else "" for a in list.copy(x)]
plt.xticks(range(len(xplots)), xplots)
fig.autofmt_xdate()

# display 'indicators' & graph
plt.legend()
plt.show()
