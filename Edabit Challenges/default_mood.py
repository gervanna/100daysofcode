#Create a function that takes in a current mood and 
#return a sentence in the following format: "Today, I am feeling {mood}". 
#However, if no argument is passed, return "Today, I am feeling neutral".

def feeling_today(mood = "neutral"):
    if mood == "":
        return(f"Today I am feeling {feeling_today()}.")
    else:
        print(f"Today I am feeling {mood}.")
    return mood
feeling_today((input("\nHow're you feeling today? ")))