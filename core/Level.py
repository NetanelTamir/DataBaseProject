import random
from core.Country import Country
from core.Game import HINT_COST, FLIGHT_COST

class Level():
    def __init__(self, countries, src):
        self.countries = countries
        self.start = src
        idx = self.start
        while idx == self.start:
            idx = random.randrange(len(self.countries))
        self.dst = idx
        self.time_left = 0

    def run(self, time_left):
        self.time_left = time_left
        country = Country(self.start)
        id = level_main_view(self, country)
        if not self.is_real_dest(id):

        print("run level")

    def get_dst(self):
        return self.dst

    def get_possible_destinations(self):
        possible_destinations = []
        for c in self.countries:
            country = Country(c)
            possible_destinations.append(country)
        return possible_destinations

    def is_real_dest(self, dest_to_check):
        return dest_to_check == self.dst

    def user_used_hint(self):
        self.time_left -= HINT_COST
        return self.time_left > 0

    def user_switched_country(self):
        self.time_left -= FLIGHT_COST
        return self.time_left > 0