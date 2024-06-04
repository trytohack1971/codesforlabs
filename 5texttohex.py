def text_to_hex(text):
    hex_output = ""
    for char in text:
        hex_output += format(ord(char), "02x") + " "
    return hex_output.strip()

text_message = "Hello, World!"
hexadecimal_representation = text_to_hex(text_message)
print(f"Text: {text_message}")
print(f"Hexadecimal: {hexadecimal_representation}")

