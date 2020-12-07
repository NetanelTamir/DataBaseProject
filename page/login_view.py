import tkinter as tk
from  page import signup_view
#import database_interaction

entry = None
entry2 = None
label = None
loginButton = None
signUpButton = None
root = None
def handle_click():
    ##todo- goto the model and get user name and password
    # entry = username entry2 = password
    print("The button was clicked: " + str(loginButton.winfo_pointerx()) + str(
        loginButton.winfo_pointery()) + "----" + entry2.get())
    username = entry.get()
    password = entry2.get()
   # response = database_interaction.log_in(username, password)
    #if response == -1:
    #    print("Wrong password or username")
    #else:
    #    print("hello" + str(response))

    # database_intercation


def handle_sign_up():
    global root
    root.destroy()
    signup_view.main()
    username = entry.get()
    password = entry2.get()
    #response = database_interaction.add_player((username, password))
   # print(response)

def main():
    global root
    global label
    global  entry2
    global entry
    global signUpButton
    global loginButton
    root = tk.Tk()
    root.geometry('640x480')
    root.configure(background = '#4169E1')
    for i in range(1, 10):
        root.grid_rowconfigure(i, {'minsize': 64})
    for i in range (0,10):
        root.grid_columnconfigure(i, {'minsize': 48})
    root.title("login")
    label = tk.Label(
        text="Welcome to Carmen Diago Game",
        background = "#4169E1",
        fg="black",
        width=20,
    ).grid(row =0, column = 1, columnspan = 10, rowspan= 2, sticky = tk.W+tk.E)

    user_label = tk.Label(
        text="enter your user name",
        fg="white",
        bg="black",
        width=20,
    ).grid(row =3, column = 3, sticky = 'NW')
    entry = tk.Entry(width=20, text="user name", master=root).grid(row =3, column =5 , sticky = 'NW')
    pass_label = tk.Label(
        text="enter your password",
        fg="white",
        bg="black",
        width=20,
    ).grid(row=4, column=3, sticky = 'NW')
    entry2 = tk.Entry(width=20, text="password", master=root).grid(row =4, column = 5, sticky = 'NW')
    loginButton = tk.Button(
        root,
        text="login!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_click
    ).grid(row =5, column = 3)
    signUpButton = tk.Button(
        root,
        text="sign up!",
        width=8,
        height=1,
        bg="black",
        fg="white",
        command=handle_sign_up
    ).grid(row =5, column = 5)
   # label.pack()
   # entry.pack()
   # entry2.pack()
   # loginButton.pack()
   # signUpButton.pack()
    root.mainloop()

if '__name__' == '__main__':
   # database_interaction.add_player(("omer", "12345"))
    main()




