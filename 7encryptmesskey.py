def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26  # Ensure the shift is within the range of 0-25
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are added without change
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

# Example usage:
plaintext = "Hello, World!"
shift = 3
encrypted = encrypt_caesar(plaintext, shift)
print(f"Encrypted: {encrypted}")
decrypted = decrypt_caesar(encrypted, shift)
print(f"Decrypted: {decrypted}")

