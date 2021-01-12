#create secret word - list or string???
#create empty list to track correctly guessed letters
#create guess counter
#ask for guess from user
#iterate to check if letter guessed match any in secret word - 
    #if yes 
            #append letter to empty list
            #print the letter
            #check if word is solved - 
                    #if no, loop to get another guess
                    #if yes, you won game - END
    #if no
            #print an *
            #check if guess counter is zero - 
                    #if no, print incorrect guess msg, loop to get another guess
                    #if yes, you lost game - END
#game ends if word is guessed correctly or if user guess wrong three times.

import word_list

secret_word = word_list.get_random_word()
word_length = len(secret_word)
letters_guessed = []
num_of_guesses = 3

game_play = True

print(f'''\nWelcome to HANGMAN. Reveal the word by guessing letters. 
You only have 3 lives, so guess wisely!
Here's a clue: The word secret word is {word_length} letters long.\n''')

def word_display():
    '''iterates through secret_word, 
    if letter guessed in secret_word prints letter, else print *'s'''

    for letter in secret_word:
        if letter in letters_guessed:
            print(letter, end=" ")
        else:
            print("*", end=" ")
word_display()

while game_play:
    
    guess_letter = input("\n\nGuess a letter: ").lower()

    if guess_letter.isalpha()==True and guess_letter in secret_word: 
        #checks if input is a letter and if in secret word
        letters_guessed.append(guess_letter)
        word_display()

    else:
        num_of_guesses -= 1
        print("\nIncorrect guess. You lost a life.")
        print(f"Lives remaining: {num_of_guesses}")

    if num_of_guesses == 0:
        game_play = False
        print("\nSorry you lost.")
        print(f"\nThe secret word was: {secret_word}.")

    did_they_win = True
    for letter in secret_word:
        if not letter in letters_guessed:
            did_they_win = False

    if did_they_win:
        game_play = False
        print("\nYou won!")
        print(f"\nThe secret word was: {secret_word}.")
    else:
        continue
