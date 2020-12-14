import tkinter as tk
from time import sleep
import core
import database_interaction
from page import signup_view, home_view
from PIL import Image, ImageTk
from page import home_view

root = None
entry_name = None

def handle_Back_click():
    global root
    root.destroy()
    home_view.main()

def handle_remove_click():
    global entry_name
    global root
    user_delete = entry_name.get()
    database_interaction.remove_friendship_by_username(home_view.PLAYER[0], user_delete)
    entry_name = None
    root.destroy()
    root = None
    main()

def handle_add_click():
    global entry_name
    global root
    user_add = entry_name.get()
    database_interaction.add_friendship_by_username(home_view.PLAYER[0], user_add)
    entry_name = None
    root.destroy()
    root = None
    main()



def callback(event):
    selection = event.widget.curselection()
    global entry_name
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        entry_name.delete(0,tk.END)
        entry_name.insert(0, data)
    else:
        entry_name.insert(0, "")


def main():
    global listbox
    global root
    global friend_list
    root = tk.Tk()

    # use width x height + x_offset + y_offset (no spaces!)
    root.configure(background='#4169E1')
    root.geometry("640x480")
    root.title('listbox with scrollbar')
    root.grid_rowconfigure(1, {'minsize': 110})
    for i in range(2, 10):
        root.grid_rowconfigure(i, {'minsize': 65})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 60})

    load = Image.open("Earth-icon.png")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render, bg="#4169E1")
    img.image = render
    img.place(x=0, y=0, relwidth=1, relheight=1)

    load2 = Image.open("images/logos/friends.png")
    render2 = ImageTk.PhotoImage(load2)
    img = tk.Label(root, image=render2, bg="#4169E1")
    img.image = render2
    img.grid(row=0, column=0, columnspan=8, rowspan=2, sticky=tk.W + tk.E)
    # create the listbox (height/width in char)
    listbox = tk.Listbox(root, width=30, height=14, font=("Helvetica", 14))
    listbox.grid(row=2, rowspan=5, columnspan=3, column=0)
    listbox.bind("<<ListboxSelect>>", callback)

    user_label = tk.Label(
        text="user name",
        fg="white",
        bg="black",
        width=10,
    ).place(x=370, y=150)
    global entry_name
    entry_name = tk.Entry(width=20, text="user name", master=root)
    entry_name.place(x=470, y=150)
    # entry_name.insert(0, userName)
    removeFriend = tk.Button(
        root,
        text="Remove friend",
        width=24,
        height=1,
        bg="red",
        fg="black",
        command=lambda: handle_remove_click()
    ).place(x=400, y=220)

    removeFriend = tk.Button(
        root,
        text="Add friend",
        width=24,
        height=1,
        bg="green",
        fg="black",
        command=lambda: handle_add_click()
    ).place(x=400, y=280)

    # create a vertical scrollbar to the right of the listbox
    yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
    yscroll.grid(row=2, rowspan=5, column=3, sticky='nsw')
    listbox.configure(yscrollcommand=yscroll.set)

    # now load the listbox with data
    friend_list = [
        'dudi', 'Tom', 'Jen', 'Adam', 'Ethel', 'Barb', 'Tiny',
        'Tim', 'Pete', 'Sue', 'Egon', 'Swen', 'Albert', 'Stew', 'Tom', 'Jen', 'Adam', 'Ethel', 'Barb', 'Tiny',
        'Tim', 'Pete', 'Sue', 'Egon', 'Swen', 'Albert', 'Stew', 'Tom', 'Jen', 'Adam', 'Ethel', 'Barb', 'Tiny',
        'Tim', 'Pete', 'Sue', 'Egon', 'Swen', 'Albert']
    for item in friend_list:
        # insert each new item to the end of the listbox
        listbox.insert('end', item)

    # optionally scroll to the bottom of the listbox
    lines = len(friend_list)
    listbox.yview_scroll(lines, 'units')

    backButton = tk.Button(
        root,
        text="Go Back",
        width=24,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_Back_click()
    ).place(x=225, y=440)

    root.mainloop()
