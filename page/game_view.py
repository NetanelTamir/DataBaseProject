import tkinter as tk

import PIL
from PIL import Image, ImageTk
from PIL import Image

from core import utils
from core.Country import Country
from page import signup_view, home_view, view_utils, Winner_view, lost_view

root = None
GAME = None
LEVEL = None
Colors = ['#34568B', '#FF6F61', '#88B04B']
country_object = None
flight = None
country_desc = ''
canvas = None
mapCanvas = None
time_label = None
country_city_banner = None


def handle_flight_choose(flight_obj):
    global GAME
    global LEVEL
    global root
    global country_object
    global mapCanvas
    global flight
    id = flight_obj.data[0]
    if LEVEL.is_real_dest(id):
        GAME.level_done()
        if GAME.is_game_won():
            root.destroy()
            Winner_view.main(home_view.PLAYER, GAME.get_score())
        else:
            GAME.user_switched_country()
            update_time()
            LEVEL = GAME.get_level()
            country_object = LEVEL.get_src_country()
            flight = LEVEL.get_possible_destinations()
            country = country_object.get_country_name()
            city = country_object.get_src_city()
            map_src = country_object.get_map()
            country_city_banner.config(text="Your current location: " + country + " , " + city)
            handle_country_info_click()
            mapCanvas.delete("all")
            map_img = Image.open("images/maps/" + map_src)
            map_img = map_img.resize((200, 200), PIL.Image.ANTIALIAS)
            root.map = mapImage = ImageTk.PhotoImage(map_img)
            mapCanvas.create_image(100, 100, image=mapImage)
    else:
        inco = utils.get_incorrect_question()
        GAME.user_switched_country()
        GAME.user_switched_country()
        canvas.delete("all")
        canvas.create_text(150, 150, width=300, fill="green", font="Times 10 bold",
                           text=f"Local person says: {inco}\n\nYou are probably at the wrong place..."
                                f" We are sending you back to the country you came from.")
        canvas.update()
        canvas.update()
        update_time()


def update_time():
    global time_label
    if GAME.is_game_lost():
        root.destroy()
        lost_view.main(home_view.PLAYER, GAME.get_score())
    else:
        time_label.config(text="Time Left: " + str(GAME.time_left) + " h")


def handle_country_info_click():
    global country_object
    global country_desc
    global canvas
    country_desc = country_object.get_description()
    canvas.delete("all")
    canvas.create_text(150, 150, width=300, fill="green", font="Times 10 bold",
                       text=country_desc)
    canvas.update()
    canvas.update()


def handel_single_hint(message):
    GAME.user_used_hint()
    update_time()
    canvas.delete("all")
    if message[0]:
        img = Image.open("images/" + message[2])
        img = img.resize((200, 200), PIL.Image.ANTIALIAS)
        mapImage = ImageTk.PhotoImage(img)
        canvas.create_image(100, 100, image=mapImage)
    canvas.create_text(150, 150, width=300, fill="red", font="Times 10 bold",
                       text=message[1])
    canvas.update()
    canvas.update()


def handle_hint():
    canvas.delete("all")
    global country_object
    hints = country_object.get_hints()
    frame = tk.Frame()
    button1 = tk.Button(frame, text='Hint 1', width=27, height=4, font=("Helvetica", 14), bg=Colors[0],
                        fg="white", command=lambda: handel_single_hint(hints[0])).place(relx=0, rely=+ 0.33 * 0)
    button2 = tk.Button(frame, text='Hint 2', width=27, height=4, font=("Helvetica", 14), bg=Colors[1],
                        fg="white", command=lambda: handel_single_hint(hints[1])).place(relx=0, rely=+ 0.33 * 1)
    button3 = tk.Button(frame, text='Hint 3', width=27, height=4, font=("Helvetica", 14), bg=Colors[2],
                        fg="white", command=lambda: handel_single_hint(hints[2])).place(relx=0, rely=+ 0.33 * 2)

    canvas.create_window(152, 152, window=frame, width=300, height=300)
    canvas.update()


def flight_click():
    global country_object
    global country_desc
    global canvas
    global flight
    l = []
    canvas.delete("all")
    frame = tk.Frame()
    button1 = tk.Button(frame, text=flight[0].data[1], width=27, height=4, font=("Helvetica", 14), bg=Colors[0],
                        fg="white", command=lambda: handle_flight_choose(flight[0])).place(relx=0, rely=+ 0.33 * 0)
    button2 = tk.Button(frame, text=flight[1].data[1], width=27, height=4, font=("Helvetica", 14), bg=Colors[1],
                        fg="white", command=lambda: handle_flight_choose(flight[1])).place(relx=0, rely=+ 0.33 * 1)
    button3 = tk.Button(frame, text=flight[2].data[1], width=27, height=4, font=("Helvetica", 14), bg=Colors[2],
                        fg="white", command=lambda: handle_flight_choose(flight[2])).place(relx=0, rely=+ 0.33 * 2)

    canvas.create_window(152, 152, window=frame, width=300, height=300)
    canvas.update()


def main():
    global canvas
    global GAME
    global LEVEL
    global country_object
    global flight
    global time_label
    global country_city_banner
    global root
    global mapCanvas
    GAME = home_view.GAME
    LEVEL = GAME.get_level()
    country_object = LEVEL.get_src_country()
    flight = LEVEL.get_possible_destinations()
    root = tk.Tk()
    country = country_object.get_country_name()
    city = country_object.get_src_city()
    map_src = country_object.get_map()
    score = 168
    #############
    view_utils.init_root(root, "home view")
    view_utils.add_image(root, 'Carmen-sandiego-game-logo.png', relx=0.13, rely=0.05)
    country_city_banner = tk.Label(
        text="Your current location: " + country + " , " + city,
        font=("Helvetica", 13),
        background="#4169E1",
        fg="black",
        width=40,
    )
    country_city_banner.place(x=10, y=0)
    time_label = tk.Label(
        text="Time Left: " + str(GAME.time_left) + " h",
        font=("Helvetica", 13),
        background="#4169E1",
        fg="black",
        width=17,
    )
    time_label.place(x=430, y=0)
    canvas = tk.Canvas(root, bg="white", height=300, width=300)
    canvas.place(relx=0.10, rely=0.25)

    mapCanvas = tk.Canvas(root, height=200, width=200)
    mapCanvas.place(relx=0.65, rely=0.12)
    try:
        map_img = Image.open("images/maps/" + map_src)
        map_img = map_img.resize((200, 200), PIL.Image.ANTIALIAS)
        root.map = mapImage = ImageTk.PhotoImage(map_img)
    except:
        flag_src = country_object.data[6]
        map_img = Image.open("images/maps/" + flag_src)
        map_img = map_img.resize((200, 200), PIL.Image.ANTIALIAS)
        root.map = mapImage = ImageTk.PhotoImage(map_img)

    mapCanvas.create_image(100, 100, image=mapImage)

    country_info = tk.Button(
        root,
        text="Information about this country",
        width=30,
        height=1,
        bg="black",
        fg="white",
        command=handle_country_info_click
    ).place(relx=0.635, rely=0.57)

    location_info = tk.Button(
        root,
        text="Information about POI in this city",
        width=30,
        height=1,
        bg="black",
        fg="white",
        # command=handle_click
    ).place(relx=0.635, rely=0.65)

    get_hint = tk.Button(
        root,
        text="Ask the locals for help",
        width=30,
        height=1,
        bg="black",
        fg="white",
        command=lambda: handle_hint()
    ).place(relx=0.635, rely=0.73)

    fly = tk.Button(
        root,
        text="Fly to next destination",
        width=30,
        height=1,
        bg="black",
        fg="white",
        command=lambda: flight_click()
    ).place(relx=0.635, rely=0.81)

    start_text = utils.get_instructions()
    canvas.create_text(150, 150, width=300, fill="darkblue", font="Times 10 italic bold",
                       text=start_text)
    canvas.update()
    mapCanvas.update()
    root.mainloop()
