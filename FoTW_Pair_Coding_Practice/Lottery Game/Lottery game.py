#basic lotto program checker etc.,

import random

tickets_bought = []

get_ticket = True

while get_ticket == True:
    buy_ticket = input("Do you want to buy a lotto ticket? yes or no \n").lower()

    if buy_ticket == "yes":
        lotto_number = random.randint(1, 20)
        tickets_bought.append(lotto_number)
    else:
        get_ticket = False

winning_lotto_number = random.randint(1, 20) #generates random lotto # for winnings
if winning_lotto_number in tickets_bought:
    print (f"You won!\nYour ticket number was {tickets_bought} and the winning number was {winning_lotto_number}")
else:
    print (f"You lost.\nYour ticket number was {tickets_bought} and the winning number was {winning_lotto_number}")
            
