import tkinter as tk
from startup_window import UI
from logger import log_activity


if __name__ == "__main__":
    log_activity("Application Started")
    root = tk.Tk()
    app = UI(root)
    root.mainloop()
    log_activity("Application Closed")


