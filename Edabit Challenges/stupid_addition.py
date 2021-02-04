#Create a function that takes two parameters and, 
#if both parameters are strings, add them as if they were integers 
#or if the two parameters are integers, concatenate them

def stupid_addition(x, y):
    if (type(x) is int) and (type(y) is int) == True:
        return f"Your result is {str(x) + str(y)}."
    elif (type(x) is str) and (type(y) is str) == True:
        return f"Your result is {int(x) + int(y)}."
    else:
        return "Your input is invalid."
print(stupid_addition("1", "3"))
print(stupid_addition(1, 2))
print(stupid_addition("11", 78))