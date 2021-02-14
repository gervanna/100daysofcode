#Write a Python program to determine if a Python shell 
#is executing in 32bit or 64bit mode on OS. 

#02_13_21

import sys

max_value = sys.maxsize 
#sys.maxsize shows max value a variable type can take depending on 32 or 64-bit platform

bit_32 = 2**31-1 #32-bit platform
bit_64 = 2**63-1 #64-bit platform

if max_value == bit_32:
    print("Your system is 32-bit.")
else:
    print("Your system is 64-bit.")