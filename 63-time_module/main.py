import time

print(time.ctime(0)) # Thu Jan  1 01:00:00 1970
                     # convert a time expressed in second since epoch to a readable string
                     # epoch -> when your computer thinks time began (reference point)

print(time.time()) # 1640896808.730367
                   # return corrent seconds since epoch

print(time.ctime(time.time())) # Thu Dec 30 21:42:38 2021

time_object = time.localtime()
print(time_object) #time.struct_time(tm_year=2021, tm_mon=12, tm_mday=30, tm_hour=21, tm_min=43, tm_sec=31, tm_wday=3, tm_yday=364, tm_isdst=0)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time) # December 30 2021 21:47:18

#(year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2020,4,20,4,20,0,0,0,0)
time_string = time.asctime(time_tuple)
print(time_string) # Mon Apr 20 04:20:00 2020

#(year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2020,4,20,4,20,0,0,0,0)
time_string = time.mktime(time_tuple)
print(time_string) # 1587352800.0