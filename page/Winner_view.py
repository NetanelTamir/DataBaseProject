import tkinter as tk

import Database_Interaction
from page import signup_view, home_view, view_utils, records_view
from core.utils import *

entry_name = None
entry_pass = None
label = None
goBack = None
signUpButton = None
root = None
userName = ""
passw = ""


def handle_go_to_main_window():
    global entry_first_name
    global entry_password
    global root
    root.destroy()
    home_view.main()


def handle_go_to_high_scores():
    global root
    global entry_pass
    global entry_name
    root.destroy()
    records_view.main()


def main(player, score):
    global root
    global label
    global entry_pass
    global entry_name
    global signUpButton
    global goBack
    global passw
    global userName
    root = tk.Tk()
    view_utils.init_root(root, "you won")
    view_utils.add_background(root, "carmen_winner.jpg")
    view_utils.add_title_image(root, "winner.png", 0.3, 0)

    score_bunner = tk.Label(
        text=str(player[4]).upper() + " Your score is: " + str(score),
        font=("Helvetica 13 bold"),
        background="#4169E1",
        fg="black",
        width=40,
    ).place(x=125, y=80)
    update_score(player, score)
    go_to_menu_button = tk.Button(
        root,
        text="return to menu",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=handle_go_to_main_window
    ).place(relx=0.33, rely=0.8)
    go_to_high_scores_button = tk.Button(
        root,
        text="high scores",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=handle_go_to_high_scores
    ).place(relx=0.53, rely=0.8)
    root.mainloop()


if '__name__' == '__main__':
    main()
