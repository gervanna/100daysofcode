import random

streaks = 0
heads_tails = []

for experiment in range(10000): #amount of times the program runs
    for flip in range(100): #number of random flips 
        if random.randint(0, 1) == 0:
            heads_tails.append("heads")
        else:
            heads_tails.append("tails")
    