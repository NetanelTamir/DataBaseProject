import tkinter as tk

from database_interaction import get_highscores_yes_repeats
from page import home_view, view_utils
window = None

def handle_Back_click():
    global window
    global player_g
    window.destroy()
    home_view.main()


def main():
    id = home_view.PLAYER[0]
    global window
    global player_g
    window = tk.Tk()
    view_utils.init_root(window, "records view")
    view_utils.add_background(window, "Earth-icon.png")
    view_utils.add_title_image(window, "highscores.png",relx=0.26,rely=0)
    label = tk.Label(
        text="High-scores of all users. With repeats",
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=50,
    ).place(relx=0, rely=0.12)
    window.grid_rowconfigure(1, {'minsize': 100})
    for i in range(2, 10):
        window.grid_rowconfigure(i, {'minsize': 0})
    for i in range(2, 6):
        window.grid_columnconfigure(i, {'minsize': 48})

    table = get_highscores_yes_repeats()

    label = []
    i = 2
    for t in table:
        i += 1
        name = t[0] + " " + t[1]
        score = t[2]
        if i % 2 == 0:
            bg = "#C0C0C0"
        else:
            bg = "#F8F8FF"
        z = tk.Label(
            window,
            text=str(i - 2) + ".",
            font="bold",
            fg="black",
            bg=bg,
            width=20,
        )
        z.grid(row=i, column=0, sticky='NW')
        x = tk.Label(
            window,
            text=name,
            font="bold",
            fg="black",
            bg=bg,
            width=20,
        )
        x.grid(row=i, column=2, sticky='NW')
        y = tk.Label(
            window,
            text=str(score),
            font="bold",
            fg="black",
            bg=bg,
            width=20,
        )
        y.grid(row=i, column=3, sticky='NW')
        label.append(x)
        label.append(y)
    backButton = tk.Button(
        window,
        text="Go Back",
        width=24,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_Back_click()
    ).place(x=225, y=420)
    window.mainloop()
