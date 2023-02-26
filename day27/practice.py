"""
This lesson is for Tkinter and Function args
"""

# NOTE:MS-DOSのCLIからMac Lisa(→Windows 95)のGUIに

"""
famous thigs from XEROX PARC(Palo Alto Research Center) ←研究所
・LAN
・OOP
・GUI
"""

"""
Tkinter
"""

from tkinter import (
    Tk,
    Label,
    Button,
    Entry,
    Text,
    Spinbox,
    Scale,
    Checkbutton,
    Radiobutton,
    Listbox,
    IntVar,
    END, #最後の文字の次の位置を表す。Entryウィジェットで使える
)

# Tk Doc:https://tcl.tk/man/tcl8.6/contents.htm

window = Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)
window['bg'] = 'white'
window.config(padx=20, pady=20) # set padding

"""
Basic Wigets
"""

# Label
my_label = Label(text='I ma a Label', font=("Arial", 24, "bold"), bg='white')
my_label.pack() #配置

# 2 way to change somthing of component
my_label['text'] = 'New Text'
my_label.config(text='New Text')

def button_clicked():
    new_text = input.get()
    my_label['text'] = new_text

# Button
# NOTE:commandで関数をバンドルできる。
button = Button(text='Click me',bg='white', command=button_clicked)
button.pack()

# Entry（like input）
input = Entry()
input.pack()
input.get() # get input value

# Text(like text area)
text = Text(height=5, width=30) #文字数
text.focus()
text.insert(END, "Example of multi-line text entry")
text.pack()

# Spinbox (like select box)
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=100, to=0, command=scale_used)
scale.pack()

# Checkbox
checkbtn_used = lambda : print(checked_state.get())
checked_state = IntVar()
checkbtn = Checkbutton(text="Is On?", variable=checked_state, command=checkbtn_used)
checkbtn.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4) #項目数
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

"""
Tkinter Layout

Tkinter Layout Mangers
・Pack：ロジックの流れに沿って配置される
・Place：xとyの座標を用いて配置する（絶対座標）
・Grid：Gridで考えて、columnとrowで指定する。
※packとgridは同じプログラムで使うことはできない。

NOTE:基本的にwiget数が少ない場合以外はgridで指定していくのが基本。
"""

window.mainloop()

"""
Advanced Python Arguments
・Keyword Arguments: arg=default_value
・Unlimited Arguments: def fun(*arg)
・Many Keyworded Arguments: def fun(**kwargs)
"""

# NOTE:*argはタプル
def add(*arg):
    print(arg)
    return sum(arg)

print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    # getなどを使うことでエラーを回避できる。
    n += kwargs.get('add')
    n *= kwargs.get('multiply')
    print(n)
            
    

print(calculate(2, add=3, multiply=5))
