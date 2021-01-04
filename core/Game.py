from core.Level import Level
from core.utils import get_new_countries
import random
from Database_Interaction import get_number_of_countries

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
        self.start = random.randrange(1, get_number_of_countries())
        self.countries_used.add(self.start)
        self.levels = self.create_levels(self.start)
        self.time_left = NUMBER_OF_HOURS

    """
        Get next level
    """

    def get_level(self):
        return self.levels[self.current_level]

    """
        Update current level once a level is done
    """

    def level_done(self):
        self.current_level += 1

    """
        Check if all levels are done and that player is on time
    """

    def is_game_won(self):
        return self.current_level >= self.number_of_levels and self.time_left >= 0

    """
        Check if there is still time left
    """

    def is_game_lost(self):
        return self.time_left <= 0

    """
        Generate levels for game
    """

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

    """
        Update time after hint
    """

    def user_used_hint(self):
        self.time_left -= HINT_COST

    """
        Update time after flight
    """

    def user_switched_country(self):
        self.time_left -= FLIGHT_COST

    def get_score(self):
        score = self.time_left / NUMBER_OF_HOURS * 100. + 20 * self.current_level
        return round(score)
