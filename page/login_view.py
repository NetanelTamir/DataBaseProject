import tkinter as tk

import database_interaction
from page import signup_view, home_view, view_utils

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
    if (entry_name and entry_pass):
        print("The button was clicked: " + "----" + entry_pass.get())
        username = entry_name.get()
        password = entry_pass.get()
        id = database_interaction.log_in(username, password)
        if (id > -1):
            home_view.PLAYER = database_interaction.get_player_by_id(id)[0]
            root.destroy()
            home_view.main()



def handle_sign_up():
    global root
    global entry_pass
    global entry_name
    root.destroy()
    signup_view.main()

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
    view_utils.init_root(root, "login view")
    view_utils.add_background(root, "Earth-icon.png")
    view_utils.add_title_image(root, "welcome.png")
    view_utils.classic_grid(root)

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
    main()
