#It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
#Create a function that takes the number of times a 
#person washes their hands per day N and the number of months 
#they follow this routine nM and calculates the duration in minutes 
#and seconds that person spends washing their hands.

def wash_your_hands(times_per_day, months_of_routine):
    seconds = times_per_day * 21
    minutes = seconds / 60
    days = minutes * 30
    total_time = days * months_of_routine
    print(total_time)
    return total_time
wash_your_hands(7, 9)

#incomplete