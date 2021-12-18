from datetime import datetime, timedelta


weekday = datetime.today()
while weekday.weekday() != 1:
    weekday += timedelta(days=1)

print(weekday)
