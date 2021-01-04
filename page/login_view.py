import tkinter as tk

import Database_Interaction
from page import signup_view, home_view, view_utils
from core import event_handler

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
    username = entry_name.get()
    password = entry_pass.get()
    response, msg = event_handler.log_in(username, password)
    if response == -1:
        view_utils.show_error(msg)
    else:
        home_view.PLAYER = msg
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
    view_utils.add_image(root, "carmen-glasses.jpg", relx=0.6, rely=0.58)
    view_utils.add_title_image(root, "welcome.png", 0.1, 0)

    view_utils.add_image(root, 'username.png', 0.07, 0.2)
    entry_name = tk.Entry(width=20, text="user name", master=root)
    entry_name.place(relx=0.4, rely=0.241)
    entry_name.insert(0, userName)
    view_utils.add_image(root, 'password.png', 0.07, 0.35)
    entry_pass = tk.Entry(width=20, text="password", show="*", master=root)
    entry_pass.place(relx=0.4, rely=0.395)
    entry_pass.insert(0, passw)
    loginButton = tk.Button(
        root,
        text="login!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_click
    ).place(relx=0.7, rely=0.24)
    signUpButton = tk.Button(
        root,
        text="sign up!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_sign_up
    ).place(relx=0.7, rely=0.39)
    root.mainloop()


if '__name__' == '__main__':
    main()
