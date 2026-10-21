# A magic date is a date where the date multiplied by the month is equal to the two-digit
# year. For example, June 10, 1960 is a magic date because June is the sixth month, and
# 6 times 10 is 60 which is the two-digit year. Write a function that determines whether
# or not a date is a magic date. Use your function to create a main program that finds
# and displays all of the magic dates in the 20th century?
def magic_date(day, month, year):
    if day * month == year % 100:
        return True
    else:
        return False


for year in range(1901, 2001):
    for month in range(1, 13):
        for day in range(1, 32):
            if magic_date(day, month, year):
                print(day, month, year)
