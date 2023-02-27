from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# def choose(letters, num_letters):
#     """与えられたリストから指定された文字数の文字のリストを返す"""
#     password_letters = [ random.choice(letters) for _ in range(num_letters)]
#     return password_letters



def generate_password():
    """ランダムなパスワードを作成する関数（英字、数字、シンボルから成る）"""
    
    # 文字数と数字とシンボルの使用する個数をランダムに決定
    num_letters = random.randint(8, 10)
    num_numbers = random.randint(2, 4)
    num_symbols = random.randint(2, 4)
    

    
    #　指定文字数分のランダムな文字列をパスワード配列に追加
    password_letters = list()
    password_letters += random.choices(letters, k=num_letters)
    password_letters += random.choices(numbers, k=num_numbers)
    password_letters += random.choices(symbols, k=num_symbols)

    # 追加したものをシャッフル
    random.shuffle(password_letters)

    password = "".join(password_letters)
    
    password_entry.insert(0, password)
    
    pyperclip.copy(password)
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_name = web_site_entry.get()
    email_or_username = email_or_username_entry.get()
    password = password_entry.get()
    
    if len(website_name) == 0 or len(email_or_username) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website_name,
            message=f"There are the details entered: \n"
                    f"Email: {email_or_username}\n"
                    f"Password: {password}\n"
                    f"Is it ok to save? "
            )
    
    if is_ok:
        with open('passwords.txt', 'a') as file:
            file.write(f"{website_name} | {email_or_username} | {password}\n")
    
        web_site_entry.delete(0, END)
        password_entry.delete(0, END)
    
    
# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='white')

# Image
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lockpad_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lockpad_img)
canvas.grid(column=1, row=0)

# Labels
web_site_name_label = Label(text='Website:', bg='white')
web_site_name_label.grid(column=0, row=1)
email_or_username_label = Label(text='Email/Username:', bg='white')
email_or_username_label.grid(column=0, row=2)
password_label = Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)

# Textboxs
# NOTE:columnspan：複数分のカラムを使いたい場合に使う。
web_site_entry = Entry(width=35)
web_site_entry.grid(column=1, row=1, columnspan=2)
web_site_entry.focus()
email_or_username_entry = Entry(width=35)
email_or_username_entry.grid(column=1, row=2, columnspan=2)
email_or_username_entry.insert(0, 'test@example.com')
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

# buttons
password_generator_btn = Button(text='Genarate password', bg='white', command=generate_password, width=13)
password_generator_btn.grid(column=2, row=3)
add_btn = Button(text='add', bg='white', width=35, command=add)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()