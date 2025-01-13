import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    # Check for length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password must be at least 8 characters long.")
    
    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password must contain at least one uppercase letter.")
    
    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password must contain at least one lowercase letter.")
    
    # Check for digit
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password must contain at least one number.")
    
    # Check for special character
    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        feedback.append("Password must contain at least one special character (e.g., @$!%*?&).")
    
    # Check for common patterns
    common_patterns = ['12345', 'password', 'qwerty', 'abc123']
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Password is too common, try a more unique one.")
    else:
        strength += 1

    # Provide feedback
    if strength < 3:
        feedback.append("Password is weak.")
    elif strength == 5:
        feedback.append("Password is medium.")
    else:
        feedback.append("Password is strong.")
    
    return strength, feedback

# Function to update password strength dynamically as the user types
def update_password_strength(event=None):
    password = password_entry.get()  # Get the password from the input field
    if password == "":
        return  # Don't evaluate if the password field is empty
    
    strength, feedback = check_password_strength(password)

    # Clear previous feedback
    feedback_text.delete(1.0, tk.END)

    # Display feedback
    for line in feedback:
        feedback_text.insert(tk.END, line + "\n")

    # Update strength score
    strength_label.config(text=f"Password Strength Score: {strength}/6")

    # Update background color based on strength
    if strength < 3:
        strength_message = "Weak password. Please consider making it stronger."
        root.config(bg="red")
    elif strength == 3 or 4:
        strength_message = "Medium strength password. Consider adding more variety."
        root.config(bg="yellow")
    else:
        strength_message = "Strong password. Good job!"
        root.config(bg="green")
    
    # Display strength message
    strength_message_label.config(text=strength_message)

# Function to clear the password entry field and reset feedback
def clear_password():
    password_entry.delete(0, tk.END)
    feedback_text.delete(1.0, tk.END)
    strength_label.config(text="Password Strength Score: 0/6")
    strength_message_label.config(text="")
    root.config(bg="white")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Set window size
root.geometry("400x450")
root.config(bg="white")

# Label for instructions
instruction_label = tk.Label(root, text="Enter a password to check its strength:", bg="white")
instruction_label.pack(pady=10)

# Entry widget to enter the password
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", update_password_strength)  # Update strength dynamically on typing

# Button to evaluate password strength
evaluate_button = tk.Button(root, text="Check Strength", command=update_password_strength)
evaluate_button.pack(pady=10)

# Button to clear the password field
clear_button = tk.Button(root, text="Clear", command=clear_password)
clear_button.pack(pady=10)

# Label to display the strength score
strength_label = tk.Label(root, text="Password Strength Score: 0/6", bg="white")
strength_label.pack(pady=5)

# Label to display strength message
strength_message_label = tk.Label(root, text="", bg="white")
strength_message_label.pack(pady=5)

# Text widget to display feedback on password strength
feedback_text = tk.Text(root, width=40, height=10, wrap=tk.WORD, bg="lightgray")
feedback_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
