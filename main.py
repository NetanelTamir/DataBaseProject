import database_interaction
import dataset_parsing
from page import login_view

database_interaction.create_connection()
#database_interaction.fill_locations()
login_view.main()
