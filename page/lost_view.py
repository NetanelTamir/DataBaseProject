import tkinter as tk

import database_interaction
from page import signup_view, home_view, view_utils, records_view

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
    view_utils.init_root(root, "you lost")
    view_utils.add_background(root, "Earth-icon.png")
    view_utils.add_title_image(root, "you_lost.png",0.1,0)

    score_bunner = tk.Label(
        text= player[0] +", Your score is: " + score,
        font=("Helvetica", 13),
        background="#4169E1",
        fg="black",
        width=40,
    ).place(x=10, y=60)
    utils.update_score(player,score)
    go_to_menu_button = tk.Button(
        root,
        text="return to menu",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=handle_go_to_main_window
    ).place(relx=0.7, rely=0.24)
    go_to_high_scores_button = tk.Button(
        root,
        text="high scores",
        width=12,
        height=1,
        bg="black",
        fg="white",
        command=handle_go_to_high_scores
    ).place(relx=0.7, rely=0.39)
    root.mainloop()


if '__name__' == '__main__':
    main()
