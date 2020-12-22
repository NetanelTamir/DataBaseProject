from database_interaction import get_number_of_countries, get_questions_by_type
import random
from core.Game import HINT_COST, FLIGHT_COST, NUMBER_OF_HOURS

QUESTION_TYPE = {0:"population", 1:"currency", 2:"flag", 3:"capital", 4:"language", 5:"map", 6:"incorrect"}
ATTR_LOCATION_IN_COUNTRY_ARRAY = {"capital":1, "population":2, "language":4, "flag":5, "map":0, "currency":3}
WETHER_DICT = {"1":"a","2":"b","3":"c","4":"d"}

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
    ret = {}
    attr = country[ATTR_LOCATION_IN_COUNTRY_ARRAY[type]]
    if type in ["flag", "map"]:
        ret["file"] = attr
        ret["string"] = generic_question
    else:
        generic_question.replace("_ATTR_", attr)
        ret["string"] = generic_question
    return generic_question

def get_instructions():
    return f"Welcome agent 007! We've got intel on Carmen San Diego's whereabout. Wer'e sending you to catch her!\n" \
        f"You need to act quickly - she's moving fast and shes about to commit a serious crime by the end of" \
        f" this week, according to our intel. So you've got {NUMBER_OF_HOURS} to catch her!\n" \
        f"You can ask people around to see if they saw her, but it will cost you time; {HINT_COST} hours for " \
        f"questioning people and {FLIGHT_COST} hours for switching countries. Keep that in mind before making " \
        f"any move!\nWer'e counting on you. Good luck!"

def get_country_description(country_data):
    # country_name, capital_name, population, currency, languages, flag, region, area, gdp, climate
    desc = f"Welcome to {country_data[0]}! Here is some infromation about this wonderful country:\n" \
           f"Our capital is {country_data[1]}, we are speaking here in {country_data[4]} and we " \
           f"are using the {country_data[3]} currency. We are located on the {country_data[5]} region. "
    if country_data[2] != "":
        desc += f"We also have a population of {country_data[2]} people. "
    if country_data[9] != "" and country_data[9] != "5": # climate
        climate = "Our wether here is "
        if country_data[9].count(",") > 0:
            climate_list = country_data.split(",")
            for i in range(len(climate_list) - 1):
                if climate_list[i] == 5:
                    continue
                climate += WETHER_DICT[climate_list[i]]
                if i == len(climate_list) - 2 and climate_list[i + 1] != 5:
                    climate += " and "
            if climate_list[len(climate_list) - 1] != 5:
                climate += WETHER_DICT[climate_list[len(climate_list) - 1]]
        else:
            climate += WETHER_DICT[country_data[9]]
        desc += climate
    return desc

