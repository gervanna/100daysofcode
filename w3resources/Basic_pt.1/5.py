#Write a Python program which accepts the user's first and last name 
#and print them in reverse order with a space between them
#02_10_21

name = []
f_name = input("What is your first name? ").capitalize()
name.append(f_name)
l_name = input("What is your last name? ").capitalize()
name.append(l_name)

first_last_name = " ".join(name)

print(f"Your name is {first_last_name}.")

name_reverser = name[::-1]
reversed_name = " ".join(name_reverser)

print(f"\nYour name in reverse is {reversed_name}.")