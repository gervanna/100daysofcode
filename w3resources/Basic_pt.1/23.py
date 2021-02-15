#Write a Python program to get the n (non-negative integer) 
#copies of the first 2 characters of a given string. 
#Return the n copies of the whole string if the length is less than 2. 

#02_14_21

test_str = input("Gimme some words: ")
test_num = int(input("Gimme a number: "))

def two_char_multiply(test_str, test_num):
    if len(test_str) < 2:
        result = (test_str)*test_num
        print(f"Your new string is: {result}.")
        return result
    else:
        result = (test_str[0:2])*test_num + test_str
        print(f"Your new string is: {result}.")
        return result

two_char_multiply(test_str, test_num)