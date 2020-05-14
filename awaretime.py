import datetime
import pytz

local_time = datetime.datetime.now()
UTC_time = datetime.datetime.utcnow()

print("Naive local time is  {}".format(local_time))
print("Naive UTC time is  {}".format(UTC_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_UTC_time = pytz.utc.localize(UTC_time)

print("Aware time local time is {} in timezone {}". format(aware_local_time, aware_local_time.tzinfo))
print("Aware time UTC time is {} in timezone {}". format(aware_UTC_time, aware_local_time.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("Seconds {} since the epoch is {}".format(s, dt1))
print("Seconds {} since the epoch is {}".format(t, dt2))


