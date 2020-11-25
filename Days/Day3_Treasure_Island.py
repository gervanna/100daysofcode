class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;93m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

print(f'''
{color.BOLD}
____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------
{color.END}
''')

print(f"\n\n\t\t{color.BOLD}Welcome to Treasure Island.{color.END} \nWhere all your dreams come true, or your luck runs out.")
print("\nYour mission is to find the treasure. \nMake good choices and be rewarded, or choose poorly and be doomed.")

print("\nYou wake up on a cold hard floor. You can hear the sound of dripping water and can make out two pathways on your left and on your right.")
step1 = input(f"Which path do you take? {color.BOLD}Left{color.END} or {color.BOLD}Right{color.END}?\n")
step1_l = step1.lower()
if step1_l == "left":
    print("\nYou see a light ahead of your path and follow it to a river. The waters seem cool and calm.")
    step2 = input(f"Do you {color.BOLD}Swim{color.END} or {color.BOLD}Wait{color.END}?\n")
    step2_l = step2.lower()
    if step2_l == "wait":
        print("\nA boat floats down onto the river bank, and you use it to get safely to the other side.")
        print("When you get off the boat, you see three different coloured doors blocking your path.")
        step3 = input(f"Which door do you choose? {color.RED}Red{color.END}, {color.YELLOW}Yellow{color.END} or {color.BLUE}Blue{color.END}?\n")
        step3_l = step3.lower()
        if step3_l == "yellow":
            print(f'''\n  {color.BOLD}           
         __________
        /\____;;___/
       | /         /
       `. ())oo() .
        |\(%()*^^()^|
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|

            {color.END}\n''')
            print(f"\n\t\t{color.BOLD}YOU WIN!{color.END}\nThe treasure is yours. Here, have a cookie too.")
        elif step3_l == "red":
            print(f"\nYou enter the room and are burned by fire... {color.BOLD}GAME OVER!{color.END}")
        elif step3_l == "blue":
            print(f"\nYou enter the room and are eaten by a scary Gruffalo... {color.BOLD}GAME OVER!{color.END}")
        else:
            print(f"\nNo luck... {color.BOLD}GAME OVER!{color.END}")            
    else:
        print(f''' 
        {color.BOLD}{color.GREEN}
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
        {color.END}{color.END}
        ''')
        print(f"\nYou are attacked by a crocodile... {color.BOLD}GAME OVER!{color.END}")   
else:
    print(f"\nYou set off a booby trap and fall into a hole filled with spikes... \n\t\t\t{color.BOLD}GAME OVER!{color.END}")

#https://ascii.co.uk/art used for art throughout the game
#https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3
#above stackoverflow reference for color in python