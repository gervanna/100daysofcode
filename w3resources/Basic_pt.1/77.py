#Write a Python program to test whether the system is 
#a big-endian platform or little-endian platform.

#02_15_21

#Big-endian is an order in which the "big end" (most significant value in the sequence) 
#is stored first (at the lowest storage address). 
#Little-endian is an order in which the "little end" 
#(least significant value in the sequence) is stored first.

import sys

print(sys.byteorder)