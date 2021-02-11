#Write a Python program to accept a filename from the user and print the extension of that.

#02_10_21

name_of_file = (input("Enter the full name of the file: "))
print(f"\nThe name of your file is {name_of_file}.")
name_of_extension = name_of_file.split(".")
print(f"The file extension is {name_of_extension[-1]}.")