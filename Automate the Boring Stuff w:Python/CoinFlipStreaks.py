import random

streaks = 0

def the100():
    heads_tails = []
    for _ in range(100):
        heads_tails.append(random.randint(0, 1))
    return heads_tails
print(the100())
flips  = the100()

def streak_finder(flips):
    