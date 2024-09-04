#A Random Password Generator
import tkinter as tk
import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def on_generate_button_click():
    """Handle the button click event."""
    try:
        length = int(entry_length.get())
        if length <= 0:
            result_label.config(text="Length must be positive.")
        else:
            password = generate_password(length)
            result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
label_prompt = tk.Label(root, text="Enter the length of the password:")
label_prompt.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=on_generate_button_click)
button_generate.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
