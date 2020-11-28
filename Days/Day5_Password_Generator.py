#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for n in range(nr_letters):
    x = random.sample(letters, n+1) 
    #used random.sample cuz .choice kept throwing an error
for n in range(nr_symbols):
    y = random.sample(symbols, n+1)
for n in range(nr_numbers):
    z = random.sample(numbers, n+1)
password = x+y+z
print("Here is your password:", "".join(password)) 
#"".join prints as a string without the list brackets and commas



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for n in range(nr_letters):
    x = random.sample(letters, n+1)
for n in range(nr_symbols):
    y = random.sample(symbols, n+1)
for n in range(nr_numbers):
    z = random.sample(numbers, n+1)
password = x+y+z
random.shuffle(password) #shuffle to randomize numbers before printing out password
print("Here is your password:", "".join(password))