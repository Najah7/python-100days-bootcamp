"""
Project Flash card
"""
# HACK:日本語の文字化けの対策

import pandas
import random
from tkinter import *

# for dev
from pprint import pprint

BACKGROUND_COLOR = "#B1DDC6"

current_card = dict()

try:
    df_words = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df_words = pandas.read_csv('data/common_english_words.csv')
    
dict_words = df_words.to_dict(orient="records")



# ---------------------------- Functions ------------------------------- #  
def next_card():
    global current_card, flip_timer
    
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_words)
    english_word = current_card['English']
    
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text='English', fill='black')
    canvas.itemconfig(word, text=english_word, fill='black')
    
    window.after(3000, func=flip_card)
    
def flip_card():
    japanese_word = current_card['Japanese']
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text='Japanese', fill='white')
    canvas.itemconfig(word,text=japanese_word, fill='white')

def is_known():
    dict_words.remove(current_card)
    new_dict_words = pandas.DataFrame(dict_words)
    new_dict_words.to_csv('data/words_to_learn.csv', index=False)
    next_card()

    

# ---------------------------- UI ------------------------------- #  
"""
window
"""
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

"""
Falsh card
"""
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150,text='Title', font=('Ariel', 48, 'italic'))
word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

"""
buttons 
"""
# cross button
cross_image = PhotoImage(file='images/wrong.png')
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

# check button
check_image = PhotoImage(file='images/right.png')
know_btn = Button(image=check_image, highlightthickness=0, command=is_known)
know_btn.grid(row=1, column=1)

next_card()

window.mainloop()



