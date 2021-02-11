#Write a Python program to display the examination schedule.
#02_10_2021

import datetime

exam_date = (11, 12, 2014) #tuple

Year_extracted = exam_date[2]
Month_extracted = exam_date[1]
Day_extracted = exam_date[0]
#extracting the date elements from the tuple

exam_schedule = datetime.date(Year_extracted, Month_extracted, Day_extracted) 
#this is now a date time object

print("The examination will be on", exam_schedule.strftime("%A - %d/%m/%Y")+".")