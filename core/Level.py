import random
from core.Country import Country
from core.utils import get_incorrect_question, get_random_question_type, get_questions_by_type, build_real_question_from_generic_question

class Level():
    def __init__(self, countries, src):
        self.countries = countries
        self.start = src
        idx = random.randrange(len(self.countries))
        self.dst = countries[idx]
        self.wrong_country = False
        self.destinations = None
        self.questions_types = set()
        self.questions = None
        while len(self.questions_types) < 3:
            type = get_random_question_type()
            if type == "incorrect":
                continue
            self.questions_types.add(type)

    """
        Return src country of level
    """
    def get_src_country(self):
        country = Country(self.start)
        return country


    """
        React to user's choice
    """
    def user_chose_dest(self, dst):
        if self.is_real_dest(dst):
            return True
        else:
            return False, get_incorrect_question()


    """
        Get specipic country of level by it's ID. Return None if not a possible dst
    """
    def get_specific_dst(self, id):
        if id not in self.countries:
            return None
        for dst in self.get_possible_destinations():
            if dst.data[0] == id:
                return dst
        # error handling
        return None


    """
        Return correct destination of level
    """
    def get_dst(self):
        return self.dst

    def get_dst_as_country(self):
        return Country(self.dst)


    """
        Get all possible destinations of level
    """
    def get_possible_destinations(self):
        if not self.destinations:
            possible_destinations = []
            for c in self.countries:
                country = Country(c)
                possible_destinations.append(country)
            self.destinations = possible_destinations
        return self.destinations


    """
        Get real destination of level
    """
    def is_real_dest(self, dest_to_check):
        return dest_to_check == self.dst


    def generate_questions(self):
        questions = []
        for type in self.questions_types:
            all_questions = get_questions_by_type(type)
            idx = random.randrange(0, len(all_questions))
            generic_question = all_questions[idx]
            generic_question = generic_question[0]
            real_question = build_real_question_from_generic_question(generic_question, type, self.get_dst_as_country())
            questions.append(real_question)
        return questions

    """
        Return questions list 
    """

    def get_hints(self):
        if not self.questions:
            self.questions = self.generate_questions()
        return self.questions