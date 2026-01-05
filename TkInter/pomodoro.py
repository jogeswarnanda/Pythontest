from tkinter import *
import math
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK      = "#e2979c"
RED       = "#e7305b"
GREEN     = "#9bdeac"
YELLOW    = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN  = 0.5
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN  = 20
reps = 0
timer = None
#initialize pygame mixer
pygame.mixer.init()

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

#def play_sound():
#    pygame.mixer.music.load("notification_sound.mp3")
#    pygame.mixer.music.play(loops=0)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_title.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_title.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label_title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = int(count / 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            pygame.mixer.music.load("notification_sound.mp3")
            pygame.mixer.music.play(loops=0)
            #play sound
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

#Label
label_title = Label(text="Timer", font=(FONT_NAME, 40))
#my_label.pack()

label_title.config(fg=GREEN, bg=YELLOW) 
label_title.config(padx=10, pady=10)
label_title.grid(column=1, row=0)

#Canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Labels

start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"),highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20, "bold"),highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text=" ", font=(FONT_NAME, 20, "bold"),fg=GREEN, bg=YELLOW,highlightthickness=0)
check_marks.grid(column=1, row=3)

#sound_button = Button(text="Sound", font=(FONT_NAME, 20, "bold"),highlightthickness=0, command=play_sound)
#sound_button.grid(column=2, row=3)


window.mainloop()
