from core.Level import Level
from core.utils import get_new_countries
import random
from database_interaction import get_number_of_countries

NUMBER_OF_LEVELS = 5
NUMBER_OF_HOURS = 168
NUMBER_OF_COUNTRIES_IN_LEVEL = 4
HINT_COST = 3
FLIGHT_COST = 8

class Game():
    def __init__(self):
        self.number_of_levels = NUMBER_OF_LEVELS
        self.current_level = 0
        self.countries_used = set()
        self.start = random.random(get_number_of_countries())
        self.countries_used.add(self.start)
        self.levels = self.create_levels(self.start)
        self.time_left = NUMBER_OF_HOURS

    def run(self):
        start_game_view()
        while self.current_level < self.number_of_levels:
            level = self.levels[self.current_level]
            time_left = level.run(self.time_left)
            if time_left <= 0:
                self.game_lost()
                return
            self.time_left = time_left
            self.current_level += 1
        self.game_won()

    def game_lost(self):
        game_lost_window()
        print("game lost")
        # go to lose page

    def game_won(self):
        game_won_window()
        print("game won")
        # go to win page

    def create_levels(self, src):
        l = []
        for i in range(self.number_of_levels):
            # randomize countries
            countries = get_new_countries(self.countries_used, NUMBER_OF_COUNTRIES_IN_LEVEL - 1)
            for c in countries:
                self.countries_used.add(c)
            level = Level(countries, src)
            src = level.get_dst()
            l.append(level)
        print("create levels")
        return l