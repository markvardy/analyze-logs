from dateutil import parser
import datetime

dateobj1 = parser.parse("2024-08-22T19:39:09.606924954Z")
dateobj2 = parser.parse("2024-08-22T18:39:09.606924954Z")

myarray = [
    [dateobj1, 11],
    [dateobj2, 4]
]

print(myarray)

myarray.sort(key=lambda x: x[0])

print(myarray)


# Formatting options shown here: https://www.w3schools.com/python/python_datetime.asp
# print(dateobj.strftime("%I:%M:%S %p on  %A %d %B, %Y"))
# print(dateobj.strftime("%d/%m/%Y %H:%M:%S"))