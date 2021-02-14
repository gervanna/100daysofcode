#Write a python program to get the path and name of the file that is currently executing.

#02_13_21

import os
print("Current File Name:",os.path.realpath(__file__))
