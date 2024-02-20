import datetime
def difference(f_d,s_d):
    date_format='%Y-%m-%d %H:%M:%S'
    f_d1=datetime.datetime.strptime(f_d,date_format)
    s_d1=datetime.datetime.strptime(s_d,date_format)
    diff=abs(f_d1-s_d1).total_seconds()
    return diff

f_d=input()
s_d=input()
difference_between_days=difference(f_d,s_d)
print("Difference between the two dates in seconds:", difference_between_days)