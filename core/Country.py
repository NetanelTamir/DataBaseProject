from database_interaction import *
from core.utils import *
import random


class Country():
    def __init__(self, id):
        self.id = id
        self.data = get_country_by_id(id)
        self.data[2] = get_random_city_from_list_by_id(id)
        self.questions_types = set()
        self.questions = None
        self.cities = None
        self.wrong = False
        while len(self.questions_types) < 3:
            type = get_random_question_type()
            if type == "incorrect":
                continue
            self.questions_types.add(type)

    """
        Generate the lists of questions and cities
    """

    def generate_questions(self):
        questions = []
        for type in self.questions_types:
            all_questions = get_questions_by_type(type)
            idx = random.randrange(0, len(all_questions))
            generic_question = all_questions[idx]
            generic_question = generic_question[0]
            real_question = build_real_question_from_generic_question(generic_question, type, self)
            questions.append(real_question)
        return questions

    """
        Return questions list 
    """

    def get_hints(self):
        if not self.questions:
            self.questions = self.generate_questions()
        return self.questions

    """
        Get locations by city
    """

    def get_locations(self):
        NUMBER_OF_LOCATIONS = 15
        all_locations = get_locations_by_city_name(self.get_src_city)
        chosen_locations = []
        idx_list = random.sample(range(len(all_locations)), NUMBER_OF_LOCATIONS)
        for idx in idx_list:
            chosen_locations.append(all_locations[idx])
        return chosen_locations

    """
        Get string description of country
    """

    def get_description(self):
        return get_country_description(self.data)

    def get_map(self):
        map = self.data[1].lower()
        map = map.replace(" ", "_")
        map = map + '.png'
        return map

    def get_country_name(self):
        return self.data[1]

    def get_src_city(self):
        return self.data[2][1]

    def get_src_city_id(self):
        return self.data[2][0]

    def get_flag(self):
        return self.data[6]

    def get_id(self):
        return self.id
