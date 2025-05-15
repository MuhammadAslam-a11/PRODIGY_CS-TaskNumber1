def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26  # Handle cases where shift is larger than 26
            new_char = chr((ord(char) + shift_amount - ord('a')) % 26 + ord('a')) if char.islower() else \
                       chr((ord(char) + shift_amount - ord('A')) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char  # Non-alphabetic characters remain unchanged
    return encrypted_message

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)  # Decrypting is just encrypting with a negative shift

def main():
    message = input("Enter a message to encrypt: ")
    shift = int(input("Enter shift value: "))
    
    encrypted = encrypt(message, shift)
    print(f"Encrypted Message: {encrypted}")
    
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
