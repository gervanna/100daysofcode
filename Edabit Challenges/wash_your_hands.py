#It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
#Create a function that takes the number of times a 
#person washes their hands per day N and the number of months 
#they follow this routine nM and calculates the duration in minutes 
#and seconds that person spends washing their hands.

SECONDS_PER_WASH = 21
DAYS_OF_MONTH = 30

def wash_your_hands(times_per_day, months_of_routine):
    seconds_per_day = times_per_day * SECONDS_PER_WASH
    seconds_total = seconds_per_day * DAYS_OF_MONTH * months_of_routine

    minutes_total = seconds_total // 60

    seconds_remaining = seconds_total % 60

    return (minutes_total, seconds_remaining)

answer = wash_your_hands(7, 9)
print(f"The time is {answer[0]} minutes and {answer[1]} seconds.")