import tkinter as tk
from tkinter import messagebox
import base64

def encrypt_decrypt(action):
    password = code_entry.get()
    if password != "1234":
        messagebox.showerror("Error", "Invalid password")
        return
    
    message = text_input.get("1.0", tk.END).strip()
    if action == "encrypt":
        result = base64.b64encode(message.encode()).decode()
        result_label.config(text="Encrypted Message")
    else:
        result = base64.b64decode(message.encode()).decode()
        result_label.config(text="Decrypted Message")
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

def main_screen():
    global text_input, code_entry, result_label, result_text
    
    root = tk.Tk()
    root.title("Simple Encrypt/Decrypt")
    root.geometry("400x400")
    
    tk.Label(root, text="Enter text:").pack(pady=5)
    text_input = tk.Text(root, height=5, width=50)
    text_input.pack(pady=5)
    
    tk.Label(root, text="Enter password:").pack(pady=5)
    code_entry = tk.Entry(root, show='*', width=20)
    code_entry.pack(pady=5)
    
    tk.Button(root, text="Encrypt", command=lambda: encrypt_decrypt("encrypt")).pack(pady=5)
    tk.Button(root, text="Decrypt", command=lambda: encrypt_decrypt("decrypt")).pack(pady=5)
    
    result_label = tk.Label(root, text="Result:")
    result_label.pack(pady=5)
    
    result_text = tk.Text(root, height=5, width=50)
    result_text.pack(pady=5)
    	
    root.mainloop()

main_screen()

