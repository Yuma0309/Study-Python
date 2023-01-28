from datetime import date, timedelta
start = date(2021, 6, 1)
for day in range(0, 30, 7):
    curdate = start + timedelta(days=day)
    print(curdate)
