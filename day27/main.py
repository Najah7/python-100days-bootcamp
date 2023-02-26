"""
Project Mile to Km Converter
"""

from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
)

window = Tk()
window.title('Mile to Km Converter')
window['bg'] = 'white'
window.config(padx=20, pady=20)


def miles_to_km(mile):
    km = mile * 1.689
    return km

def click_handler():
    miles = float(miles_input.get())
    label_num['text'] = str(miles_to_km(miles))

miles_input = Entry(bg='white', width=7)
miles_input.grid(column=1, row=0)
label_miles = Label(text='Miles', bg='white')
label_miles.grid(column=2, row=0)
label_is_equal_to = Label(text='is equal to', bg='white')
label_is_equal_to.grid(column=0, row=1)
label_num = Label(text='0', bg='white')
label_num.grid(column=1, row=1)
label_km = Label(text='Km', bg='white')
label_km.grid(column=2, row=1)
calculate_btn = Button(text='Calculate', command=click_handler)
calculate_btn.grid(column=1, row=2)

window.mainloop()