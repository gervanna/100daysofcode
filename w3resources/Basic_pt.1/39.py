#Write a Python program to compute the future value of a 
#specified principal amount, rate of interest, and a number of years.

#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output : 12722.79

#02_13_21

principal = 10000
interest_rate = 3.5/100
compounded = 12
time = 7

acurred_amt = principal * (1 + interest_rate/compounded)**(compounded*time)
print(round(acurred_amt, 2))