import random

number_of_streaks = 0
streaks = 0

def the100():
    heads_tails = []
    for _ in range(100):
        heads_tails.append(random.randint(0, 1))
    return heads_tails

flips  = the100()
print(flips)

def streak_finder(flips):
    