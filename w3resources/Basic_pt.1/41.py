#Write a Python program to check whether a file exists.

#02_13_21

import os.path

open("39.py", "w")
print("Is it a file:", (os.path.isfile("39.py")))

#without open you have to use full or relative path to check if file exists