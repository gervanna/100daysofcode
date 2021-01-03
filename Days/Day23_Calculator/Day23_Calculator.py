import os
from calc_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
  

operations = {"+" : add, 
"-" : subtract, 
"*" : multiply, 
"/" : divide,
}

def calculator():
    print(logo)

    unvalidated_first_num = True
    while unvalidated_first_num:
        try:
            num1 = float(input("\nType the first number? "))
            unvalidated_first_num = False
        except:
            print("That's not a number.")
            continue

    for sign in operations:
        print (sign)

    go_again = True
    while go_again == True:

        unvalidated_operation = True
        while unvalidated_operation:
            operation_sign = input("\nPick an operation: ")
            if operation_sign not in operations:
                print("Choose a valid operation.")
                continue
            else:
                unvalidated_operation = False

        unvalidated_second_num = True
        while unvalidated_second_num:
            try:
                num2 = float(input("\nType the next number? "))
                if operation_sign == "/" and num2 == 0:
                    raise ZeroDivisionError #throw an error
                unvalidated_second_num = False
            except ValueError:
                print("That's not a number.")
                continue
            except ZeroDivisionError:
                print("Cannot divide by Zero.")
                continue 
        
        calc = operations[operation_sign]
        answer = calc(num1, num2)
        print(f"\n{num1} {operation_sign} {num2} = {answer}")
  
        next_calc = input(f"\nType 'y' to continue calculations with {answer}, or type 'n' to start a new calculation, else type 'e' to exit the Calculator: ").lower()
        if next_calc == 'y':
            num1 = answer
        elif next_calc == 'e':
            break
        else:
            go_again = False
            os.system('clear')
            calculator()
    print("\nGoodbye.")

calculator()