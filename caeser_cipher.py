alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:  # Check if character is a letter
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char  # Keep spaces and symbols unchanged
    print(f"Encrypted text: {cipher_text}")
    return cipher_text

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:  # Check if character is a letter
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char  # Keep spaces and symbols unchanged
    print(f"Decrypted text: {plain_text}")
    return plain_text

# Main program loop
end_program = False
while not end_program:
    what_to_do = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift key:\n"))

    if what_to_do == "encrypt":
        encryption(text, shift)
    elif what_to_do == "decrypt":
        decryption(text, shift)
    else:
        print("Invalid input. Please enter 'encrypt' or 'decrypt'.")

    play_again = input("Type 'yes' to continue, type 'no' to end: ").lower()
    if play_again == 'no':
        end_program = True
        print("Hope you enjoyed the game!")
