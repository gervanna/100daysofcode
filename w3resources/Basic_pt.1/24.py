#Write a Python program to test whether a passed letter is a vowel or not.

#02_13_21

vowels = ["a", "e", "i", "o", "u"]

def is_vowel(letter):
    if letter in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is not a vowel.")
is_vowel(input("Type a letter to check if it's a vowel or nah: "))
    