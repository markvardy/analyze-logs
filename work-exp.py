import csv
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


for apirow in api1:
    print(apirow[latcol])
for apirow in api2:
    print(apirow[latcol])