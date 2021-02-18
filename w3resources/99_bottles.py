#Create a Python project that prints out every line of the song "99 bottles of beer on the wall." 
#Note: Try to use a built in function instead of manually type all the lines.

#02_17_21

'''One-hundred bottles of beer on the wall,
One-hundred bottles of beer!
Take one down,
Pass it around,
Ninety-nine bottles of beer on the wall!'''


for i in range(100, 0, -1):
    print(f'''{i} bottles of beer on the wall,
    {i} bottles of beer!
    Take one down,
    Pass it around,
    {(i - 1)} bottles of beer on the wall!\n''')

#edit for grammar re bottles and to print new final line:
#No more bottles of beer on the wall!



#mostly complete