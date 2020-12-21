import tkinter as tk
import datetime
from page import records_view, friends_view, view_utils, login_view, favorite_locations_view
from core.Game import Game

PLAYER = None
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
    if (entry_name and entry_pass):
        print("The button was clicked: " + "----" + entry_pass.get())
        username = entry_name.get()
        password = entry_pass.get()

    game = Game()
    game.run()



def handle_add_friend_click():
    global root
    root.destroy()
    friends_view.main()

def handle_records_click():
    global root
    root.destroy()
    records_view.main()


def handle_Exit_click():
    global root
    root.destroy()
    login_view.main()


def favorite_locations_click():
    global root
    root.destroy()
    favorite_locations_view.main()

def main():
    global PLAYER
    global root
    global label
    global entry_pass
    global entry_name
    global signUpButton
    global goBack
    global passw
    global userName
    id = PLAYER[0]
    firstName = PLAYER[4]
    lastName = PLAYER[5]
    lastPlay = PLAYER[6]
    userName = PLAYER[1]
    delta = datetime.datetime.today().date() - lastPlay
    root = tk.Tk()

    view_utils.init_root(root, "home view")
    view_utils.add_background(root, "Earth-icon.png")


    root.grid_rowconfigure(1, {'minsize': 110})
    for i in range(2, 10):
        root.grid_rowconfigure(i, {'minsize': 64})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 45})
    label = tk.Label(
        text="Welcome " + firstName + ",\n your last game was " + str(delta.days) + " days ago",
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=20,
    ).grid(row=0, column=3, columnspan=10, rowspan=2, sticky=tk.W + tk.E)

    playButton = tk.Button(
        root,
        text="Play!",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda:handle_play_click()
    ).grid(row=2, column=6)
    recordsButton = tk.Button(
        root,
        text="Show Records",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda:handle_records_click()
    ).grid(row=3, column=6)
    favoritesButton = tk.Button(
        root,
        text="Favorite Locations",
        width=14,
        height=1,
        bg="black",
        fg="white",
        command=lambda:favorite_locations_click()
    ).grid(row=4, column=6)
    addFriend_button = tk.Button(
        root,
        text="Friends",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda:handle_add_friend_click()
    ).grid(row=5, column=6)
    exitButton = tk.Button(
        root,
        text="log out",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda:handle_Exit_click()
    ).grid(row=7, column=6)
    root.mainloop()