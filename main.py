import tkinter as tk
from startup_window import UI
from contents.logger import log_activity
import hashlib
from tkinter import messagebox
from contents.encoder import Encoder

if __name__ == "__main__":
    log_activity("Application Started")
    encoder=Encoder()
    encoder.decode('contact-tracing-data.csv')
    with open('contact-tracing-data.csv','rb') as f:
        content=f.read()
        md5=hashlib.md5()
        md5.update(content)
        checksum1 = md5.hexdigest()

    encoder.encode('contact-tracing-data.csv')

    try:
        with open('md5','r') as mdf:
            checksum2=mdf.read()

        if str(checksum1)!=str(checksum2):
            print(f'checksum1={checksum1}, checksum2={checksum2}')
            tk.messagebox.showwarning(title=None, message="Warining! File destroyed!")
    except:
        pass

    root = tk.Tk()
    app = UI(root)
    root.mainloop()
    log_activity("Application Closed")


