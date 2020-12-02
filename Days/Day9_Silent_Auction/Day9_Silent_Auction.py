import os 
from auc_art import logo


bidders = {}

still_bidding = True
while still_bidding == True:
    print("\n\t\tWelcome to the Silent Auction\n")
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid #adds name and bid to dictionary as key:value

    max_name = max(bidders, key=bidders.get) #gets the person with the max bid
    all_values = bidders.values() #stores all the bids in a variable
    max_bid = max(all_values)    #gets the max bid amounts
    
    next_bidder = input("\nAre there any other bidders? Type 'yes' or 'no': ").lower()
    if next_bidder == 'no':
        still_bidding = False
        print(f"\nThe winner of the Silent Auction is {max_name} with a bid of ${max_bid}.\nCongratulations!")
        #prints max bidder
    elif next_bidder == 'yes':
        os.system('clear') #clears screen in anticipation of next bidder