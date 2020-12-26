import tkinter as tk

import PIL
from PIL import Image, ImageTk
from PIL import Image

from core.Country import Country
from page import signup_view, home_view, view_utils
country_object = Country(154)
def handle_country_info_click():
    global country_object
    #country_object.get_description()



def main():
    root = tk.Tk()
    country = "Spain"
    city = "Madrid"
    score = 130
    view_utils.init_root(root, "home view")
    view_utils.add_image(root, 'Carmen-sandiego-game-logo.png', relx=0.13, rely=0.05)
    country_city_banner = tk.Label(
        text="Your current location: "+country+" , "+city,
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=30,
    ).place(x=0, y=0)
    score_banner= tk.Label(
        text="Your score: "+ str(score),
        font=("Helvetica", 14),
        background="#4169E1",
        fg="black",
        width=20,
    ).place(x=400, y=0)

    canvas=tk.Canvas(root, bg="white", height=300, width=300)
    canvas.place(relx=0.10,rely=0.25)

    mapCanvas=tk.Canvas(root, height=200, width=200)
    mapCanvas.place(relx=0.65,rely=0.12)
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
        # command=handle_click
    ).place(relx=0.635, rely=0.81)

    canvas.update()
    mapCanvas.update()
    root.mainloop()
