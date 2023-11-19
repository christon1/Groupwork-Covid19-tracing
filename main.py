import tkinter as tk
from startup_window import UI
import hashlib
from tkinter import messagebox

if __name__ == "__main__":
    with open('contact-tracing-data.csv','rb') as f:
        content=f.read()
        md5=hashlib.md5()
        md5.update(content)
        checksum1 = md5.hexdigest()

    try:
        with open('md5','r') as mdf:
            checksum2=mdf.read()

        if checksum1!=checksum2:
            tk.messagebox.showinfo("Warining! File destroyed!")
    except:
        pass

    root = tk.Tk()
    app = UI(root)
    root.mainloop()