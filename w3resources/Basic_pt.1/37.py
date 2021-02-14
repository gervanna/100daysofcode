#Write a Python program to display your details 
#like name, age, address in three different lines.

#02_13_21
import os
import time

name = input("What is your name? ")
age = input("How old are you? ")
address = input("Where do you live? ")

time.sleep(1)
os.system("clear")

print(f"Name: {name}\nAge: {age}\nAddress: {address}")