#Write a Python program to get the 
#least common multiple (LCM) of two positive integers. 

#02_15_21

def lcm(num1, num2):
    n = max(num1, num2)

    while(True): 
        if n % num1 == 0 and n % num2 == 0: # check if both numbers are factors of n
            break
        else:
            n += 1 # n gets bigger and bigger until it becomes a multiple of both

    return n

print("\nLCM\n", lcm(60, 160))
print("\nLCM\n", lcm(5, 7))
print("\nLCM\n", lcm(12, 144))