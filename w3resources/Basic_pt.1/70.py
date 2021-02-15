#Write a Python program to sort files by date.

#02_15_21

import glob #the glob module is used to retrieve files/pathnames matching a specified pattern. 
import os

files = glob.glob("*.txt") #insert relative path here
files.sort(key=os.path.getmtime) #getmtime sorts by date modified
print("\n".join(files))


