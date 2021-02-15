#Write a Python program to convert seconds to day, hour, minutes and seconds.

#02_14_21

print("Enter the amount of seconds in order to convert to minutes, hours and days.")

seconds = int(input("Enter the total amount of seconds: "))

secs_to_days = seconds // 3600 // 24
days_remainder = seconds % (3600 * 24)

secs_to_hours = days_remainder // 3600
hours_remainder = days_remainder % 3600

secs_to_minutes = hours_remainder // 60
mins_remainder = hours_remainder % 60

sec_remainder = mins_remainder


print(f"{seconds} seconds is {secs_to_days} days, {secs_to_hours} hours and {secs_to_minutes} minutes and {sec_remainder} seconds.")