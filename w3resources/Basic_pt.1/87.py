#Write a Python program to get the size of a file.

#02_16_21

import os

def size_of_file(txt):
    txt_stats = os.stat(txt)
    txt_size = round(txt_stats.st_size / (1024 * 1024), 2)
    print(f"File size is: {txt_size} MBs.")
    return txt_size
size_of_file("39.py") #7.1MB
size_of_file("39.py") #1.2MB
