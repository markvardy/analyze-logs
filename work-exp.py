import csv
import json
from dateutil import parser
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as dates
from matplotlib.dates import DateFormatter
api1 = []
api2 = []
latcol = 0
with open("logs/analytics.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(", ".join(row))
            col_count = 0
            for col in row:
                if col == "latency_info":
                    latcol = col_count
                else:
                    col_count += 1
        else:
            # print(row[3])
            # line_count += 1
            if row[3] == "wait100ms":
                api1.append(row)
            else:
                api2.append(row)
        line_count += 1


# for apirow in api1:
#     print(apirow[latcol])
# for apirow in api2:
#     print(apirow[latcol])
time = []
sum2 = []
listoflist = []
for row in api1:
    item = []
    timestamp = row[0]
    datetime_timestamp = parser.parse(timestamp)
    # datetime.strftime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    firstjson = row[latcol]
    jsonobj = json.loads(firstjson)
    sum = 0
    for x in jsonobj:
       sum = sum + x["started"]
    time.append(datetime_timestamp.strftime("%H:%M:%S.%f\n%d/%m/%Y"))
    sum2.append(sum)
    item.append(datetime_timestamp)
    item.append(sum)
    listoflist.append(item)


# print(time)
# print(sum2)

listoflist.sort()
# print(listoflist)

time1 = []
for list3 in listoflist:
    date = list3[0]
    time1.append(date)
# print (time1)

sum1 = []
for list4 in listoflist:
    sums = list4[1]
    sum1.append(sums)
# print (sum1)

listoflist2 = []
for row in api2:
    item1 = []
    timestamp1 = row[0]
    datetime_timestamp1 = parser.parse(timestamp1)
    # datetime.strftime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    firstjson1 = row[latcol]
    jsonobj1 = json.loads(firstjson1)
    sum3 = 0
    for x1 in jsonobj1:
       sum3 = sum3 + x1["started"]
    # time2.append(datetime_timestamp1.strftime("%H:%M:%S.%f\n%d/%m/%Y"))
    # sum4.append(sum3)
    item1.append(datetime_timestamp1)
    item1.append(sum3)
    listoflist2.append(item1)

listoflist2.sort()

time3 = []
for list5 in listoflist2:
    date1 = list5[0]
    time3.append(date1)
# print (time3)

sum5 = []
for list6 in listoflist2:
    sums2 = list6[1]
    sum5.append(sums2)
# print (sum5)


# fig, ax = plt.subplots()
# x_pos = np.arange(len(sum2))
# ax.bar(x_pos, sum2, align="center")
# ax.set_xticks(x_pos, labels=time)
# ax.set_xlabel("Timestamp", fontsize = 20)
# ax.set_ylabel("Duration", fontsize = 20)
# # ax.xaxis.label.set_color("")
# plt.show()


plt.style.use("_mpl-gallery")


# plot
fig, ax = plt.subplots()
myFmt = DateFormatter("%H:%M:%S\n%d/%m/%Y")
ax.xaxis.set_major_formatter(myFmt)
ax.plot(time1, sum1, "x-c", time3, sum5, "x-m", linewidth = 3)


# plt.gcf().autofmt_xdate()
plt.show()
