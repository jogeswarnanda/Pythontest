
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
GREEN = "#9bdeac"
current_card = {}
flip_timer = None
to_learn = {}

try:    
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():    
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=canvas_img_front)
    flip_timer = window.after(3000, flip_card)

    
def flip_card():
    print("in flip card")
    print(current_card)
    canvas.itemconfig(card_background, image=canvas_img_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    #window.after(3000, flip_card)
    #window.after_cancel(flip_card)
    
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()
    
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img_front = PhotoImage(file="card_front.png")
canvas_img_back = PhotoImage(file="card_back.png")

card_background = canvas.create_image(400, 263, image=canvas_img_front)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text=" ", font=(FONT_NAME, 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text=" ", font=(FONT_NAME, 60, "bold"), fill="black")

cross_img = PhotoImage(file="wrong.png")
check_img = PhotoImage(file="right.png")

unknown_button = Button(image=cross_img, highlightthickness=0,command=next_card)
unknown_button.grid(column=0, row=1)
known_button = Button(image=check_img, highlightthickness=0,command=is_known)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()


