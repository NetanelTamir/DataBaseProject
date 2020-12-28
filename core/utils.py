from database_interaction import *
import random
#from core.Game import HINT_COST, FLIGHT_COST, NUMBER_OF_HOURS

QUESTION_TYPE = {0:"population", 1:"currency", 2:"flag", 3:"capital", 4:"language", 5:"map", 6:"incorrect"}
ATTR_LOCATION_IN_COUNTRY_ARRAY = {"capital":2, "population":3, "language":5, "flag":6, "map":1, "currency":4}
WETHER_DICT = {"1":"a","2":"b","3":"c","4":"d"}

"""
    Generate n new countries which are not in given set
"""
def get_new_countries(countries_set, number_of_countries):
    countries = []
    total_countries = get_number_of_countries()

    for i in range(number_of_countries):
        chosen = random.randrange(total_countries)
        while chosen in countries_set:
            chosen = random.randrange(total_countries)
        countries.append(chosen)

    return countries


"""
    Get random question type
"""
def get_random_question_type():
    idx = random.randrange(7)
    return QUESTION_TYPE[idx]


"""
    Generate questions for country
"""
def generate_questions(country):
    questions = []
    for type in country.questions_types:
        all_questions = get_questions_by_type(type)
        idx = random.randrange(0, len(all_questions))
        generic_question = all_questions[idx]
        real_question = build_real_question_from_generic_question(generic_question, type, country)
        questions.append(real_question)
    return questions


"""
    Generate real question from generic one
"""
def build_real_question_from_generic_question(generic_question, type, country):
    ret = {}
    attr = country.data[ATTR_LOCATION_IN_COUNTRY_ARRAY[type]]
    if type in [2,5]:
        attr = type
        generic_question.replace("_ATTR_", str(attr))
    else:
        generic_question.replace("_ATTR_", str(attr))
        ret["string"] = generic_question
    return generic_question


"""
    Get instruction for game
"""
def get_instructions():
    NUMBER_OF_HOURS = 168
    HINT_COST = 1
    FLIGHT_COST = 8
    return f"Welcome agent 007! We've got intel on Carmen San Diego's whereabouts. We're sending you to catch her!\n" \
        f"You need to act quickly - she's moving fast and she's about to commit a serious crime by the end of" \
        f" this week, according to our intel. You've got {NUMBER_OF_HOURS} to catch her!\n" \
        f"You can ask people around to see if they saw her, but it will cost you time; {HINT_COST} hour for " \
        f"questioning people and {FLIGHT_COST} hours for switching countries. Keep that in mind before making " \
        f"any move!\nWe're counting on you. Good luck!"


"""
    Get country description
"""
def get_country_description(country_data):
    # country_name, capital_name, population, currency, languages, flag, region, area, gdp, climate
    desc = f"Welcome to {country_data[1]}! Here is some infromation about this wonderful country:\n" \
           f"Our capital is {country_data[2]}, the size of our country is  {country_data[8]} square meters and our gdp is {country_data[9]} USD.\nOur " \
           f"currency is called the {country_data[4]}.\nWe are located in the {country_data[7]} region.\n"
    if country_data[2] != "":
        desc += f"We also have a population of {country_data[3]} people.\n"
    if country_data[10] != "" and country_data[10] != "5" and country_data[10] != "0": # climate
        climate=""
        if(country_data[10]==1):
            climate = "Our climate is - dry tropical or tundra and ice"
        if (country_data[10] == 2):
            climate = "Our climate is - wet tropical"
        if (country_data[10] == 3):
            climate = "Our climate is - temperate humid subtropical and temperate continental"
        if (country_data[10] == 4):
            climate = "Our climate is - dry hot summers and wet winters"
        desc += climate
    return desc


"""
    Generate incorrect question
"""
def get_incorrect_question():
    all_questions = get_questions_by_type("incorrect")
    idx = random.randrange(len(all_questions))
    return all_questions[idx]


def get_random_city_from_list_by_id(id):
    all_cities = get_cities_by_country_id(id)
    idx = random.randrange(len(all_cities))
    return all_cities[idx]