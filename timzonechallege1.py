import pytz
import datetime

available_timezones = {'1': "US/Alaska",
                       '2': "US/Aleutian",
                       '3': "US/Arizona",
                       '4': "US/Central",
                       '5': "US/East-Indiana",
                       '6': "US/Eastern",
                       '7': "US/Hawaii",
                       '8': "US/Indiana-Starke",
                       '9': "US/Michigan", }
for x in available_timezones:
    print("\t{}. {}".format(x, available_timezones[x]))

while True:
    tmz = input("Choose one of up to 9 time zones from a menu (or 0 to Quit): ")

    if tmz == '0':
        break

    if tmz in available_timezones.keys():
        tz_to_display = pytz.timezone(available_timezones[tmz])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print(("The time in {} is {} {}".format(tmz, world_time.strftime('%A %x %X %z'), world_time.tzname())))
        print("Local time in {} is {}".format(tmz,world_time.strftime('%A %x %X %z')))
        print("UTC time in {} is {}".format(tmz, datetime.datetime.utcnow()))
        print()

