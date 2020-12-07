import tkinter as tk

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
    for i in range(0, 10):
        window.grid_columnconfigure(i, {'minsize': 48})
    window.title("records")

    label = tk.Label(
        text="High score table",
        font=("Helvetica", 18, "bold"),
        background="#4169E1",
        fg="black",
        width=20,
    ).grid(row=0, column=0, columnspan=6, rowspan=2, sticky=tk.W + tk.E)

    # table_records = get table records from DB limit
    table = [("tal", 1000), ("omer", 900), ("yael", 700), ("tal", 1000), ("omer", 900), ("yael", 700), ("tal", 1000),
             ("omer", 900), ("yael", 700), ("yoe", 10000)]

    label = []
    i = 2
    for t in table:
        i += 1
        name = t[0]
        score = t[1]
        if i % 2 == 0:
            bg = "GREY"
        else:
            bg = "WHITE"
        x = tk.Label(
            window,
            text=name,
            font=("bold"),
            fg="black",
            bg=bg,
            width=20,
        )
        x.grid(row=i, column=2, sticky='NW')
        y = tk.Label(
            window,
            text=str(score),
            font=("bold"),
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
