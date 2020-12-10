from database_interaction import get_country_by_id, get_cities_by_countryid
from core.utils import get_random_question_type

class Country():
    def __init__(self, id):
        self.id = id
        self.data = get_country_by_id(id)
        self.cities = get_cities_by_countryid(id)
        self.questions_types = set()
        while len(self.questions_types) < 3:
            type = get_random_question_type()
            if type == "incorrect":
                continue
            self.questions_types.add(type)
