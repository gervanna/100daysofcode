#Write a Python program to create a histogram from a given list of integers.

#02_15_21

def histogram( items ):
    for num in items:
        if num > 0: #you dont need this check if you know all the numbers are positive
            output = '* ' * num
            print(output)
print("\nHistogram")
histogram([2, 7, 9, 4, 1, 25])



def alt_histogram( items ):
    [ print('@ ' * num) for num in items if num > 0 ] #uses list comprehension

print("\nAlt Histogram")
alt_histogram([2, 7, 1, 12])