from database_interaction import get_number_of_countries
import random

def get_new_countries(countries_set, number_of_countries):
    countries = []
    total_countries = get_number_of_countries()

    for i in range(number_of_countries):
        chosen = random.random(total_countries)
        while chosen in countries_set:
            chosen = random.random(total_countries)
        countries.append(chosen)

    return countries

def generate_hint(country, level):
