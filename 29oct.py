# date time  , time  , time delta , calender 

import datetime as dt 

"""a= dt.datetime.now()
print(a)

b= dt.datetime.today()
print(b)

# string  format time  :29 - 10 -2025  18 :11:45 
c =dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(c)
"""
"""d=dt.datetime(2025,10,30,18,11,45,34567)
print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)

"""

import time as t

"""print(t.time())
print(t.ctime())
print(t.localtime())
"""
# sleep  function  : 

"""
for i in range(10):
    t.sleep(1)
    print(i)
"""

"""
from datetime import timedelta as td 

today_date =dt.datetime.today()  # 29/10/2025 
future_date =today_date + td(days =90)

print(today_date)
print(future_date)
"""

"""import calendar as cal 

a=cal.calendar(2025)
print(a)
"""

# random  ,  date time  time  delta  ,calender  ==> python in-built
 
from my_package import myfunction as mf ,hello as hl

print(mf.sum(12,34))
hl.say_hello()