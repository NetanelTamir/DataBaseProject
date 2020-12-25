import random
from core.Country import Country
from core.utils import get_incorrect_question

class Level():
    def __init__(self, countries, src):
        self.countries = countries
        self.start = src
        idx = random.randrange(len(self.countries))
        self.dst = idx
        self.wrong_country = False
        self.destinations = None


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


