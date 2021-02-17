#Write a Python program to check whether a file path is a file or a directory.

#02_16_21

import os.path

def which_path(txt):
    if os.path.isdir(txt) == True:
        print("This is a directory.")
    elif os.path.isfile(txt) == True:
        print("This is a file.")
    else:
        print("Different type of file. Please verify extension.")
which_path("39.py")#insert relative or full path here