import tkinter as tk
import datetime
from page import records_view, friends_view, view_utils, login_view, favorite_locations_view, all_records_view, \
    game_view
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

    root.destroy()
    game_view.main()


def handle_add_friend_click():
    global root
    root.destroy()
    friends_view.main()


def handle_records_click():
    global root
    root.destroy()
    records_view.main()


def handle_all_records_click():
    global root
    root.destroy()
    all_records_view.main()


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

    # root.grid_rowconfigure(1, {'minsize': 110})
    # for i in range(2, 10):
    #     root.grid_rowconfigure(i, {'minsize': 64})
    # for i in range(0, 10):
    #     root.grid_columnconfigure(i, {'minsize': 45})
    label = tk.Label(
        text="Welcome " + firstName + "!\n Your last game was " + str(delta.days) + " days ago.",
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=25,
    ).place(relx=0.28, rely=0)
    view_utils.add_image(root, 'carmen_home.png', relx=0.70, rely=0.10)
    view_utils.add_image(root, 'carmen_home_miror.png', relx=0.013, rely=0.10)
    playButton = tk.Button(
        root,
        text="Play!",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_play_click()
    ).place(relx=0.42, rely=0.2)
    recordsButton = tk.Button(
        root,
        text="Friends Records",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_records_click()
    ).place(relx=0.32, rely=0.3)
    allrecordsButton = tk.Button(
        root,
        text="All Records",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_all_records_click()
    ).place(relx=0.52, rely=0.3)
    favoritesButton = tk.Button(
        root,
        text="Favorite Locations",
        width=14,
        height=1,
        bg="black",
        fg="white",
        command=lambda: favorite_locations_click()
    ).place(relx=0.41, rely=0.4)
    addFriend_button = tk.Button(
        root,
        text="Friends",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_add_friend_click()
    ).place(relx=0.42, rely=0.50)
    exitButton = tk.Button(
        root,
        text="Log Out",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_Exit_click()
    ).place(relx=0.422, rely=0.8)
    root.mainloop()
