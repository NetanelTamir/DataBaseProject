import tkinter as tk
from page import login_view

# import database_interaction

name = None
last_name = None
user_name = None
password = None
signUpButton = None
goBack = None
label = None


def handle_signup():
    str_name = name.get()
    str_lastname = last_name.get()
    str_username = user_name.get()
    str_password = password.get()
    global label
    label = tk.Label(
        text="You sign up Successfully",
        fg="white",
        bg="black",
        width=50,
        height=10
    )



def handle_goback():
    login_view.main()


def main():
    global name
    global last_name
    global user_name
    global password
    global signUpButton
    global goBack
    global label
    root = tk.Tk()
    root.title("Sign up")
    label = tk.Label(
        text="Welcome to the Game\n Login View",
        fg="white",
        bg="black",
        width=50,
        height=10
    )
    name = tk.Entry(width=20, text="name", master=root)
    last_name = tk.Entry(width=20, text="last name", master=root)
    user_name = tk.Entry(width=20, text="user name", master=root)
    password = tk.Entry(width=20, text="password", master=root)
    signUpButton = tk.Button(
        root,
        text="login!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_signup
    )
    goBack = tk.Button(
        root,
        text="sign up!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_goback
    )
    signUpButton.place(relx=0,
                       rely=1.0,
                       anchor='sw')
    label.pack()
    name.pack()
    last_name.pack()
    user_name.pack()
    password.pack()
    signUpButton.pack()
    root.mainloop()
    goBack.pack()


if '__name__' == '__main__':
    # database_interaction.add_player(("omer", "12345"))
    main()
