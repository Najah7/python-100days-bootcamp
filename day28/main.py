"""
Project Pomodoro:https://ja.wikipedia.org/wiki/ポモドーロ・テクニック
"""

from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label_timer['text'] = 'Timer'
    lable_check['text'] = ''
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if not reps % 2 == 0:
        count_down(WORK_MIN * 60)
        label_timer.config(text='Work', fg=GREEN)
        
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_timer.config(text='Break', fg=RED)
        reps = 0
    else:
        count_down(SHORT_BREAK_MIN * 60)
        label_timer.config(text='Break', fg=PINK)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    # calculate timer min from all of sec 
    count_min = count // 60
    if count_min < 10: count_min = f"0{count_min}"
    # calculate timer sec form all of sec
    count_sec = count % 60
    if count_sec < 10: count_sec = f"0{count_sec}"
    # set tiemr count
    output_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=output_text)
    # ccount down
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        check = '✓'
        num_checks = reps // 2
        lable_check.config(text=f'{check * num_checks}')
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



# NOTE:イメージのサイズに合わせただけ。
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img) # 半分のxとy
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 30, "bold")) # 絶対座標
canvas.grid(column=1, row=1)

label_timer = Label(text='Timer',font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)
start_btn = Button(text='Start',bg='white', command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text='Reset', bg='white', command=reset_time)
reset_btn.grid(column=2, row=2)
lable_check = Label(font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=GREEN)
lable_check.grid(column=1, row=3)


window.mainloop()



