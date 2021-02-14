#Write a Python program to concatenate all elements in a list into a string and return it.

#02_13_21

test1 = [1, 5, 12, 2]
test2 = ["I am", 5, "bruv", "lies", 77]
test3 = ["K", "bro", "yeah", "sigh", "Z"]

def strung_together(lst):
    all_together = str(lst)
    result = "".join(all_together)
    print (result)
    return result
strung_together(test1)
strung_together(test2)

# def strung_together(lst):
#     result = ""
#     for element in lst:
#         result += str(element)
#     print(result)
#     return result
# strung_together(test1)
# strung_together(test2)