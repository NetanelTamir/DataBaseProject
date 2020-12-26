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
    view_utils.add_title_image(root, "welcome.png",0.1,0)
    #view_utils.classic_grid(root)

    # user_label = tk.Label(
    #     text="enter your user name",
    #     fg="white",
    #     bg="black",
    #     width=20,
    # ).grid(row=3, column=3, sticky='NW')

    view_utils.add_image(root,'username.png',0.07,0.2)
    entry_name = tk.Entry(width=20, text="user name", master=root)
    entry_name.place(relx=0.4, rely=0.241)
    entry_name.insert(0, userName)
    # pass_label = tk.Label(
    #     text="enter your password",
    #     fg="white",
    #     bg="black",
    #     width=20,
    # ).grid(row=4, column=3, sticky='NW')
    view_utils.add_image(root,'password.png',0.07,0.35)
    entry_pass = tk.Entry(width=20, text="password",show="*" ,master=root)
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
