from page import login_view
import Database_Interaction
import Dataset_Parsing

Database_Interaction.create_connection()
login_view.main()
