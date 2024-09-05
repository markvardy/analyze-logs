from dateutil import parser
import datetime

dateobj = parser.parse("2024-08-22T19:39:09.606924954Z")

# Formatting options shown here: https://www.w3schools.com/python/python_datetime.asp
print(dateobj.strftime("%I:%M:%S %p on  %A %d %B, %Y"))
print(dateobj.strftime("%d/%m/%Y %H:%M:%S"))
