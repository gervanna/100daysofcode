#Write a function that given a year and a month, returns a string 
#with the date (1st Tuesday of every month) of when the new games will be available.

import datetime

current_date = datetime.datetime.now(timezone.utc)
print(current_date.year, current_date.month, current_date.strftime("%A"))


#def game_releases(year, month):
    