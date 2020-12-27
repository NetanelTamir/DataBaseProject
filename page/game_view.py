import tkinter as tk

import PIL
from PIL import Image, ImageTk
from PIL import Image

from core import utils
from core.Country import Country
from page import signup_view, home_view, view_utils

country_object = Country(154)
flight = ['israel', 'lebanon', 'USA']
Colors = ['#34568B', '#FF6F61', '#88B04B']
country_desc = ""


def handle_country_info_click():
    global country_object
    global country_desc
    global canvas
    country_object = Country(154)
    country_desc = country_object.get_description()
    canvas.delete("all")
    canvas.create_text(150, 150, width=300, fill="green", font="Times 10 bold",
                       text=country_desc)
    canvas.update()
    canvas.update()


def flight_click():
    global country_object
    global country_desc
    global canvas
    global flight
    l = []
    canvas.delete("all")
    for i in range(0, 3):
        l.append(tk.Button(
            canvas,
            text=flight[i],
            width=27,
            height=4,
            font=("Helvetica", 14),
            bg=Colors[i],
            fg="white",
            # command=new_
        ).place(relx=0, rely= + 0.33 * i))
    canvas.update()
    canvas.update()


def main():
    global canvas
    root = tk.Tk()
    country = "Spain"
    city = "Madrid"
    score = 168
    view_utils.init_root(root, "home view")
    view_utils.add_image(root, 'Carmen-sandiego-game-logo.png', relx=0.13, rely=0.05)
    country_city_banner = tk.Label(
        text="Your current location: " + country + " , " + city,
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=30,
    ).place(x=0, y=0)
    score_banner = tk.Label(
        text="Time Left: " + str(score) + " h",
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=20,
    ).place(x=400, y=0)

    canvas = tk.Canvas(root, bg="white", height=300, width=300)
    canvas.place(relx=0.10, rely=0.25)

    mapCanvas = tk.Canvas(root, height=200, width=200)
    mapCanvas.place(relx=0.65, rely=0.12)
    map_img = Image.open("images/maps/spain.png")
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
        # command=handle_click
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

    canvas.update()
    mapCanvas.update()
    root.mainloop()
