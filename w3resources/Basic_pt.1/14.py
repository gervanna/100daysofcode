#Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)

#02_11_21

import datetime

first_date = datetime.date(2014, 7, 2)
next_date = datetime.date(2014, 7, 11)
days_between = (next_date - first_date)
print(days_between)