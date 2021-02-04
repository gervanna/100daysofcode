#Create a function where given the number n to count down from, and 
#some words txt, return a countdown sequence as a string leading up to the words at the end.
#Put a full stop after each number and uppercase and add an exclamation mark to the word.

import random

num = random.randint(3, 15)
options = ["blast off", "let 'er rip", "boom", "go", "fire", "no", 
"that's a wrap", "buzz", "expelliarmus", "stupefy", "avada kedavra"]
msg = random.choice(options)

def countdown(n, txt):
    for i in range (n, 0, -1):
        print(f"{i}. ", end="")
    print(f"{txt.upper()}!")
(countdown(num, msg))