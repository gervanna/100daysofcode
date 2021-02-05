#A number is said to be Harshad if it's exactly divisible by the sum of its digits. 
#Create a function that determines whether a number is a Harshad or not.

def Harshad(num):
    num = int(num)
    sum_of_digits = sum(map(int, str(num)))
    if num % sum_of_digits == 0:
        print(f"\nYes Bruv. {num} is Harshad.")
    else:
        print(f"\nNah fam. {num} is not Harshad.")
Harshad(12)
Harshad(89)
Harshad(171)
Harshad(input("\nType a number: "))