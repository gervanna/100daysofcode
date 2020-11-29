import random
from Day7_Hangman_Art import stages
from Day7_Hangman_Art import logo
import requests #allows access to HTTP content
url = 'https://www.mit.edu/~ecprice/wordlist.10000' #credit to MIT for this word list
words = requests.get(url)
text = words.text #this is one big string of all the words
individual_word = text.split() #this splits all the words into a list

chosen_word = random.choice(individual_word) #random word saved as variable
x = len(chosen_word) #length of random word
game_over = False #states premise for while loop
lives = 6

print(logo)
print("\n\t\tWelcome to Hangman.\n\nGuess letters one by one to solve the word.\nYou win if you guess the word. You lose if the character gets hung. GOOD LUCK!\n\n")
print(f'Pssst, the solution is {chosen_word}.')

display = [] #empty list to store blanks
for y in range(x): #loops through length to add as many blanks as letters in word
    display.append("_") 

while game_over == False:
    guess = input("Guess a letter: ").lower() #lowers input before checking
    for position in range(x):
        #this loop finds the position, assigns it then replaces it with guess or not
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = guess
            if guess == guess:
                print(f"You already guessed {guess}")
    if guess not in chosen_word: #decrements lives
        print(f"You guessed {guess}. That's not in the word. You lose a life.")
        lives -= 1
        if lives == 0: #also quits the loop if lives hits zero
            game_over = True
            print("\nYou lose...\nGame over.")
    print(" ".join(display)) #prints as string not list
    if "_" not in display: #gives condition for ending loop
        game_over = True
        print("\nYou win!\nGame Over.")
    print(stages[lives]) #prints images to show hangman happening with lives lost