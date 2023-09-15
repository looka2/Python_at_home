from datetime import datetime, time
from time import sleep
import os


def dateDiffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def daysHoursMinutesSecondsFromSeconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return days, hours, minutes, seconds


req = datetime.strptime('2024-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
now = datetime.now()

while req > now:
    print("Happy new year in %dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req)))
    sleep(1)
    now = datetime.now()


print("Done")

