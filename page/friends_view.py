import tkinter as tk
import database_interaction
from page import view_utils
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
    view_utils.init_root(root, "friendship view")
    view_utils.add_background(root, "Earth-icon.png")
    view_utils.add_title_image(root, "friends.png")

    PLAYER = home_view.PLAYER
    root.grid_rowconfigure(1, {'minsize': 110})
    for i in range(2, 10):
        root.grid_rowconfigure(i, {'minsize': 65})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 60})

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

    removeFriend = tk.Button(
        root,
        text="Remove friend",
        width=24,
        height=1,
        bg="red",
        fg="black",
        command=lambda: handle_remove_click()
    ).place(x=400, y=220)
    addFriend = tk.Button(
        root,
        text="Add friend",
        width=24,
        height=1,
        bg="green",
        fg="black",
        command=lambda: handle_add_click()
    ).place(x=400, y=280)
    yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
    yscroll.grid(row=2, rowspan=5, column=3, sticky='nsw')
    listbox.configure(yscrollcommand=yscroll.set)
    friend_list = database_interaction.get_all_friendships_by_id(PLAYER[0])
    for item in friend_list:
        listbox.insert('end', item)

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
