#Write a Python program to convert all units of time into seconds.

#02_14_21

print("Please enter a time in numbers for each prompt. If not applicable enter the number 0.")

days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

days_to_sec = days * 24 * 3600
hours_to_sec = hours * 3600
minutes_to_sec = minutes * 60

time = days_to_sec + hours_to_sec + minutes_to_sec + seconds

print(f"The total amount of seconds: {time}.")