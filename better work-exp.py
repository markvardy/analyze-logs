# Imports
import csv
import json
from dateutil import parser
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

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
    listoflist.sort()
    for item_in_listoflist in listoflist:
        time.append(item_in_listoflist[0])
        sum.append(item_in_listoflist[1])
    return time, sum

# Main code
listoflist = []
listoflist2 = []
latcol = 0

with open("logs/analytics.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            col_count = 0
            for col in row:
                if col == "latency_info":
                    latcol = col_count
                else:
                    col_count += 1
        else:
            if row[3] == "wait100ms":
                listoflist.append(extract_data(row, latcol))
            else:
                listoflist2.append(extract_data(row, latcol))
        line_count += 1

time1, sum1 = extract_list(listoflist)
time3, sum5 = extract_list(listoflist2)

plt.style.use("_mpl-gallery")
fig, ax = plt.subplots()
myFmt = DateFormatter("%H:%M:%S\n%d/%m/%Y")
ax.xaxis.set_major_formatter(myFmt)
ax.plot(time1, sum1, "x-c", time3, sum5, "x-m", linewidth = 3)

plt.show()