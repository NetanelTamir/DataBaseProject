import tkinter as tk

import PIL
from PIL import Image, ImageTk
from PIL import Image

from core import utils
from core.Country import Country
from page import signup_view, home_view, view_utils

GAME = None
LEVEL = None
Colors = ['#34568B', '#FF6F61', '#88B04B']
country_object = None
flight = None
country_desc = ''


# def update_country(new_country_id):

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
    canvas.delete("all")
    canvas.create_text(150, 150, width=300, fill="red", font="Times 10 bold",
                       text=message)
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
                        fg="white").place(relx=0, rely=+ 0.33 * 0)
    button2 = tk.Button(frame, text=flight[1].data[1], width=27, height=4, font=("Helvetica", 14), bg=Colors[1],
                        fg="white").place(relx=0, rely=+ 0.33 * 1)
    button3 = tk.Button(frame, text=flight[2].data[1], width=27, height=4, font=("Helvetica", 14), bg=Colors[2],
                        fg="white").place(relx=0, rely=+ 0.33 * 2)

    canvas.create_window(152, 152, window=frame, width=300, height=300)
    canvas.update()


def main():
    global canvas
    global GAME
    global LEVEL
    global country_object
    global flight
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
    ).place(x=10, y=0)
    score_banner = tk.Label(
        text="Time Left: " + str(GAME.time_left) + " h",
        font=("Helvetica", 13),
        background="#4169E1",
        fg="black",
        width=17,
    ).place(x=430, y=0)

    canvas = tk.Canvas(root, bg="white", height=300, width=300)
    canvas.place(relx=0.10, rely=0.25)

    mapCanvas = tk.Canvas(root, height=200, width=200)
    mapCanvas.place(relx=0.65, rely=0.12)
    try:
        map_img = Image.open("images/maps/" + map_src)
        map_img = map_img.resize((200, 200), PIL.Image.ANTIALIAS)
        root.map = mapImage = ImageTk.PhotoImage(map_img)
    except:
        flag_src = country.data[6]
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
