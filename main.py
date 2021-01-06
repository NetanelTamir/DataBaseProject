import Database_Interaction
from page import login_view

Database_Interaction.create_connection()
login_view.main()
Database_Interaction.close_connection()
