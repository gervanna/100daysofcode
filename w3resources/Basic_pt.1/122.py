#Write a Python program to empty a variable without destroying it.

#02_17_21

some_int_var = 789
print(type(some_int_var)()) #why?
#type() produces type object for each value, which when called produces an 'empty' new value.

some_str_var = "Jah know"
some_lst_var = [89, "ha"]
some_dict_var = {"John" : "Doe"}
some_tup_var = (5, 7)

var_list = [some_str_var, some_lst_var, some_dict_var, some_tup_var]

print([type(i)() for i in var_list])
#list comprehension - what's to be printed goes 1st then the loop after


# some_int_var = None
# print(some_int_var)
