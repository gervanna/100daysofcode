#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#example - Sample value of n is 5 and Expected Result : 615

#02_11_21

def weird_addition(num):
    '''Takes an int and returns the value for n + nn + nnn.
    Example - num is 5, (n+nn+nnn) 5+55+555 = 615'''
    n = num
    nn = int((f"{num}")*2)
    nnn = int((f"{num}")*3)
    result = n + nn + nnn
    print(f"Your result is {result}.")
    return result

usr_num = input("Type an integer: ")

try:
    usr_int = int(usr_num)
    weird_addition(usr_int)
except:
    print("You did not type an integer. Goodbye.")
