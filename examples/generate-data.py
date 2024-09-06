import csv
import datetime
from dateutil.tz import tzlocal
from faker import Faker
import random
import json
import os

# Get the field names
with open("logs/analytics.csv") as original_file:
    fields, *_ = csv.reader(original_file, delimiter=",")

# Generate data
start_date = datetime.date(year=2024, month=8, day=1)
apitype = ['wait100ms', 'wait200ms']
fake = Faker()
data = []

for i in range(100):
    row = {}
    row['@timestamp'] = fake.date_time_between(start_date=start_date, end_date='+30d',tzinfo=tzlocal()).isoformat(timespec='microseconds')[:-6]+'000Z'
    row['api_name'] = random.choice(apitype)
    latency_data = []
    for j in range(random.randint(1, 10)):
        step = {}
        step['started'] = random.randint(0, 100)
        latency_data.append(step)
    row['latency_info'] = json.dumps(latency_data)
    data.append(row)

data.sort(key=lambda x: x['@timestamp'])

os.remove("logs/analytics100.csv")

# Write to file
with open('logs/analytics100.csv', 'w', newline='') as newcsv100:
    writer = csv.DictWriter(newcsv100, fieldnames=fields, restval='')
    writer.writeheader()
    writer.writerows(data)
