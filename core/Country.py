from database_interaction import *
from core.utils import *
import random


class Country():
    def __init__(self, id):
        self.id = id
        self.data = get_country_by_id(id)
        self.city = get_random_city_from_list_by_id(id)


    """
        Get locations of city
    """
    def get_locations(self):
        NUMBER_OF_LOCATIONS = 10
        all_locations = get_locations_by_city_id(self.get_src_city_id())
        chosen_locations = []
        if len(all_locations) < NUMBER_OF_LOCATIONS:
            return all_locations
        idx_list = random.sample(range(len(all_locations)), NUMBER_OF_LOCATIONS)
        for idx in idx_list:
            chosen_locations.append(all_locations[idx])
        for i in range(len(chosen_locations)):
            if chosen_locations[i][2] == "diplomatic-representation":
                chosen_locations[i][2] = "diplomatic"
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
        return self.city[1]


    def get_src_city_id(self):
        return self.city[0]


    def get_flag(self):
        return self.data[6]


    def get_id(self):
        return self.id