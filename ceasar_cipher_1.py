alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    encrypt_letter = ''
    for i in text:
        # if the letter in text matches with the letter in the alphabet the it will get the index of the letter in the alphabet else it will add to encrypt_letter as it is.
        if i in alphabet:
            letter_index = alphabet.index(i)
            # this will prevent index error
            try:
                # adding shift amount to the letter index so that it shifts forward
                encrypt_letter += alphabet[letter_index+shift]
            except IndexError:
                # this gives the remainder which is the shifed index and prevents index error 
                encrypt_letter += alphabet[(letter_index+shift) % len(alphabet)]
        else:
            encrypt_letter += i
    print(f"The encoded text is {encrypt_letter}")

def decrypt(text,shift):
    decrypt_letter = ''
    for i in text:
        if i in alphabet:
            letter_index = alphabet.index(i)
            # this will prevent index error
            try:
                # substracting shift amount to the letter index so that it shifts backward
                decrypt_letter += alphabet[letter_index-shift]
            except IndexError:
                # this gives the remainder which is the shifed index and prevents index error 
                decrypt_letter += alphabet[(letter_index-shift) % len(alphabet)]
        else:
            decrypt_letter += i
    print(f"The encoded text is {decrypt_letter}")


  
if direction  == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("Please type a valid code to encode or decode") 
