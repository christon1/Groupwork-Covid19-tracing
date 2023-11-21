import tkinter as tk
from tkinter import messagebox
import hashlib
import json
import re  # Import for regular expression handling

class UserLoginWindow:
    def __init__(self, parent, on_success):
        self.parent = parent
        self.on_success = on_success

        self.login_window = tk.Toplevel(parent)
        self.login_window.title("User Login/Register")
        self.login_window.geometry("300x250")

        tk.Label(self.login_window, text="Username:").pack()
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.pack()

        tk.Label(self.login_window, text="Password:").pack()
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack()

        tk.Button(self.login_window, text="Login", command=self.check_credentials).pack()
        tk.Button(self.login_window, text="Register", command=self.register_user).pack()

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if username in users and users[username] == hashed_password:
            messagebox.showinfo("Login Successful", "You are now logged in.")
            self.login_window.destroy()
            self.on_success()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate email format for username
        if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            messagebox.showerror("Registration Failed", "Invalid email format for username.")
            return

        # Validate password requirements
        if not (6 <= len(password) <= 20 and 
                any(char.isupper() for char in password) and 
                any(char.islower() for char in password) and 
                any(char.isdigit() for char in password)):
            messagebox.showerror("Registration Failed", 
                                 "Password must be 6-20 characters long and include uppercase, lowercase letters, and numbers.")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if username in users:
            messagebox.showerror("Registration Failed", "Username already exists.")
            return

        users[username] = hashed_password

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        messagebox.showinfo("Registration Successful", "You are now registered.")
        self.login_window.destroy()
        self.on_success()
