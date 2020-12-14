from database_interaction import get_number_of_countries, get_questions_by_type
import random

QUESTION_TYPE = {0:"population", 1:"currency", 2:"flag", 3:"capital", 4:"language", 5:"map", 6:"incorrect"}
ATTR_LOCATION_IN_COUNTRY_ARRAY = {"capital":1, "population":2, "language":3, "flag":4, "map":0, }

def get_new_countries(countries_set, number_of_countries):
    countries = []
    total_countries = get_number_of_countries()

    for i in range(number_of_countries):
        chosen = random.random(total_countries)
        while chosen in countries_set:
            chosen = random.random(total_countries)
        countries.append(chosen)

    return countries

def get_random_question_type():
    idx = random.randrange(7)
    return QUESTION_TYPE[idx]

def generate_questions(country):
    questions = []
    for type in country.questions_types:
        all_questions = get_questions_by_type(type)
        idx = random.randrange(0, len(all_questions))
        generic_question = all_questions[idx]
        real_question = build_real_question_from_generic_question(generic_question, type, country)
        questions.append()
    return questions

def build_real_question_from_generic_question(generic_question, type, country):
    return ''