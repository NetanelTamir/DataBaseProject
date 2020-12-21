from database_interaction import *
from core.utils import get_random_question_type, build_real_question_from_generic_question
import random

class Country():
    def __init__(self, id):
        self.id = id
        self.data = get_country_by_id(id)
        self.cities = get_cities_by_countryid(id)
        self.questions_types = set()
        self.questions = None
        self.cities = None
        while len(self.questions_types) < 3:
            type = get_random_question_type()
            if type == "incorrect":
                continue
            self.questions_types.add(type)

    def generate_questions_and_cities(self):
        questions = []
        cities = []
        for type in self.questions_types:
            all_questions = get_questions_by_type(type)
            idx = random.randrange(0, len(all_questions))
            generic_question = all_questions[idx]
            real_question = build_real_question_from_generic_question(generic_question, type, self)
            questions.append(real_question)
        all_cities = get_cities_by_countryid(self.id)
        idx_list = random.sample(range(len(all_cities)), len(self.questions_types))
        for idx in idx_list:
            cities.append(all_cities[idx][1])
        return questions, cities

    def get_questions_and_cities(self):
        if not self.questions:
            self.questions, self.cities = self.generate_questions_and_cities()
        return self.questions, self.cities

    def make_wrong(self):
        self.questions = []
        all_questions = get_questions_by_type("incorrect")
        idxs = random.sample(range(len(all_questions)), 3)
        for idx in idxs:
            self.questions.append(all_questions[idx])

    def get_locations(self, city_name):
        # NUMBER_OF_LOCATIONS_OF_EACH_TYPE = 4
        # LOCATIONS_TYPES = ("buy", "sleep", "eat", "drink", "go", "see", "do", "other", "diplomatic-representation")
        NUMBER_OF_LOCATIONS = 15
        all_locations = get_locations_by_city_name(city_name)
        chosen_locations = []
        idx_list = random.sample(range(len(all_locations)), NUMBER_OF_LOCATIONS)
        for idx in idx_list:
            chosen_locations.append(all_locations[idx])
        return chosen_locations

