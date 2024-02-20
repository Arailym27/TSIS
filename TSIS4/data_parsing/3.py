import datetime
now=datetime.datetime.now()
micr=int(now.strftime("%f"))
new=now-datetime.timedelta(microseconds=micr)
time = now.replace(microsecond=0)
print(now)
print(new)
print(time)

