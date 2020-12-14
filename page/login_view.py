import tkinter as tk
from time import sleep

import database_interaction
from page import signup_view, home_view
from PIL import Image, ImageTk
import datetime

# import database_interaction

entry_name = None
entry_pass = None
label = None
goBack = None
signUpButton = None
root = None
userName = ""
passw = ""


def handle_click():
    global entry_first_name
    global entry_password
    global root
    ##todo- goto the model and get user name and password
    # entry = username entry2 = password
    if (entry_name and entry_pass):
        print("The button was clicked: " + "----" + entry_pass.get())
        username = entry_name.get()
        password = entry_pass.get()
        id = database_interaction.log_in(username, password)
        if (id > -1):
            home_view.PLAYER = database_interaction.get_player_by_id(id)[0]
            root.destroy()
            home_view.main()


# response = database_interaction.log_in(username, password)
# if response == -1:
#    print("Wrong password or username")
# else:
#    print("hello" + str(response))

# database_intercation


def handle_sign_up():
    global root
    global entry_pass
    global entry_name
    root.destroy()
    signup_view.main()
    # response = database_interaction.add_player((username, password))


# print(response)
def after_signup_main(user, password):
    global entry_pass
    global entry_name
    global userName
    global passw
    userName = user
    passw = password
    main()


def main():
    global root
    global label
    global entry_pass
    global entry_name
    global signUpButton
    global goBack
    global passw
    global userName
    root = tk.Tk()
    root.geometry('640x480')
    root.configure(background='#4169E1')
    load = Image.open("Earth-icon.png")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render, bg="#4169E1")
    img.image = render
    img.place(x=0, y=0, relwidth=1, relheight=1)
    for i in range(1, 10):
        root.grid_rowconfigure(i, {'minsize': 64})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 48})

    load2 = Image.open("images/logos/welcome.png")
    render2 = ImageTk.PhotoImage(load2)
    img = tk.Label(root, image=render2, bg="#4169E1")
    img.image = render2
    img.grid(row=0, column=0, columnspan=10, rowspan=2, sticky=tk.W + tk.E)

    root.title("login")
    # label = tk.Label(
    #     text="Welcome to Carmen Diago Game",
    #     font=("Helvetica", 27),
    #     background="#4169E1",
    #     fg="black",
    #     width=20,
    # ).grid(row=0, column=0, columnspan=10, rowspan=2, sticky=tk.W + tk.E)

    user_label = tk.Label(
        text="enter your user name",
        fg="white",
        bg="black",
        width=20,
    ).grid(row=3, column=3, sticky='NW')
    entry_name = tk.Entry(width=20, text="user name", master=root)
    entry_name.grid(row=3, column=5, sticky='NW')
    entry_name.insert(0, userName)
    pass_label = tk.Label(
        text="enter your password",
        fg="white",
        bg="black",
        width=20,
    ).grid(row=4, column=3, sticky='NW')
    entry_pass = tk.Entry(width=20, text="password", master=root)
    entry_pass.grid(row=4, column=5, sticky='NW')
    entry_pass.insert(0, passw)
    loginButton = tk.Button(
        root,
        text="login!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_click
    ).grid(row=5, column=3)
    signUpButton = tk.Button(
        root,
        text="sign up!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_sign_up
    ).grid(row=5, column=5)
    root.mainloop()


if '__name__' == '__main__':
    # database_interaction.add_player(("omer", "12345"))
    main()
