#Write a Python program to print the calendar of a given month and year.
#Note : Use 'calendar' module.

#02_11_21

import datetime
import calendar

print("\nCalendar example with a specific year and month:\n")
year1 = 1993
month1 = 1
print(calendar.month(year1, month1))

current = datetime.datetime.now()
print(f"Current date and time: {current}")

print("\nCalendar example using the datetime module:\n")
year2 = current.year
month2 = current.month
print(calendar.month(year2, month2))


