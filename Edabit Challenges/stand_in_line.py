#Write a function that takes a list and a number as arguments. 
#Add the number to the end of the list, then remove the first element of the list. 
#The function should then return the updated list.

eg1 = [4, 5, 8, 2, 45, 9]
eg2_empty = []

def stand_in_line(lst, num):
    if lst == []:
        print("No list selected.")
    else: 
        print(lst)
        lst.append(num)
        lst.pop(0)
        print(lst)
    return lst
stand_in_line(eg1, 77)
stand_in_line(eg2_empty, 3)