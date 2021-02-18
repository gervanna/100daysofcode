#Write a Python program to get the identity of an object.

#02_17_21

#Python id() function returns the “identity” of the object. 
#The identity of an object is an integer, which is guaranteed 
#to be unique and constant for this object during its lifetime.


some_str_var = "Sneaky fox"
some_int_var = 5667
some_list_var = ["Kool kat", 98, 6.78, ["A", "B", "C"]]

print(f"This is the ID for {some_str_var}: {id(some_str_var)}.")
print(f"This is the ID for {some_int_var}: {id(some_int_var)}.")
print(f"This is the ID for {some_list_var}: {id(some_list_var)}.")

#the id changes everytime I run it. Is it supposed to do that?