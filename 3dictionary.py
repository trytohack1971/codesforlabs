import hashlib

# List of commonly used passwords and their variations
common_passwords = [
    "password", "password123", "letmein", "qwerty", "pass" ,
    "123456", "abc123", "admin", "welcome", "monkey", "sunshine"
]
password_variations = [
    "", "123", "1234", "12345", "123456", "1", "@", "S"
]

# Hash of the password to be attacked
hashed_password = hashlib.sha256(b"pass123").hexdigest()

# Try out all possible combinations of common passwords and their variations
password_found = False
for password in common_passwords:
    for variation in password_variations:
        possible_password = password + variation
        hashed_possible_password = hashlib.sha256(possible_password.encode()).hexdigest()

        if hashed_possible_password == hashed_password:
            print(f"Password found: {possible_password}")
            password_found = True
            break

    if password_found:
        break

if not password_found:
    print("Password not found")

