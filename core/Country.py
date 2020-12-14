from database_interaction import get_country_by_id, get_cities_by_countryid,get_questions_by_type
from core.utils import get_random_question_type, build_real_question_from_generic_question
import random

class Country():
    def __init__(self, id):
        self.id = id
        self.data = get_country_by_id(id)
        self.cities = get_cities_by_countryid(id)
        self.questions_types = set()
        self.questions = None
        while len(self.questions_types) < 3:
            type = get_random_question_type()
            if type == "incorrect":
                continue
            self.questions_types.add(type)

    def generate_questions(self):
        questions = []
        for type in self.questions_types:
            all_questions = get_questions_by_type(type)
            idx = random.randrange(0, len(all_questions))
            generic_question = all_questions[idx]
            real_question = build_real_question_from_generic_question(generic_question, type, self)
            questions.append(real_question)
        return questions

    def get_questions(self):
        if not self.questions:
            self.questions = self.get_questions()
        return self.questions