import calendar

dane = list(map(int, input().split()))
cal = calendar.weekday(dane[2], dane[0], dane[1])
print(calendar.day_name[cal].upper())
