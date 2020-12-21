import tkinter as tk
import database_interaction
from page import view_utils
from page import home_view

root = None
entry_name = None
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
    if(currentLocationId == -1):
        return
    database_interaction.remove_favorite_location(home_view.PLAYER[0], currentLocationId)
    entry_name = None
    root.destroy()
    root = None
    main()

# def handle_add_click():
#     global entry_name
#     global root
#     user_add = entry_name.get()
#     database_interaction.add_friendship_by_username(home_view.PLAYER[0], user_add)
#     entry_name = None
#     root.destroy()
#     root = None
#     main()

def splitByLength(data):
    splitedData = data.split(" ")
    finalStr = ""
    counter = 0
    for word in splitedData:
        if(counter + len(word) >= NUM_OF_CHARACTERS_IN_ROW):
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
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        for item in favoriteLocations:
            if item[1] == data:
                currentLocationId = item[0]
                dataToShow = splitByLength(item[5])
                entry_name.delete("1.0","end")
                entry_name.insert("1.0", dataToShow)
    else:
        entry_name.insert(0, "")


def main():
    global listbox
    global root
    global favoriteLocations
    root = tk.Tk()
    view_utils.init_root(root, "favorite locations view")
    view_utils.add_background(root, "Earth-icon.png")
    view_utils.add_title_image(root, "favorite_locations.png")

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
        text="Country descriptions",
        fg="white",
        bg="black",
        width=17,
    ).place(x=360, y=110)
    global entry_name
    entry_name = tk.Text(width=20, master=root)
    entry_name.place(x=280, y=150,height=140,width=300)

    remove_favorite_location = tk.Button(
        root,
        text="Remove locations",
        width=24,
        height=1,
        bg="red",
        fg="black",
        command=lambda: handle_remove_click()
    ).place(x=340, y=320)
    # addFriend = tk.Button(
    #     root,
    #     text="Add country",
    #     width=24,
    #     height=1,
    #     bg="green",
    #     fg="black",
    #     command=lambda: handle_add_click()
    # ).place(x=340, y=360)
    yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
    yscroll.grid(row=2, rowspan=4, column=3, sticky='nsw')
    listbox.configure(yscrollcommand=yscroll.set)
    favoriteLocations = database_interaction.get_favorite_locations_by_user_id(PLAYER[0])
    #favoriteLocations = [("Israel", "fsafafsaafafafaffmkvnsssssssssssssf fsafa ksafksfksafklnlks anlfasfaaaaaaaaab"),("Israel2", "fsaffsafaasfaa fsfsafsaaf afa faffmkvfsaffsasfmksaf ksfksafkln lksanl fasf")]
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
    ).place(x=225, y=440)

    root.mainloop()
