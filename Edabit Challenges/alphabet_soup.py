#Create a function that takes a string and 
#returns a string with its letters in alphabetical order.

eg1_txt = "hello"
eg2_txt = "mississippi"

def alphabet_soup(some_txt):
    print(some_txt)
    alphabetical = " ".join(sorted(some_txt))
    print(alphabetical)
    return alphabetical
alphabet_soup(eg1_txt)
alphabet_soup(eg2_txt)
alphabet_soup(input("Bruh, type a word: "))