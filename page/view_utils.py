import tkinter as tk
from PIL import Image, ImageTk

def init_root(root, title_name):
    root.geometry('640x480')
    root.configure(background='#4169E1')
    root.title(title_name)

def add_background(root, img_name):
    load = Image.open(img_name)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render, bg="#4169E1")
    img.image = render
    img.place(x=0, y=0, relwidth=1, relheight=1)

def add_title_image(root, image_name):
    load2 = Image.open("images/logos/" + image_name)
    render2 = ImageTk.PhotoImage(load2)
    img = tk.Label(root, image=render2, bg="#4169E1")
    img.image = render2
    img.grid(row=0, column=0, columnspan=10, rowspan=2, sticky=tk.W + tk.E)

def classic_grid(root):
    for i in range(1, 10):
        root.grid_rowconfigure(i, {'minsize': 64})
    for i in range(0, 10):
        root.grid_columnconfigure(i, {'minsize': 48})
