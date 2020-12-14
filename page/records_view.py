import tkinter as tk

from database_interaction import get_highscores_no_repeats_friends
from page import home_view
from PIL import Image, ImageTk

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
    window.geometry('640x480')
    window.configure(background='#4169E1')
    load = Image.open("Earth-icon.png")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(window, image=render, bg="#4169E1")
    img.image = render
    img.place(x=0, y=0, relwidth=1, relheight=1)
    window.grid_rowconfigure(1, {'minsize': 100})
    for i in range(2, 10):
        window.grid_rowconfigure(i, {'minsize': 0})
    for i in range(2, 5):
        window.grid_columnconfigure(i, {'minsize': 48})

    window.title("records")

    load2 = Image.open("images/logos/highscores.png")
    render2 = ImageTk.PhotoImage(load2)
    img = tk.Label(window, image=render2, bg="#4169E1")
    img.image = render2
    img.grid(row=0, column=0, columnspan=6, rowspan=2, sticky=tk.W + tk.E)
    # label = tk.Label(
    #     text="High score table",
    #     font=("Helvetica", 18, "bold"),
    #     background="#4169E1",
    #     fg="black",
    #     width=20,
    # ).grid(row=0, column=0, columnspan=6, rowspan=2, sticky=tk.W + tk.E)

    # table_records = get table records from DB limit
    # table = [("tal", 1000), ("omer", 900), ("yael", 700), ("tal", 1000), ("omer", 900), ("yael", 700), ("tal", 1000),
    #          ("omer", 900), ("yael", 700), ("yoe", 10000)]
    table = get_highscores_no_repeats_friends(home_view.PLAYER[0])

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
        z.grid(row=i, column=2, sticky='NW')
        x = tk.Label(
            window,
            text=name,
            font="bold",
            fg="black",
            bg=bg,
            width=20,
        )
        x.grid(row=i, column=3, sticky='NW')
        y = tk.Label(
            window,
            text=str(score),
            font="bold",
            fg="black",
            bg=bg,
            width=20,
        )
        y.grid(row=i, column=4, sticky='NW')
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
