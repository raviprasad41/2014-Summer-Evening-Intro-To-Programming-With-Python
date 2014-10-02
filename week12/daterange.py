from datetime import datetime, timedelta
d = datetime.now()
delta = timedelta(days=0.5)

#round to midnight today
current = datetime(d.year, d.month, d.day)

print dir(current)

for i in range(0,60):
    print i + 1
    print current.isoformat()
    # print current.strftime("%Y-%m-%d %H:%M:%S")
    current -= delta