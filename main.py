import database_interaction
import dataset_parsing
from page import login_view

database_interaction.create_connection()
login_view.main()
