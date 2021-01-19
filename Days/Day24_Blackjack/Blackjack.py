import random
import os

def deal_card():
    '''Deals a random card from the deck'''
    cards = [11, 2, 3 ,4 ,5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    