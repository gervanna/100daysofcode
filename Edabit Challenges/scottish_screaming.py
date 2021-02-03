#A strong Scottish accent makes every vowel similar to an "e", 
#so you should replace every vowel with an "e". 
#Additionally, it is being screamed, so it should be in block capitals.
#Create a function that takes a string and returns a string.

def scottish_screaming(some_text):
    vowels = ['a', 'i', 'o', 'u']
    for letter in some_text:
        if letter in vowels:
            scottish = some_text.replace(letter, "E")
    print(some_text)
    screaming = scottish.upper()
    print(screaming)
    return screaming
scottish_screaming("hello bredda bredda!")
scottish_screaming("hello bredda bredda I cannot see you!")

#doesn't replace all instances
