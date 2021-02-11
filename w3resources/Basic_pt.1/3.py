#Write a Python program to display the current date and time.
#02_10_21

import datetime

right_now = datetime.datetime.now()
formatted_date_time = right_now.strftime("%Y/%m/%d, %I:%M %p") 
#formatted year, month, day, hour(I for 12hr clock), minutes, %p - AM/PM)

print(f"Date and time right now:\n{formatted_date_time}")