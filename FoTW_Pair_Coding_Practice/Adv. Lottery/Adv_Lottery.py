import random

pick_numbers = list(range(1, 100)) #turns range into a list of numbers.
random.shuffle(pick_numbers)

buying = True

user_tickets = []
nums_for_tuple = []
num_of_possible_tickets = 3

while buying:

    buy_ticket = input("\nDo you want to buy a lottery ticket? yes or no\n").lower()

    if buy_ticket == "yes":
        for number in range(0, 3):
            removed_nums = pick_numbers.pop(0)
            nums_for_tuple.append(removed_nums)
        
        x = iter(nums_for_tuple)
        result = zip(x, x, x) #breaks the list into tuples 
        user_tickets = list(result)
        number_bought = len(user_tickets)
        print(f"\nYou've bought {number_bought} lotto ticket(s) so far: {user_tickets}")
        
        if num_of_possible_tickets == number_bought:
            print("You can't buy anymore tickets")
            buying = False

    else:
        buying = False
        break

if len(user_tickets) == 0:
    print("\nNo ticket, no chance.")
else:
    print("\nChecking for winning Lottery number......")
    winning_number = random.randint(1, 20)
    if winning_number in user_tickets:
        print(f"\nYou won! The winning number was {winning_number}.")
    else:
        print(f"\nNo winners. The winning number was {winning_number}. Better luck next time.")