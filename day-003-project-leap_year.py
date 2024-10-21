# a normal year has 365 days
# leap year has 366 days, with an extra day in February

# a year is a leap year if:
# - it is evenly divisible by 4
# - but not evenly divisible by 100, unless evenly divisible by 400
year = int(input('enter year: '))
isLeapYear = False
if year % 4 == 0:
    if year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
        isLeapYear = True
if isLeapYear:
    print(f"year {year} is a leap year")
else:
    print(f"year {year} is not leap")

