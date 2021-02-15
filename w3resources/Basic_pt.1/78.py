#Write a Python program to find the available built-in modules.

#02_15_21

# print(__builtins__.__doc__, "\n")
# built = dir(__builtins__)
# print("\n".join(built))
#printed builtin functions etc. not modules

import sys

names_of_modules = sys.builtin_module_names
print("\n".join(names_of_modules))