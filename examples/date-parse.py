from dateutil import parser
import datetime

dateobj = parser.parse("2024-08-22T19:39:09.606924954Z")

print(dateobj)
print(dateobj.strftime("%A %d %B, %Y"))