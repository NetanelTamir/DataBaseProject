import csv
import hashlib
import os
from datetime import date, datetime

import mysql.connector
from mysql.connector import Error
from mysql.connector import Error

from dataset_parsing import help_create_cities, create_cities, create_comments, create_questions, create_locations

connection = mysql.connector.connect(host='localhost', auth_plugin='mysql_native_password',
                                             database='carmen_sandiego',
                                             user='root',
                                             password='netanel')
cursor = None


def create_connection():
    try:
        global connection
        global cursor
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)


    except Error as e:
        print("Error while connecting to MySQL", e)


def close_connection():
    global connection
    connection.commit()


def fill_countries():
    global cursor

    with open('parsed_csvs/countries.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.countries (country_name,capital_name,population,currency,languages,flag,region,area,gdp,climate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for row in reader:
            row[2] = int(row[2].replace(',', ''))
            row[7] = int(row[7])
            try:
                row[8] = int(row[8])
            except:
                row[8] = 0
            try:
                row[9] = int(row[9])
            except:
                row[9] = 0

            cursor.execute(sql, row)


def fill_cities():
    global cursor
    # query = "LOAD DATA INFILE 'cities.csv' INTO TABLE carmen_sandiego.cities"
    # cursor.execute(query)

    with open('parsed_csvs/cities.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.cities (city, country) VALUES (%s,%s)"
        for row in reader:
            cursor.execute(sql, row)


def fill_comments():
    global cursor

    with open('parsed_csvs/comments.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.comments (comment_type, description) VALUES (%s,%s)"
        for row in reader:
            cursor.execute(sql, row)


def fill_questions():
    global cursor

    with open('parsed_csvs/questions.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.questions (question_type, description) VALUES (%s,%s)"
        for row in reader:
            cursor.execute(sql, row)


def fill_locations():
    global cursor
    with open('parsed_csvs/locations.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.locations (location_name, type, city,url,description) VALUES (%s,%s,%s,%s,%s)"
        for row in reader:
            cursor.execute(sql, row)


def fill_all():
    create_connection()
    fill_countries()
    fill_cities()
    fill_comments()
    fill_questions()
    close_connection()


# Gets Player By ID
def get_player_by_id(id):
    sql = "SELECT * FROM carmen_sandiego.players WHERE id_players='%s'" % (id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# Adds player to DB
def add_player(user):
    # (username,password,first_name,last_name)
    salt = str(os.urandom(32))
    password = user[1]
    hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    last_played = datetime.now()

    sql = "INSERT INTO carmen_sandiego.players (user_name,password,salt,first_name,last_name,last_played) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (user[0], hash, salt, user[2], user[3], last_played))

    return


# Returns PlayerID if username and password exist in DB, -1 otherwise
def log_in(username, password):
    sql = "SELECT * FROM carmen_sandiego.players WHERE user_name='%s'" % (username)
    cursor.execute(sql)
    res = cursor.fetchall()[0]

    salt = res[3]
    hash = res[2]
    if (hashlib.sha256((password + salt).encode('utf-8')).hexdigest() == hash):
        sql = "UPDATE carmen_sandiego.players SET last_played = '%s' WHERE user_name = '%s'" % (
            datetime.now(), username)
        cursor.execute(sql)

        sql = "SELECT * FROM carmen_sandiego.players WHERE user_name='%s'" % (username)
        cursor.execute(sql)
        res = cursor.fetchall()[0][0]
        return res
    return -1


# Adds friendship to DB
def add_friendship(id1, id2):
    sql = "INSERT INTO carmen_sandiego.friendships (id_friendships_a,id_friendships_b) VALUES (%s,%s)"

    try:
        if (id1 < id2):
            cursor.execute(sql, (id1, id2))
        else:
            cursor.execute(sql, (id2, id1))
    except:
        print("Friendship exists already ")


# Returns the ids of players who are friends with id
def get_all_friendships_by_id(id):
    sql = "SELECT * FROM carmen_sandiego.friendships WHERE id_friendships_a='%s'" % (id)
    cursor.execute(sql)
    res1 = cursor.fetchall()
    sql = "SELECT * FROM carmen_sandiego.friendships WHERE id_friendships_b='%s'" % (id)
    cursor.execute(sql)
    res2 = cursor.fetchall()
    res = res1 + res2
    return_list = []
    for i in res:
        for j in i:
            if (j != id):
                return_list.append(j)
    return sorted(return_list)


# Updates DB with new high_score
def update_highscore_table(id, score):
    sql = "SELECT * FROM carmen_sandiego.high_scores WHERE id_players='%s' and score='%s'" % (id, score)
    cursor.execute(sql)
    res = cursor.fetchall()

    if len(res) == 0:
        sql = "INSERT INTO carmen_sandiego.high_scores (id_players,score,date) VALUES (%s,%s,%s)"
        cursor.execute(sql, (id, score, datetime.now()))

    else:
        sql = "UPDATE carmen_sandiego.high_scores SET date ='%s' WHERE id_players = '%s' and score='%s'" % (
            datetime.now(), id, score)
        cursor.execute(sql)


# Gets HighScores (No Repeats)
def get_highscores_no_repeats():
    sql = "SELECT id_players,max(score) AS score FROM carmen_sandiego.high_scores GROUP BY id_players;"
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# Gets HighScores (Yes Repeats)
def get_highscores_yes_repeats():
    sql = "SELECT * FROM carmen_sandiego.high_scores;"
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# Gets HighScores (No Repeats - Friends Only)
def get_highscores_no_repeats_friends(id):
    sql = '''SELECT id_players,max(score) AS score FROM carmen_sandiego.high_scores
             WHERE (id_players in (SELECT id_friendships_a FROM friendships WHERE id_friendships_b='%s') or
		     id_players in (SELECT id_friendships_b FROM friendships WHERE id_friendships_a='%s' ) or
		      id_players = '%s') group by id_players;''' % (id, id, id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# Gets Average Score for each player
def get_highscores_avg_scores():
    sql = '''SELECT id_players,avg(score) AS score FROM carmen_sandiego.high_scores group by id_players;'''
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def get_number_of_countries():
    sql = '''SELECT count(country_name) FROM carmen_sandiego.countries'''
    cursor.execute(sql)
    res = cursor.fetchall()[0][0]
    return res


def get_country_by_id(country_id):
    sql = '''SELECT * FROM carmen_sandiego.countries WHERE id_countries='%s' ''' %(country_id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def get_cities_by_countryid(country_id):
    sql = '''SELECT id_cities,city 
            FROM carmen_sandiego.cities,carmen_sandiego.countries
            WHERE country=country_name AND id_countries='%s' ''' % (country_id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def get_locations_by_city_name(city_name):
    sql = '''SELECT * FROM carmen_sandiego.locations WHERE city='%s' ''' % (city_name)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def get_locations_by_city_name_and_type(city_name,type):
    #Type= around/buy/diplomatic-representation/do/drink/eat/other/see/sleep/vicinity
    sql = '''SELECT * FROM carmen_sandiego.locations WHERE city='%s' AND type='%s' ''' % (city_name,type)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


def add_favorite_location(player_id,location_id):
    try:
        sql = "INSERT INTO carmen_sandiego.favorite_locations (id_players,id_locations) VALUES (%s,%s)"
        cursor.execute(sql, (player_id, location_id))
    except:
        pass
    return


def remove_favorite_location(player_id,location_id):
    try:
        sql = "DELETE FROM carmen_sandiego.favorite_locations WHERE id_players='%s' AND id_locations='%s'"
        cursor.execute(sql, (player_id, location_id))
    except:
        pass
    return


def get_location_by_id(location_id):
    sql = '''SELECT * FROM carmen_sandiego.locations WHERE id_locations='%s' ''' % (location_id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


create_connection()
close_connection()
