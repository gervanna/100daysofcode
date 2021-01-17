def collatz(number):
    '''A math sequence that NO ONE understands.'''
    if (number % 2) == 0:
        even = number // 2
        print(even)
        return even
    else:
        number % 2 == 1
        odd = 3 * number + 1
        print(odd)
        return odd
        
trying = True
while trying:
    try:
        user_num = int((input("Please type a number:\n")))
        if user_num <= 0:
            print("You need to type a positive integer.")
            continue
        else:
            while user_num != 1: 
                user_num = collatz(user_num) 
                trying = False
    except ValueError:
        print("You didn't type a positive integer.")
