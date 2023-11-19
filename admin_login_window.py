import tkinter as tk
from tkinter import messagebox
import hashlib
import time

class AdminLoginWindow:
    def __init__(self, parent, on_success):
        self.parent = parent
        self.on_success = on_success
        self.attempt_count = 0
        self.last_attempt_time = time.time()

        self.login_window = tk.Toplevel(parent)
        self.login_window.title("Administrator Login")
        self.login_window.geometry("300x200")

        tk.Label(self.login_window, text="Username:").pack()
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.pack()

        tk.Label(self.login_window, text="Password:").pack()
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack()

        tk.Button(self.login_window, text="Login", command=self.check_credentials).pack()

    def check_credentials(self):
        current_time = time.time()
        if current_time - self.last_attempt_time < 5:  # 5 seconds cooldown between attempts
            messagebox.showwarning("Login Failed", "Too many attempts. Please wait.")
            return
        self.last_attempt_time = current_time

        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hash the input password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

       


        # Replace this with a secure method to retrieve stored credentials
        stored_username, stored_hashed_password = self.retrieve_stored_credentials()


       

        if username == stored_username and hashed_password == stored_hashed_password:
            messagebox.showinfo("Login Successful", "You are now logged in.")
            self.login_window.destroy()
            self.on_success()
        else:
            self.attempt_count += 1
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def retrieve_stored_credentials(self):
        # In a real application, securely retrieve these from a database
        # For demonstration, we'll simulate this with a file
        with open("credentials.txt", "r") as file:
            stored_username = file.readline().strip()
            stored_hashed_password = file.readline().strip()
        return stored_username, stored_hashed_password

# In a real application, you would securely create this file with hashed passwords
# For example, the password "password" hashed with SHA-256
# with open("credentials.txt", "w") as file:
#     file.write("admin\n")
#     file.write(hashlib.sha256("password".encode()).hexdigest())

