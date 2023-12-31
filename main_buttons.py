# main buttons.py
from admin_login_window import AdminLoginWindow
from UserLoginWindow import UserLoginWindow

import os, subprocess, sys
import tkinter as tk

from csv_reader import CsvReader
from PIL import Image, ImageTk

class MainButtons:
    '''constains add contact and ADMINISTRATOR LOGIN buttons'''
    def __init__(self, canvas,root):
        self.__canvas = canvas
        self.__root = root
        # Add contact button with background
        self.__add_contact_frame = tk.Frame(canvas, bg="white", padx=5, pady=5)
        canvas.create_window(180, 300, window=self.__add_contact_frame, anchor='nw')

        self.__add_contact_label = tk.Label(self.__add_contact_frame, text="ADD CONTACT", font=("Arial", 12, "bold"))
        self.__add_contact_label.pack(fill="both", expand=True)
        self.__add_contact_label.original_bg_color = "light blue"  # Store the original background color
        self.__add_contact_label.bind("<Enter>", self.__on_button_hover)
        self.__add_contact_label.bind("<Leave>", self.__on_button_hover)
        self.__add_contact_label.bind("<Button-1>", self.__open_contact_form)
    
        # ADMINISTRATOR LOGIN button with background
        self.__search_contact_frame = tk.Frame(canvas, bg="white", padx=5, pady=5)
        canvas.create_window(165, 370, window=self.__search_contact_frame, anchor='nw')

        self.__search_contact_label = tk.Label(self.__search_contact_frame, text="ADMINISTRATOR LOGIN", font=("Arial", 12, "bold"))
        self.__search_contact_label.pack(fill="both", expand=True)
        self.__search_contact_label.original_bg_color = "light blue"  # Store the original background color
        self.__search_contact_label.bind("<Enter>", self.__on_button_hover)
        self.__search_contact_label.bind("<Leave>", self.__on_button_hover)
        self.__search_contact_label.bind("<Button-1>", self.__search_contacts)

    def __on_button_hover(self, event):
        if event.type == '7':  # Enter event
            event.widget.config(foreground="black", background="orange")
            event.widget.master.config(background="orange")  # Update the frame's background
        elif event.type == '8':  # Leave event
            event.widget.config(foreground="blue", background=event.widget.original_bg_color)
            event.widget.master.config(background=event.widget.original_bg_color)  # Reset the frame's background
        
    def __open_contact_form(self, event):
        # Modify this method to open the user login/registration window
        # Assuming UserLoginWindow is a class that handles the login and registration process
        login_window = UserLoginWindow(self.__root, self.after_login_open_contact_form)

    def after_login_open_contact_form(self):
        # This method opens the contact form after successful login or registration
        subprocess.Popen(["python", "contents/contact_form.py"])
 
    
    def __search_contacts(self, event):
    # Open the AdminLoginWindow and pass the callback
        login_window = AdminLoginWindow(self.__root, self.open_csv_reader)

    def open_csv_reader(self):
        # Open the CSV Reader Table after successful login
        subprocess.Popen(["python", "csv_reader.py"])


   
