alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(text,shift,direction):
    plain_text = ""
    for i in text:
        if i in alphabet:
            # if the letter in text matches with the letter in the alphabet the it will get the index of the letter in the alphabet else it will add to encrypt_letter as it is.
            letter_index = alphabet.index(i)
            if direction == "encode":
                # this will prevent index error
                try:
                    # adding shift amount to the letter index so that it shifts forward
                    plain_text += alphabet[letter_index+shift]
                except IndexError:
                    # this gives the remainder which is the shifed index and prevents index error 
                    plain_text += alphabet[(letter_index+shift) % len(alphabet)]
            elif direction == "decode":
                try:
                    # substracting shift amount to the letter index so that it shifts backward
                    plain_text += alphabet[letter_index-shift]
                except IndexError:
                    # this gives the remainder which is the shifed index and prevents index error 
                    plain_text += alphabet[(letter_index-shift) % len(alphabet)]
            else:
                print("Please type a valid code to encode or decode")
        else:
            plain_text += i

    print(f"The {direction} text is {plain_text}")


carry_on = True
while carry_on:
    user_input = input("Do you want to continue type yes or no\n").lower()
    if user_input == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        default_number = True
        while default_number:
            shift = int(input("Type the shift number:\n"))
            if shift == 26:
                print("type in another number to encode or decode") 
            else:
                default_number = False       
        ceaser(text,shift,direction)
    elif user_input == "no":
        carry_on = False
    else:
        print("Type yes or no to continue")