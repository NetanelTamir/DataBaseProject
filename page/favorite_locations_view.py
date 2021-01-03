import tkinter as tk
import Database_Interaction
from page import view_utils
from page import home_view

root = None
entry_name = None
url_place = None
NUM_OF_CHARACTERS_IN_ROW = 38
currentLocationId = -1
favoriteLocations = None


def handle_Back_click():
    global root
    root.destroy()
    home_view.main()


def handle_remove_click():
    global entry_name
    global root
    if (currentLocationId == -1):
        return
    Database_Interaction.remove_favorite_location(home_view.PLAYER[0], currentLocationId)
    entry_name = None
    root.destroy()
    root = None
    main()


def splitByLength(data):
    splitedData = data.split(" ")
    finalStr = ""
    counter = 0
    for word in splitedData:
        if (counter + len(word) >= NUM_OF_CHARACTERS_IN_ROW):
            finalStr += "\n" + word + " "
            counter = len(word)
        else:
            counter += len(word)
            finalStr += word + " "
    return finalStr


def callback(event):
    global favoriteLocations
    global currentLocationId
    selection = event.widget.curselection()
    global entry_name
    global url_place
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        for item in favoriteLocations:
            if item[1] == data:
                currentLocationId = item[0]
                dataToShow = item[5]
                url = item[4]
                entry_name.configure(state='normal')
                url_place.configure(state='normal')
                entry_name.delete("1.0", "end")
                entry_name.insert("1.0", dataToShow)
                url_place.delete("1.0", "end")
                url_place.insert("1.0", url)
                entry_name.configure(state='disabled')
                url_place.configure(state='disabled')

    else:
        try:
            entry_name.insert(0, "")
        except Exception:
            pass


def main():
    global listbox
    global root
    global favoriteLocations
    root = tk.Tk()
    view_utils.init_root(root, "favorite locations view")
    view_utils.add_background(root, "Earth-icon.png")
    view_utils.add_title_image(root, "favorite_locations.png", relx=0.27, rely=0)

    PLAYER = home_view.PLAYER
    root.grid_rowconfigure(1, {'minsize': 110})
    for i in range(2, 10):
        root.grid_rowconfigure(i, {'minsize': 65})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 60})

    listbox = tk.Listbox(root, width=14, height=12, font=("Helvetica", 14))
    listbox.grid(row=2, rowspan=4, columnspan=2, column=1)
    listbox.bind("<<ListboxSelect>>", callback)

    description_label = tk.Label(
        text="Description",
        fg="white",
        bg="black",
        width=17,
    ).place(x=408, y=60)
    global entry_name
    entry_name = tk.Text(width=20, wrap="word", master=root)
    entry_name.configure(state='disabled')
    entry_name.place(x=320, y=100, height=200, width=300)

    global url_place
    url_place = tk.Text(width=20, master=root)
    url_place.configure(state='disabled')
    url_place.place(x=320, y=350, height=30, width=300)

    url_label = tk.Label(
        text="URL",
        fg="white",
        bg="black",
        width=17,
    ).place(x=408, y=320)

    remove_favorite_location = tk.Button(
        root,
        text="Remove location",
        width=24,
        height=1,
        bg="red",
        fg="black",
        command=lambda: handle_remove_click()
    ).place(x=59, y=410)
    yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
    yscroll.grid(row=2, rowspan=4, column=3, sticky='nsw')
    listbox.configure(yscrollcommand=yscroll.set)
    xscroll = tk.Scrollbar(command=listbox.xview, orient=tk.HORIZONTAL)
    xscroll.place(x=60, y=390, width=175)
    listbox.configure(xscrollcommand=xscroll.set)
    favoriteLocations = Database_Interaction.get_favorite_locations_by_user_id(PLAYER[0])
    for item in favoriteLocations:
        listbox.insert('end', item[1])

    lines = len(favoriteLocations)
    listbox.yview_scroll(lines, 'units')

    backButton = tk.Button(
        root,
        text="Go Back",
        width=24,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_Back_click()
    ).place(x=235, y=440)

    root.mainloop()
