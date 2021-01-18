empty = []
words = ["cat", "dog", "apprentice", "bowl", "lol", "fudgestickles", "boomer"]
numbers = [1, 5, 99, 0, 89, 12, -2, 1000, 3.14]
single_number = [4]
single_word = ["Kojo"]
some_words = ["muggles", "wizards"]
mixed = ["Lmao", 34, "a", ("a tuple:", "grapes", "apples"), 3.14, ["a list:", "bruv", "innit"]]

def commacode(lst):
    if len(lst) == 1: #checks if list is only a single item
        print("".join(map(str, lst))) #prints single item as string
        #"".join(lst) only works in printing items that aren't numerical
        #using map function factors in if the single element in the list is also a number type
        return #returns to stop rest of code from running

    try: 
        for item in range(len(lst) -2):
            print(lst[item], end=", ")
        print(f"{lst[-2]}", "and", f"{lst[-1]}" + ".")
    except IndexError:
        print("Your list is empty. Try again.")

def run_examples():
    print("\nThe following program shows examples of taking lists \
and returning strings, \nwith the items separated by a comma and a space, \
with 'and' inserted before the last item.")
    print("\nExample with an empty list:")
    commacode(empty)
    print("\nExample with a list of words:")
    commacode(words)
    print("\nExample with a list of numbers:")
    commacode(numbers)
    print("\nExample with a single number list:")
    commacode(single_number)
    print("\nExample with a single word list:")
    commacode(single_word)
    print("\nExample with a list of two items:")
    commacode(some_words)
    print("\nExample with a list of mixed types: ")
    commacode(mixed)
run_examples()

#exception raised for empty list as the indexing throws error
#similarly checks if list is only 1 first as indexing would also throw error
#works fine if list is two or more items
#.isdigit doesn't work on lists
#fstrings makes it work with a list of numbers!
#doesn't work with a single number list though