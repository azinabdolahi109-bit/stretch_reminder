import tkinter as tk
from tkinter import messagebox
import time

def show_reminder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Stretch Reminder", "Time to stand up and stretch!")
    root.destroy()

if __name__ == "__main__":
    print("Stretch Reminder script started. Press Ctrl+C to stop.")
    try:
        while True:
            # Wait for 30 minutes (1800 seconds)
            time.sleep(1800)
            show_reminder()
    except KeyboardInterrupt:
        print("\nStretch Reminder script stopped.")
