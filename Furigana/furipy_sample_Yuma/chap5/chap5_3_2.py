from datetime import date, timedelta
dayname = '月火水木金土日'
start = date(2021, 6, 18)
for day in range(14):
    curdate = start + timedelta(days=day)
    wd = curdate.weekday()
    print(curdate, dayname[wd])