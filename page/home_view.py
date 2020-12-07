import tkinter as tk
import datetime
from time import sleep

from page import signup_view
from PIL import Image, ImageTk

# import database_interaction

entry_name = None
entry_pass = None
label = None
goBack = None
signUpButton = None
root = None
userName = ""
passw = ""


def handle_play_click():
    global entry_first_name
    global entry_password
    ##todo- goto the model and get user name and password
    # entry = username entry2 = password
    if (entry_name and entry_pass):
        print("The button was clicked: " + "----" + entry_pass.get())
        username = entry_name.get()
        password = entry_pass.get()


# response = database_interaction.log_in(username, password)
# if response == -1:
#    print("Wrong password or username")
# else:
#    print("hello" + str(response))

# database_intercation


def handle_records_click():
    global root
    global entry_pass
    global entry_name
    root.destroy()

    # response = database_interaction.add_player((username, password))


def handle_Exit_click():
    global root
    #root.destroy()
    #exit(0)


def favorite_locations_click():
    print("b")


def main(player):
    global root
    global label
    global entry_pass
    global entry_name
    global signUpButton
    global goBack
    global passw
    global userName
    firstName = player[3]
    lastName = player[4]
    lastPlay = player[5]
    userName = player[0]
    delta = datetime.datetime.today() - lastPlay
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
    root.title("login")
    label = tk.Label(
        text="Welcome " + firstName + ",\n your last game was " + str(delta.days) + " days ago",
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=20,
    ).grid(row=0, column=3, columnspan=10, rowspan=2, sticky=tk.W + tk.E)

    playButton = tk.Button(
        root,
        text="play!",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=handle_play_click
    ).grid(row=3, column=6)
    recordsButton = tk.Button(
        root,
        text="show records",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=handle_records_click
    ).grid(row=4, column=6)
    favoritesButton = tk.Button(
        root,
        text="favorite locations",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=favorite_locations_click
    ).grid(row=5, column=6)
    exitButton = tk.Button(
        root,
        text="Exit",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=handle_Exit_click()
    ).grid(row=6, column=6)
    root.mainloop()
