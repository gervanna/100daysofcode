#Write a Python program to get file creation and modification date/times.

#02_14_21

import os
import os.path, time 

print("Created: %s" % time.ctime(os.path.getctime("57.py")))

print("Last modified: %s" % time.ctime(os.path.getmtime("57.py")))

#both print the same date and time.