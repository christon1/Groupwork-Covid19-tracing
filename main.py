import tkinter as tk
from tkinter import messagebox
import re  # Import for regular expression
from startup_window import UI  # Import the UI class from startup_window.py
from user_management import register_user, login_user

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def show_register_form():
    def on_register():
        username = entry_username.get()
        password = entry_password.get()
        if not is_valid_email(username):
            messagebox.showerror("Error", "Invalid email format")
            return

        if register_user(username, password):
            messagebox.showinfo("Success", "Registration successful")
            register_window.destroy()
            show_login_form()
        else:
            messagebox.showerror("Error", "Username already exists")

    register_window = tk.Toplevel(root)
    register_window.title("Register")

    tk.Label(register_window, text="Username:").pack()
    entry_username = tk.Entry(register_window)
    entry_username.pack()

    tk.Label(register_window, text="Password:").pack()
    entry_password = tk.Entry(register_window, show="*")
    entry_password.pack()

    tk.Button(register_window, text="Register", command=on_register).pack()

def show_login_form():
    def on_login():
        username = entry_username.get()
        password = entry_password.get()
        if login_user(username, password):
            messagebox.showinfo("Success", "Login successful")
            login_window.destroy()
            root.deiconify()  # Reveal the main window
            app = UI(root)  # Initialize and show the main app UI
        else:
            messagebox.showerror("Error", "Login failed")

    login_window = tk.Toplevel(root)
    login_window.title("Login")

    tk.Label(login_window, text="Username:").pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    tk.Label(login_window, text="Password:").pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    tk.Button(login_window, text="Login", command=on_login).pack()
    tk.Button(login_window, text="Register", command=lambda: [login_window.destroy(), show_register_form()]).pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window initially
    root.title("COVID Contact Tracing App")

    show_login_form()  # Initially, show the login form

    root.mainloop()
