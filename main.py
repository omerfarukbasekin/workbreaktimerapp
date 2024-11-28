import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from tkinter import messagebox
import winsound
from datetime import datetime, timedelta
import sys

def start_countdown():
    worktime_hours = worktime_hours_entry.get()
    worktime_minutes = worktime_minutes_entry.get()
    worktime_seconds = worktime_seconds_entry.get()
    breaktime_hours = breaktime_hours_entry.get()
    breaktime_minutes = breaktime_minutes_entry.get()
    breaktime_seconds = breaktime_seconds_entry.get()

    if (worktime_hours.isdigit() and worktime_minutes.isdigit() and worktime_seconds.isdigit()
        and breaktime_hours.isdigit() and breaktime_minutes.isdigit() and breaktime_seconds.isdigit()):
        worktime_countdown_seconds = calculate_seconds(worktime_hours, worktime_minutes, worktime_seconds)
        breaktime_countdown_seconds = calculate_seconds(breaktime_hours, breaktime_minutes, breaktime_seconds)
        subprocess.Popen(["python", "worktimecountdown.py", str(worktime_countdown_seconds), str(breaktime_countdown_seconds)])
        root.destroy()

def calculate_seconds(hours, minutes, seconds):
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

root = tk.Tk()
root.title("Countdown Setup")
root.geometry("300x230")

# Ekran boyutunu al
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

taskbar_height = 75

# Pencereyi sağ alt köşeye konumlandır
root.geometry(f"300x150+{screen_width-315}+{screen_height-150-taskbar_height}")

worktime_label = tk.Label(root, text="Enter Work Time:")
worktime_label.pack()

worktime_frame = tk.Frame(root)
worktime_frame.pack()

worktime_hours_label = tk.Label(worktime_frame, text="Hours:")
worktime_hours_label.pack(side="left")

worktime_hours_entry = tk.Entry(worktime_frame, width=5)
worktime_hours_entry.insert(0, "1")
worktime_hours_entry.pack(side="left")

worktime_minutes_label = tk.Label(worktime_frame, text="Minutes:")
worktime_minutes_label.pack(side="left")

worktime_minutes_entry = tk.Entry(worktime_frame, width=5)
worktime_minutes_entry.insert(0, "0")
worktime_minutes_entry.pack(side="left")

worktime_seconds_label = tk.Label(worktime_frame, text="Seconds:")
worktime_seconds_label.pack(side="left")

worktime_seconds_entry = tk.Entry(worktime_frame, width=5)
worktime_seconds_entry.insert(0, "6")
worktime_seconds_entry.pack(side="left")

breaktime_label = tk.Label(root, text="Enter Break Time:")
breaktime_label.pack()

breaktime_frame = tk.Frame(root)
breaktime_frame.pack()

breaktime_hours_label = tk.Label(breaktime_frame, text="Hours:")
breaktime_hours_label.pack(side="left")

breaktime_hours_entry = tk.Entry(breaktime_frame, width=5)
breaktime_hours_entry.insert(0, "0")
breaktime_hours_entry.pack(side="left")

breaktime_minutes_label = tk.Label(breaktime_frame, text="Minutes:")
breaktime_minutes_label.pack(side="left")

breaktime_minutes_entry = tk.Entry(breaktime_frame, width=5)
breaktime_minutes_entry.insert(0, "15")
breaktime_minutes_entry.pack(side="left")

breaktime_seconds_label = tk.Label(breaktime_frame, text="Seconds:")
breaktime_seconds_label.pack(side="left")

breaktime_seconds_entry = tk.Entry(breaktime_frame, width=5)
breaktime_seconds_entry.insert(0, "0")
breaktime_seconds_entry.pack(side="left")

# Load the image
image = Image.open("utilities/start.png")
image = image.resize((50, 50))  # Adjust the size of the image
photo = ImageTk.PhotoImage(image)

start_button = tk.Button(root, image=photo, command=start_countdown)
start_button.pack()

root.mainloop()
