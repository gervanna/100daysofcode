#Create a function that accepts a Date object and returns True 
#if it's Christmas Eve (December 24th) and False otherwise.

import datetime

current_date = datetime.datetime.now()

def milk_and_cookies(date):
    xmas_eve = datetime.datetime(current_date.year, 12, 24)
    if current_date == xmas_eve:
        #print("It's time for milk and cookies.")
        return True
    else:
        #print("No milk and cookies just yet.")
        return False
#milk_and_cookies(current_date)
print("Is it Christmas Eve?", milk_and_cookies(current_date))
