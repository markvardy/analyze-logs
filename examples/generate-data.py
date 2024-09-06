import csv
import datetime
from dateutil.tz import tzlocal
from faker import Faker
import random
import json
import os

# Function

def create_data(start_date, end_date, min, max, min_steps, steps, range_num):
    fake = Faker()
    apitype = ['wait100ms', 'wait200ms', "wait300ms", "wait400ms"]
    data = []
    for i in range(range_num):
        row = {}
        row['@timestamp'] = fake.date_time_between(start_date=start_date, end_date=end_date,tzinfo=tzlocal()).isoformat(timespec='microseconds')[:-6]+'000Z'
        row['api_name'] = random.choice(apitype)
        latency_data = []
        for j in range(random.randint(min_steps, steps)):
            step = {}
            step['started'] = random.randint(min, max)
            latency_data.append(step) 
        row['latency_info'] = json.dumps(latency_data)
        data.append(row)
    return data


# Get the field names
with open("logs/analytics.csv") as original_file:
    fields, *_ = csv.reader(original_file, delimiter=",")

# Generate data


data = []

start_date = datetime.date(year=2024, month=8, day=1)
end_date = datetime.date(year=2024, month=8, day=6)
data = data + create_data(start_date, end_date, 1, 5, 1, 3, 100)

start_date = datetime.date(year=2024, month=8, day=6)
end_date = datetime.date(year=2024, month=8, day=8)
data = data + create_data(start_date, end_date, 11, 15, 4, 9, 40)

start_date = datetime.date(year=2024, month=8, day=8)
end_date = datetime.date(year=2024, month=8, day=13)
data = data + create_data(start_date, end_date, 1, 5, 1, 3, 100)


data.sort(key=lambda x: x['@timestamp'])

os.remove("logs/analytics100.csv")

# Write to file
with open('logs/analytics100.csv', 'w', newline='') as newcsv100:
    writer = csv.DictWriter(newcsv100, fieldnames=fields, restval='')
    writer.writeheader()
    writer.writerows(data)
