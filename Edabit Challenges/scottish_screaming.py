#A strong Scottish accent makes every vowel similar to an "e", 
#so you should replace every vowel with an "e". 
#Additionally, it is being screamed, so it should be in block capitals.
#Create a function that takes a string and returns a string.

def scottish_screaming(some_text):
    print(some_text)
    vowels = ['a', 'i', 'o', 'u']

    scottish = ""
    for letter in some_text:
        if letter in vowels:
            #some_text.replace(letter, "E")
            scottish = scottish + "e"
        else:
            scottish = scottish + letter

    screaming = scottish.upper()
    print(screaming)
    return screaming
scottish_screaming("hello bredda bredda!")
scottish_screaming("hello bredda bredda I cannot see you!")
scottish_screaming(input("\nType something here and test it yourself: "))