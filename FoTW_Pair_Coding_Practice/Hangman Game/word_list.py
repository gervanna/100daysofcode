import random
import requests #allows access to HTTP content

def get_random_word():
    '''uses requests to get a list of words from an HTTP 
    then converts to text, splits into individual words and picks one at random'''
    
    url = 'https://www.mit.edu/~ecprice/wordlist.10000' #credit to MIT for this word list
    words = requests.get(url)
    text = words.text #this is one big string of all the words
    individual_word = text.split() #this splits all the words into a list

    return random.choice(individual_word)