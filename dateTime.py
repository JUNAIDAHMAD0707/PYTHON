from datetime import *

#getting min date
Min_date=date.min
print("Supported min date is:",Min_date)

Max_date=date.max
print("Supported max date is:",Max_date)
'''current_date=date(2022,9,28)
print(current_date)

#Accessing the Attributes
print("current year is:",current_date.year)
print("current month is:",current_date.month)
print("current day is:",current_date.day)'''
today=date.today()
print("today's date is:",today)

#getting weekday using weekdays() method
print("weekday using weekday() method is:",today.weekday())

#getting weekday using isoweekdays() method
print("weekday using isoweekday() method is:",today.isoweekday())

iso_str=date.isoformat(today)
print("ISO representation is:",iso_str)
print(type(iso_str))


########    TIME class   ############
current_time=time(2,3,30)
print("current time:",current_time)
# time with only one parameter
current_time=time(minute=7)
print("time with only one parameter:",current_time)
####   time with no argument
current_time=time()
print("time with no parameter:",current_time)

#getting min time
mintime=time.min
print("min time supported:",mintime)

#getting max time
maxtime=time.max
print("max time supported:",maxtime)

#####   creating time object
Time= time(14,17,54,5454)

# Accessing attributes
print("Hours:",Time.hour)
print("Minutes:",Time.minute)
print("Seconds:",Time.second)
print("Microseconds:",Time.microsecond)

#### converting time object to string
timestr=Time.isoformat()
print("string representation:",timestr)
print(type(timestr))

#### converting string to time object
Time=time.fromisoformat(timestr)
print("string to time:",Time)
print(type(Time))

Time=Time.replace(minute=29,second=39)
print("new time:",Time)

#####  Formatting time   ######
ftime=Time.strftime("%I:%M %p")
print("Formatted time",ftime)
