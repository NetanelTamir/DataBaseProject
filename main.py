from tkinter import *
from tkinter import messagebox

import Database_Interaction
from page import login_view

Database_Interaction.create_connection()
if Database_Interaction.connection != '' and Database_Interaction.connection.is_connected():
    login_view.main()
    Database_Interaction.close_connection()
else:
    Tk().withdraw()
    messagebox.showerror("Error", "Error connecting to database, please check config file")
