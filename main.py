import tkinter as tk
import pyperclip
from tkinter import END
from tkinter import messagebox

from password_generator import PasswordGenerator

# Create Screen
root = tk.Tk()
root.title("Password Manager")
root.config(pady=50, padx=50)

# Create the canvas for the logo
logo = tk.PhotoImage(file='logo.png')
canvas = tk.Canvas(master=root, height=200, width=190)
canvas.create_image(100, 95, image=logo)
canvas.grid(row=0, column=1)


# Generate Password
def pw_generate():
    my_pw_generator = PasswordGenerator()
    pw = my_pw_generator.generate()
    pyperclip.copy(pw)
    entry_password.delete(0, END)
    entry_password.insert(0, pw)


# Register Password to txt
def pw_registration(**kwargs):
    reg_website = kwargs['website']
    reg_username = kwargs['username']
    reg_password = kwargs['password']
    with open(file='password.txt', mode='a') as file:
        file.write(f'{reg_website} | {reg_username} | {reg_password}\n')


# Perform function by clicking 'Yes' button
def pw_yes_button():
    add_website = entry_website.get()
    add_username = entry_username.get()
    add_password = entry_password.get()
    pw_registration(website=add_website, username=add_username, password=add_password)
    entry_password.delete(0, END)
    entry_website.delete(0, END)


# Create confirmation pop-up window
def pop_up():
    pop_up_website = entry_website.get()
    pop_up_username = entry_username.get()
    pop_up_password = entry_password.get()
    message = f'Email: {pop_up_username}\nPassword: {pop_up_password}\nDo you wish to proceed?'
    if pop_up_password == '' or pop_up_website == '' or pop_up_username == '':
        tk.messagebox.showerror(title='Oops', message="Please don't leave any fields empty.")
    else:
        res = tk.messagebox.askokcancel(title=pop_up_website, message=message)
        if res:
            pw_yes_button()


# Create widgets for buttons, labels and entry
tk.Label(text='Website: ', master=root).grid(row=1, column=0)
tk.Label(text='Email/Username: ', master=root).grid(row=2, column=0)
tk.Label(text='Password: ', master=root).grid(row=3, column=0)

tk.Button(text='Generate Password', master=root, command=pw_generate).grid(row=3, column=2)
tk.Button(text='Add', width=42, master=root, command=pop_up).grid(row=4, column=1, columnspan=2, pady=2)

entry_website = tk.Entry(width=50, master=root)
entry_website.grid(row=1, column=1, columnspan=2, sticky='w', pady=2)
entry_website.focus()
entry_username = tk.Entry(width=50, master=root)
entry_username.grid(row=2, column=1, columnspan=2, sticky='w', pady=2)
entry_password = tk.Entry(width=30, master=root)
entry_password.grid(row=3, column=1, sticky='w', pady=2)

root.mainloop()
