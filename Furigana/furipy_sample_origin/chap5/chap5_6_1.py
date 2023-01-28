from datetime import date, timedelta
start = date(2021, 6, 1)
for day in range(30):
    curdate = start + timedelta(days=day)
    print(curdate)
