from datetime import date, timedelta
start = date(2021, 6, 18)
for day in range(14):
    curdate = start + timedelta(days=day)
    print(curdate)