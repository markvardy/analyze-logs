# Imports
import csv
import json
from dateutil import parser
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import random

# Functioms
def extract_data(row, latcol):
    item = []
    jsonobj = json.loads(row[latcol]) 
    sum = 0
    for x in jsonobj:
        sum = sum + x["started"]
    item.append(parser.parse(row[0]))
    item.append(sum)
    return item

def extract_list(listoflist):
    time = []
    sum = []
    # listoflist.sort()
    for item_in_listoflist in listoflist:
        time.append(item_in_listoflist[0])
        sum.append(item_in_listoflist[1])
    return time, sum

# Main code
apilists = {}
latcol = 0

# Read data
with open("logs/analytics100.csv") as csv_file:
    labels, *data_rows = csv.reader(csv_file, delimiter=",")
    for idx, label in enumerate(labels):
        if label == "latency_info":
            latcol = idx
    
    for row in data_rows:
        apiname = row[3]
        if apiname not in apilists:
            apilists[apiname] = []
        apilists[apiname].append(extract_data(row, latcol))

# print(apilists)

# Plot data
plt.style.use("_mpl-gallery")
fig, ax = plt.subplots()
myFmt = DateFormatter("%H:%M:%S\n%d/%m/%Y")
colourlist = ["c", "r", "m", "b"]
ax.xaxis.set_major_formatter(myFmt)
for apiname in apilists:
    timedata, sumdata = extract_list(apilists[apiname])
    linecolour = random.choice(colourlist)
    ax.plot(timedata, sumdata, "x-" + linecolour, linewidth = 3)

plt.show()