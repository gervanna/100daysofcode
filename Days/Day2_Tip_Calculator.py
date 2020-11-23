#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total of the bill? $"))
tip_options = int(input("What % tip would you like to give? 10, 12 or 15? "))
num_ppl = int(input("How many people are splitting the bill? "))
bill_and_tip = (total_bill * tip_options/100) + total_bill
per_person = round(bill_and_tip / num_ppl, 2)
print(f"Each person should pay ${per_person:.2f}.") 
# {:.2f} string formatting will research further