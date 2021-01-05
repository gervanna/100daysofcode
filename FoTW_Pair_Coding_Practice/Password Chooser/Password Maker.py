#password maker etc., error keeper
#CHECKS: length, @ least 1 capital, @ least 1 symbol or number
#APPEND ERRORS: not enough characters, no capitals, no symbol or number
#for loops for the checks except length? NO FOR LOOPS used
#while loop encompasses whole code - breaks when LIST IS CHECKED TO BE FOUND EMPTY
#clear screen to restart and remove any errors in list etc., 

import os
import time #imported to use sleep function

get_password = True

while get_password:
    password_errors = []

    print('''\nWelcome to Password Chooser.
Please enter a password with 8 or more characters.
Your password should also have at least 1 capital letter and/or 1 number/symbol to be valid.''')
    
    ask_for_password = input("\nPlease type a password: ")
    #could import and use getpass() in order to not show password being typed

    has_8characters = len(ask_for_password)
    contains_capital = any(map(str.isupper, ask_for_password))
    contains_digit = any(map(str.isdigit, ask_for_password))
    contains_spec_char = ask_for_password.isalnum() #doesn't factor in spaces
    #returns False if any special characters are found

    if has_8characters < 8:
        password_errors.append("Not enough characters in password.")
    if contains_capital == False:
        password_errors.append("Your password should contain a capital letter.")
    if contains_digit == False and contains_spec_char == True: #figuring this out was tricky
        password_errors.append("Your password needs a number or a symbol.")
    if len(password_errors) != 0: #checks if list isn't empty
        print("There were errors. Choose again.\n")
        print(password_errors)
        time.sleep(1) #delay before clearing screen so that print msgs are shown
        os.system("clear")
    else:
        get_password = False
        print("Password Accepted.\nThank you.")
