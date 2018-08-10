import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	highs = []
	dates = []
	lows = []
	for row in reader:
		highs.append(int(row[1]))
		dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
		lows.append(int(row[3]))

fig = plt.figure(dpi = 148,figsize = (10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.5)
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10) 
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()