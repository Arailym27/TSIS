#1
import datetime
x=datetime.datetime.now()-datetime.timedelta(days=5)
print(x.strftime("%d"))

#2
import datetime
now=datetime.datetime.now()
yest=now-datetime.timedelta(days=1)
tom=now+datetime.timedelta(days=1)
print(yest)
print(now)
print(tom)

#3
import datetime
now=datetime.datetime.now()
new=now.replace(microsecond=0)
time=now-datetime.timedelta(microseconds=int(now.strftime("%f")))
print(time)
print(new)

#4
import datetime
def shet(time_1,time_2):
    time_form='%Y-%m-%d %H:%M:%S'
    tim1=datetime.datetime.strptime(time_1,time_form)
    tim2=datetime.datetime.strptime(time_2,time_form)
    diff=abs(tim1-tim2).total_seconds()
    return diff



time_1=input()
time_2=input()
print(shet(time_1,time_2))