#Write a python program to access environment variables. 

#02_13_21

import os

print(os.environ)
#no idea wtf is happening or this is doing

for k, v in os.environ.items():
    print(f'{k}={v}')