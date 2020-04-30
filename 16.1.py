import csv
from datetime import datetime 

from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
filename2 = 'sitka_weather_2014.csv'
with open(filename2) as Q:
    reader2 = csv.reader(Q)
    header_row2 = next(reader2)

    dates2, highs2, lows2 = [], [], []
    for row2 in reader2:
            try:
                current_date2 = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date2, 'missing data')
            else:
                dates2.append(current_date)
                highs2.append(high)
                lows2.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates2, highs2, c= 'red', alpha = 0.9)
plt.plot(dates2, lows2, c = 'green', alpha = 0.9)


plt.title("Temperature difference betwen Sitka and death valley", fontsize = 24)
plt.xlabel('', fontsize =16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize =16)
plt.tick_params(axis='both', which = 'major', labelsize=16)

plt.show()


