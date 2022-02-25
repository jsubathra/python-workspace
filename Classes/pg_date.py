import datetime
import pytz

# create date to work with days,months and year
# date format shd be only intergers without any 0
# DATE ONLY
# d = datetime.date(2020, 7, 22)
# print(d)
# tdy = datetime.date.today()
# print(tdy.day)  # current dte
# print(tdy.weekday())  # Mon 0 and sun 6
# print(tdy.isoweekday())  # Mon is 1 and SUn is 7


# # Time Deltas - time diff between times and days
# tdy = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# print(tdy + tdelta)  # cal date after 7 days
# print(tdy - tdelta)  # cal date before 7 days

# # date 2 = date1+ timedelta
# # timedelta = date1 + date2

# bday = datetime.date(2021, 12, 22)
# till_bday = bday - tdy
# print(till_bday)
# print(till_bday.total_seconds()) # print seconds till birthday

# TIME ONLY
# To work with hours,min,sec,micro
t = datetime.time(9, 30, 33, 10000)
print(t)


# BOTH DATE AND TIME
# to work with all - date and time
dt = datetime.datetime(2021, 1, 3, 11, 53, 46, 10000)
print(dt)
print(dt.time())
print(dt.date())
print(dt.year)

# Add and sub timedelta
dt_delta = datetime.timedelta(days=7)
dt_delta1 = datetime.timedelta(hours=12)

print(dt+dt_delta)
print(dt - dt_delta1)
# ------------------

# TIMEZONES not used with below -- use pytz - recommemend
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


for z in pytz.all_timezones:
    print(z)
