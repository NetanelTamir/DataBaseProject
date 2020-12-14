import tkinter as tk
import datetime
from time import sleep
# from core.event_handlers import handle_Exit_click,handle_play_click, handle_records_click, handle_add_friend_click

from page import records_view, friends_view
from PIL import Image, ImageTk
from core.Game import Game

# import database_interaction
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
    ##todo- goto the model and get user name and password
    # entry = username entry2 = password
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

    # response = database_interaction.add_player((username, password))


def handle_Exit_click():
    global root
    # root.destroy()
    # exit(0)


def favorite_locations_click():
    print("b")

# response = database_interaction.log_in(username, password)
# if response == -1:
#    print("Wrong password or username")
# else:
#    print("hello" + str(response))

# database_intercation



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
    root.geometry('640x480')
    root.configure(background='#4169E1')
    load = Image.open("Earth-icon.png")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render, bg="#4169E1")
    img.image = render
    img.place(x=0, y=0, relwidth=1, relheight=1)

    root.grid_rowconfigure(1, {'minsize': 110})
    for i in range(2, 10):
        root.grid_rowconfigure(i, {'minsize': 64})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 45})
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