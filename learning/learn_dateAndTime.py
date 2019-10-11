# File Name learn_dateAndTime.py
# Demo for basic Python tuple functionality
# link : https://www.tutorialspoint.com/python3/python_date_time.htm
#!usr/bin/python3

import time
import calendar
from utility import *
printDes("Time,Date and Calender", "This is tutorial for time and date handling in python")


printDes("Time and Date")
# tick or epoch
print("tick or epoch: Seconds since 1st JAN 1970: time.time() = ", time.time())

# Time struct
#time.struct_time(tm_year=2017,
#    tm_mon=10,
#    tm_mday=24,
#    tm_hour=14,
#    tm_min=37,
#    tm_sec=32,
#    tm_wday=1,
#    tm_yday=297,
#    tm_isdst=0)
timeStruct = time.localtime()
print("Time Struct: ", timeStruct)
print("Accessing values from Time Struct: timeStruct.tm_hour:", timeStruct.tm_hour)

# Time Tuple from tick or epoch
tick = 1508822152
anotherTime = time.localtime(tick)
print("Time Tuple for epoch 1508822152 => ", anotherTime)

# Create Time Tuple
tup = (2017, 6, 27, 18, 34, 36,1,1,0)
tupTime = time.mktime(tup)
timeTupleFromTuple = time.localtime(tupTime)
print("Time from tuple: ", tup, " => ", tupTime, " => ", timeTupleFromTuple)

# Time Formatting
# %a − abbreviated weekday name
# %A − full weekday name
# %b − abbreviated month name
# %B − full month name
# %c − preferred date and time representation
# %C − century number (the year divided by 100, range 00 to 99)
# %d − day of the month (01 to 31)
# %D − same as %m/%d/%y
# %e − day of the month (1 to 31)
# %g − like %G, but without the century
# %G − 4-digit year corresponding to the ISO week number (see  %V).
# %h − same as %b
# %H − hour, using a 24-hour clock (00 to 23)
# %I − hour, using a 12-hour clock (01 to 12)
# %j − day of the year (001 to 366)
# %m − month (01 to 12)
# %M − minute
# %n − newline character
# %p − either am or pm according to the given time value
# %r − time in a.m. and p.m. notation
# %R − time in 24 hour notation
# %S − second
# %t − tab character
# %T − current time, equal to %H:%M:%S
# %u − weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday = 1
# %U − week number of the current year, starting with the first Sunday as the first day of the first week
# %V − The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
# %W − week number of the current year, starting with the first Monday as the first day of the first week
# %w − day of the week as a decimal, Sunday = 0
# %x − preferred date representation without the time
# %X − preferred time representation without the date
# %y − year without a century (range 00 to 99)
# %Y − year including the century
# %Z or %z − time zone or name or abbreviation
# %# % − a literal % character


# String From Time
formatStr = "%B %d, %a, %Y, %r"
strVal = time.strftime(formatStr, anotherTime)
print("String From Time with format - %s" % formatStr, "[", anotherTime,"] => ", strVal)
strVal = time.strftime(formatStr, timeTupleFromTuple)
print("String From Time (tupTime) with format - %s" % formatStr, "[", timeTupleFromTuple,"] => ", strVal)

formatStr = "%m%d%Y"
strVal = time.strftime(formatStr, time.localtime())
print("\nLocal: String From Time (tupTime) with format - %s" % formatStr, "[", time.localtime(),"] => ", strVal)


# Time from string
# %a − abbreviated weekday name
# %A − full weekday name
# %b − abbreviated month name
# %B − full month name
# %c − preferred date and time representation
# %C − century number (the year divided by 100, range 00 to 99)
# %d − day of the month (01 to 31)
# %D − same as %m/%d/%y
# %e − day of the month (1 to 31)
# %g − like  %G, but without the century
# %G − 4-digit year corresponding to the ISO week number (see %V).
# %h − same as %b
# %H − hour, using a 24-hour clock (00 to 23)
# %I − hour, using a 12-hour clock (01 to 12)
# %j − day of the year (001 to 366)
# %m − month (01 to 12)
# %M − minute
# %n − newline character
# %p − either am or pm according to the given time value
# %r − time in a.m. and p.m. notation
# %R − time in 24 hour notation
# %S − second
# %t − tab character
# %T − current time, equal to %H:%M:%S
# %u − weekday as a number (1 to 7), Monday = 1. Warning: In Sun Solaris Sunday = 1
# %U − week number of the current year, starting with the first Sunday as the first day of the first week
# %V − The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
# %W − week number of the current year, starting with the first Monday as the first day of the first week
# %w − day of the week as a decimal, Sunday = 0
# %x − preferred date representation without the time
# %X − preferred time representation without the date
# %y − year without a century (range 00 to 99)
# %Y − year including the century
# %Z or %z − time zone or name or abbreviation
# %% − a literal % character

timeStr = "July 27, 2014, 04:12:11 PM"
formatStr = "%B %d, %Y, %I:%M:%S %p"
timeTupleFromStr = time.strptime(timeStr, formatStr)
print("Time From String: %s" % timeStr, "with Format %s" % formatStr, " => ", timeTupleFromStr)

# GMT Time and asctime(convert time tuple to string)
timeVal = time.mktime(timeTupleFromStr)
gmtTime = time.gmtime(timeVal)
gmtTimeStr = time.asctime(gmtTime)
print("GMT Time of tuple", timeStr, " => ", gmtTimeStr)

# ctime: Convert sec to local time string
print("ctime: ", timeStr,"(", timeVal, ") => ", time.ctime(timeVal))

printDes("Calender")
yr2011 = calendar.calendar(2011)
print("** 2011 **\n")
print(yr2011)
month12_2014 = calendar.month(2014,12)
print("** Dec 2014 **\n")
print(month12_2014)
month11_1944 = calendar.month(1944,11)
print("** Nov 1944 **\n")
print(month11_1944)
month12_1952 = calendar.month(1952,12)
print("** Dec 1952 **\n")
print(month12_1952)

# weekday
print("weekday : 02 N0V 1944 => ", calendar.weekday(1944,11,2))

printEnd()
################################################################################
