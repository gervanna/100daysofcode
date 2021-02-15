#Write a Python program to get a directory listing, sorted by creation date.

#02_15_21

import os

directories = os.listdir(".") #"." represents current directory
directories.sort(key= os.path.getctime)
print("\n".join(directories))