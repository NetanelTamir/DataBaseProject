import tkinter as tk
from tkinter import messagebox
from page import login_view, view_utils
import Database_Interaction
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
    first_name = entry_first_name.get()
    if len(first_name) < 2 or len(first_name) > 20:
        view_utils.show_error("first name must contain at least 2 characters and at most 20 characters!")
        return
    last_name = entry_last_name.get()
    if len(last_name) < 2 or len(last_name) > 20:
        view_utils.show_error("Last name must contain at least 2 characters and at most 20 characters!")
        return
    user_name = entry_user_name.get()
    if len(user_name) < 2 or len(user_name) > 20:
        view_utils.show_error("User name must contain at least 2 characters and at most 20 characters!")
        return
    password = entry_password.get()
    if len(password) < 2 or len(password) > 20:
        view_utils.show_error("password must contain at least 2 characters and at most 20 characters!")
        return
    print(password + "  " + user_name)
    response = Database_Interaction.add_player((user_name, password, first_name, last_name))
    if response == -1:
        view_utils.show_error("user-name already exist")
    if response == -2:
        view_utils.show_error("sign up failed")
    if response == 0:
        view_utils.show_message("success!", "welcome " + first_name + " " + last_name)
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

    view_utils.init_root(root, "sign-up view")
    view_utils.add_background(root, "Earth-icon.png")
    view_utils.add_title_image(root, "signUp.png",0.38,0)
    view_utils.classic_grid(root)

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