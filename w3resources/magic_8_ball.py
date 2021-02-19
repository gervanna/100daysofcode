#Create a Python project of a Magic 8 Ball which is a toy 
#used for fortune-telling or seeking advice.

#Allow the user to input their question.
#Show an in progress message.
#Create 10/20 responses, and show a random response.
#Allow the user to ask another question/advice or quit the game.

#02_18_21

import random
import time
import os

answers = ["As I see it, yes.", "Ask again later.", "Better not tell you now.",
"Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", 
"It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
"Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", 
"Very doubtful.", "Without a doubt.", "Yes", "Yes – definitely.", "You may rely on it."]

magic_response = random.choice(answers)

asking = True

def magic_8_ball(questions):
    '''Takes input from the user and returns randomly chosen answers from list.'''
   
    print(f"\nGravity's 8 Ball is communing with the Oracle.... ")
    time.sleep(1)
    print(f"{magic_response}\n")
    return magic_response

print("\nWelcome to Gravity's 8 Ball.")

while asking: 
    ask_oracle = input("Do you want to talk to the Oracle? Type 'Y' for yes or 'N' for no: ").lower()
    if ask_oracle == 'y':
        questions = input("\nAsk the Oracle a question: ")
        magic_8_ball(questions)
    else:
        asking = False
        print("\nThe Oracle will await your return.... ")