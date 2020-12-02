import os
from auc_art import logo


bidders = {}

still_bidding = True
while still_bidding == True:
    print("\n\t\tWelcome to the Silent Auction\n")
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    max_name = max(bidders, key=bidders.get)
    all_values = bidders.values()
    max_bid = max(all_values)    
    
    next_bidder = input("\nAre there any other bidders? Type 'yes' or 'no': ").lower()
    if next_bidder == 'no':
        still_bidding = False
        print(f"\nThe winner of the Silent Auction is {max_name} with a bid of ${max_bid}.\nCongratulations!")
    elif next_bidder == 'yes':
        os.system('clear')