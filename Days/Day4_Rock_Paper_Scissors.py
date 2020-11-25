import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_choices = [rock, paper, scissors]

player = int(input("Make a choice: Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS...\n"))
print(game_choices[player])

computer = random.randint(0, 2)
print(f"\nComputer chose:\n{game_choices[computer]}")

if player >= 3 or player < 0:
    print("\nThat wasn't a valid choice. You lose.")
elif player == computer:
    print("\nIt's a draw.")
elif player == 0 and computer == 2:
    print("\nYou win!")
elif computer == 0 and player == 2:
    print("\nYou lose...")
elif computer > player:
    print("\nYou lose...")
elif player > computer:
    print("\nYou win!")








'''
if player == computer:
    print("It's a tie.")
elif player == 0:
    if computer == 2:
        print("Rock wins.")
    else:
        print("Paper wins.")
elif player ==  1:
    if computer == 0:
        print("Paper wins.")
    else:
        print("Scissors wins.")
elif player == 2:
    if computer == 1:
        print("Scissors wins.")
    else:
        ("Rock wins.")      
else:
    print ("That wasn\'t a valid response")
'''