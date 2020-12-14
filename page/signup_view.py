import tkinter as tk
from time import sleep
from tkinter import messagebox
from page import login_view
from PIL import Image, ImageTk
import database_interaction
entry_first_name = None
entry_password = None
entry_user_name = None
entry_last_name = None
label = None
goBack = None
signUpButton = None
root = None

def handle_go_backclick():
    global root
    root.destroy()
    login_view.main()

def handle_sign_up():
    global root
    global entry_last_name
    global entry_user_name
    global entry_first_name
    global entry_password
    last_name = entry_last_name.get()
    user_name = entry_user_name.get()
    first_name = entry_first_name.get()
    password = entry_password.get()
    ##insert to DB and connect
    print(password + "  " + user_name)
    response = database_interaction.add_player((user_name,password,first_name,last_name))
    if response == -1:
        messagebox.showerror("Error", "user-name already exist")
    if response == -2:
        messagebox.showerror("Error","sign up failed")
    if response == 0:
        messagebox.showinfo("success!", "welcome " + first_name + " " + last_name)
        root.destroy()
        login_view.after_signup_main(user_name,password)
def main():
    global entry_last_name
    global entry_user_name
    global root
    global label
    global entry_password
    global entry_first_name
    global signUpButton
    global goBack
    root = tk.Tk()
    root.geometry('640x480')
    root.configure(background='#4169E1')
    load = Image.open("Earth-icon.png")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render,bg="#4169E1")
    img.image = render
    img.place(x=0, y=0, relwidth = 1, relheight=1)
    for i in range(1, 10):
        root.grid_rowconfigure(i, {'minsize': 64})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 48})
    root.title("sign-up")
    label = tk.Label(
        text="Sign up :)",
        font=("Helvetica", 27),
        background="#4169E1",
        fg="black",
        width=20,
    ).grid(row=0, column=0, columnspan=10, rowspan=2, sticky=tk.W + tk.E)
    first_name_label = tk.Label(
        text="enter first name",
        fg="white",
        bg="black",
        width=20,
    ).grid(row=3, column=3, sticky='NW')
    entry_first_name = tk.Entry(width=20, text="first name", master=root)
    entry_first_name.grid(row=3, column=5, sticky='NW')
    last_name_label = tk.Label(
        text="enter last name",
        fg="white",
        bg="black",
        width=20,
    ).grid(row=4, column=3, sticky='NW')
    entry_last_name = tk.Entry(width=20, text="last name", master=root)
    entry_last_name.grid(row=4,column=5,sticky='NW')
    user_label = tk.Label(
        text="enter user name",
        fg="white",
        bg="black",
        width=20,
    ).grid(row=5, column=3, sticky='NW')
    entry_user_name = tk.Entry(width=20, text="user name", master=root)
    entry_user_name.grid(row=5, column=5, sticky='NW')
    pass_label = tk.Label(
        text="enter password",
        fg="white",
        bg="black",
        width=20,
    ).grid(row=6, column=3, sticky='NW')
    entry_password = tk.Entry(width=20, text="password", master=root)
    entry_password.grid(row=6, column=5, sticky='NW')
    goBack = tk.Button(
        root,
        text="go back!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_go_backclick
    ).grid(row=7, column=3)
    signUpButton = tk.Button(
        root,
        text="sign up!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_sign_up
    ).grid(row=7, column=5)
    root.mainloop()