alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(msg, shift_num, crypt_direction):
    final_result = ""
    if crypt_direction == "decode":
        shift_num *= -1
    for char in msg:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_num
            final_result += alphabet[new_position]
        else:
            final_result += char
    print(f"The {crypt_direction}d text is {final_result}") 

replay = True
while replay == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    caesar(msg = text, shift_num = shift, crypt_direction = direction)

    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no' ").lower
    if run_again == 'no':
        replay == False
        print("\nGood-bye..")