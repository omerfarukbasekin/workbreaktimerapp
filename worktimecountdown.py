import subprocess
import tkinter as tk
import winsound
from datetime import datetime, timedelta
import sys
from tkinter import messagebox
from PIL import Image, ImageTk

worktime_countdown_seconds = int(sys.argv[1])
breaktime_countdown_seconds = int(sys.argv[2])
end_time = datetime.now() + timedelta(seconds=worktime_countdown_seconds)
work_time_rest = 0
is_paused = False
imagepath = "utilities/"
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def countdown(end_time):
    global is_paused, work_time_rest

    remaining_time = end_time - datetime.now()
    if remaining_time.total_seconds() >= 0 and not is_paused:
        label.config(text=format_time(int(remaining_time.total_seconds())))
        window.attributes("-topmost", True)  # Diğer pencerelerin önünde olmasını sağlar
        window.after(1000, countdown, end_time)
    elif not is_paused:
        winsound.PlaySound("utilities/notification_sound.wav", winsound.SND_FILENAME)
        messagebox.showinfo("Popup", "Work Time Done. Ready For Resting?")
        window.destroy()
        subprocess.Popen(["python", "resttimecountdown.py", str(breaktime_countdown_seconds)])
    else:
        work_time_rest = remaining_time.total_seconds()

def pause_countdown():
    global is_paused
    is_paused = True

def play_countdown():
    global is_paused, end_time

    if is_paused:
        end_time = datetime.now() + timedelta(seconds=work_time_rest)
        is_paused = False
        countdown(end_time)

def reset_countdown():
    subprocess.Popen(["python", "worktimecountdown.py", str(worktime_countdown_seconds), str(breaktime_countdown_seconds)])
    window.destroy()

def getimage(getimagepath):
    getimagepath = imagepath+getimagepath
    imagepng = Image.open(getimagepath)
    imagepng = imagepng.resize((25, 25))  # Adjust the size of the image
    imagepng = ImageTk.PhotoImage(imagepng)
    return imagepng

window = tk.Tk()
window.title("Countdown Timer")
window.geometry("200x100")  # Pencere boyutunu 300x300 olarak ayarlar
window.configure(bg="gray")  # Arkaplan rengini gri yapar

# Ekran boyutunu al
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

taskbar_height = 75

# Pencereyi sağ alt köşeye konumlandır
window.geometry(f"200x100+{screen_width-215}+{screen_height-100-taskbar_height}")

work_time_label = tk.Label(window, text="Work Time", font=("Arial", 16), bg="gray")
work_time_label.pack()

label = tk.Label(window, font=("Arial", 24), bg="gray")  # Etiketin arkaplan rengini gri yapar
label.pack()

button_frame = tk.Frame(window, bg="gray")
button_frame.pack()

# Load the image
imagestart = Image.open(imagepath+"start.png")
imagestart = imagestart.resize((25, 25))  # Adjust the size of the image
photostart = ImageTk.PhotoImage(imagestart)

imagereplay = Image.open(imagepath+"replay.png")
imagereplay = imagereplay.resize((25, 25))  # Adjust the size of the image
photoreplay = ImageTk.PhotoImage(imagereplay)

imagepause = Image.open(imagepath+"pause.png")
imagepause = imagepause.resize((25, 25))  # Adjust the size of the image
photopause = ImageTk.PhotoImage(imagepause)

pause_button = tk.Button(button_frame, image=photopause, command=pause_countdown)
pause_button.pack(side="left", padx=5)

play_button = tk.Button(button_frame, image=photostart, command=play_countdown)
play_button.pack(side="left", padx=5)

reset_button = tk.Button(button_frame, image=photoreplay, command=reset_countdown)
reset_button.pack(side="left", padx=5)

countdown(end_time)

window.mainloop()
