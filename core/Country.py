from database_interaction import get_country_by_id, get_cities_by_countryid

class Country():
    def __init__(self, id):
        self.id = id
        self.data = get_country_by_id(id)
        self.cities = get_cities_by_countryid(id)
