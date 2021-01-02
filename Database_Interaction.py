import csv
import hashlib
import os
from datetime import date, datetime

import mysql.connector
from mysql.connector import Error

from Dataset_Parsing import help_create_cities, create_cities, create_comments, create_questions, create_locations

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


def commit_connection():
    global connection
    connection.commit()

def close_connection():
    global connection
    connection.close()

def fill_countries():
    global cursor

    with open('parsed_csvs/countries.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.countries (country_name,capital_name,population,currency,languages,flag,region,area,gdp,climate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for row in reader:
            row[2] = int(row[2].replace(',', ''))
            row[4] = row[4].split(',')[0]
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
    commit_connection()


def fill_cities():
    global cursor
    # query = "LOAD DATA INFILE 'cities.csv' INTO TABLE carmen_sandiego.cities"
    # cursor.execute(query)

    with open('parsed_csvs/cities.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.cities (city, id_country) VALUES (%s,%s)"
        for row in reader:
            cursor.execute(sql, row)
    commit_connection()


def fill_comments():
    global cursor

    with open('parsed_csvs/comments.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.comments (comment_type, description) VALUES (%s,%s)"
        for row in reader:
            cursor.execute(sql, row)
    commit_connection()


def fill_questions():
    global cursor

    with open('parsed_csvs/questions.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.questions (question_type, description) VALUES (%s,%s)"
        for row in reader:
            cursor.execute(sql, row)
    commit_connection()


def fill_locations():
    global cursor
    with open('parsed_csvs/locations.csv', encoding='cp850') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        sql = "INSERT INTO carmen_sandiego.locations (location_name, type, cityid ,url,description) VALUES (%s,%s,%s,%s,%s)"
        for row in reader:
            cursor.execute(sql, row)
    commit_connection()


def fill_all():
    create_connection()
    fill_countries()
    fill_cities()
    fill_comments()
    fill_questions()
    commit_connection()


# Gets Player By ID
def get_player_by_id(id):
    sql = "SELECT * FROM carmen_sandiego.players WHERE id_players='%s'" % (id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# Adds player to DB
def add_player(user):
    # (username,password,first_name,last_name)
    try:
        sql = "SELECT * FROM carmen_sandiego.players WHERE user_name='%s'" % (user[0])
        cursor.execute(sql)
        res = cursor.fetchall()
        if (len(res) > 0):
            return -1
        salt = str(os.urandom(32))
        password = user[1]
        hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
        last_played = datetime.today().date()

        sql = "INSERT INTO carmen_sandiego.players (user_name,password,salt,first_name,last_name,last_played) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (user[0], hash, salt, user[2], user[3], last_played))
        commit_connection()
        return 0

    except:
        return -2


# Returns PlayerID if username and password exist in DB, -1 otherwise
def log_in(username, password):
    sql = "SELECT * FROM carmen_sandiego.players WHERE user_name='%s'" % (username)
    cursor.execute(sql)
    res = cursor.fetchall()[0]

    salt = res[3]
    hash = res[2]
    if (hashlib.sha256((password + salt).encode('utf-8')).hexdigest() == hash):
        return res[0]
    return -1

def update_last_played(id):
    sql = "UPDATE carmen_sandiego.players SET last_played = '%s' WHERE id_players='%s'" % (
        datetime.now(), id)
    cursor.execute(sql)
    commit_connection()


# # Adds friendship to DB
# def add_friendship_by_id(id1, id2):
#     sql = "INSERT INTO carmen_sandiego.friendships (id_friendships_a,id_friendships_b) VALUES (%s,%s)"
#
#     try:
#         if (id1 < id2):
#             cursor.execute(sql, (id1, id2))
#             commit_connection()
#         else:
#             cursor.execute(sql, (id2, id1))
#             commit_connection()
#     except:
#         print("Friendship exists already ")

def add_friendship_by_username(id,username):
    try:
        sql = '''Insert into friendships (id_friendships_a,id_friendships_b) values((SELECT min(id_players) FROM carmen_sandiego.players WHERE (id_players='%s' or user_name='%s')),
                (SELECT max(id_players) FROM carmen_sandiego.players WHERE (id_players='%s' or user_name='%s')))''' % (id, username, id,username)
        cursor.execute(sql)
        commit_connection()
    except:
        print("Friendship exists already ")

# def remove_friendship(id1, id2):
#     sql = "DELETE FROM carmen_sandiego.friendships WHERE id_friendships_a='%s' AND id_friendships_b='%s'"
#     try:
#         if (id1 < id2):
#             cursor.execute(sql, (id1, id2))
#             commit_connection()
#             return 1
#         else:
#             cursor.execute(sql, (id2, id1))
#             commit_connection()
#             return 1
#     except:
#         print("Error Deleting friendship")
#         return -1

def remove_friendship_by_username(id,username):
    try:
        sql = '''Delete from friendships where(id_friendships_a = (SELECT min(id_players) FROM carmen_sandiego.players WHERE (id_players='%s' or user_name='%s')) and id_friendships_b =
                (SELECT max(id_players) FROM carmen_sandiego.players WHERE (id_players='%s' or user_name='%s')))''' % (id, username, id,username)
        cursor.execute(sql)
        commit_connection()
    except:
        print("Error Deleting friendship ")
# Returns the ids of players who are friends with id

def get_all_friendships_by_id(id):
    sql = '''Select user_name from players where ((id_players in (select id_friendships_a FROM carmen_sandiego.friendships
     WHERE id_friendships_b='%s')) or (id_players in (select id_friendships_b FROM carmen_sandiego.friendships 
     WHERE id_friendships_a='%s')))''' % (id,id)
    cursor.execute(sql)
    res = cursor.fetchall()
    for count,value in enumerate(res):
        res[count]=res[count][0]
    return res


# Updates DB with new high_score
def update_highscore_table(id, score):
    # sql = "SELECT * FROM carmen_sandiego.high_scores WHERE id_players='%s' and score='%s'" % (id, score)
    # cursor.execute(sql)
    # res = cursor.fetchall()
    #
    # if len(res) == 0:
    #     sql = "INSERT INTO carmen_sandiego.high_scores (id_players,score,date) VALUES (%s,%s,%s)"
    #     cursor.execute(sql, (id, score, datetime.now()))
    #
    # else:
    #     sql = "UPDATE carmen_sandiego.high_scores SET date ='%s' WHERE id_players = '%s' and score='%s'" % (
    #         datetime.now(), id, score)
    #     cursor.execute(sql)
    sql = "INSERT INTO carmen_sandiego.high_scores (id_players,score,date) VALUES (%s,%s,%s)"
    cursor.execute(sql, (id, score, datetime.now()))
    commit_connection()


# # Gets HighScores (No Repeats)
# def get_highscores_no_repeats():
#     sql = "SELECT id_players,max(score) AS score FROM carmen_sandiego.high_scores GROUP BY id_players;"
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     return res


# Gets HighScores (Yes Repeats)
def get_highscores_yes_repeats():
    sql = '''SELECT first_name,last_name,score AS score FROM carmen_sandiego.high_scores ,carmen_sandiego.players 
            WHERE high_scores.id_players=players.id_players order by score DESC limit 10'''
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# Gets HighScores (No Repeats - Friends Only)
def get_highscores_no_repeats_friends(id):
    sql = '''SELECT first_name,last_name,max(score) AS score FROM carmen_sandiego.high_scores ,carmen_sandiego.players
             WHERE ((high_scores.id_players in (SELECT id_friendships_a FROM friendships WHERE id_friendships_b='%s') or
		     high_scores.id_players in (SELECT id_friendships_b FROM friendships WHERE id_friendships_a='%s' ) or
		      high_scores.id_players = '%s')) and players.id_players=high_scores.id_players group by high_scores.id_players order by score DESC limit 10''' % (id, id, id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# # Gets Average Score for each player
# def get_highscores_avg_scores():
#     sql = '''SELECT id_players,avg(score) AS score FROM carmen_sandiego.high_scores group by id_players;'''
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     return res


def get_number_of_countries():
    sql = '''SELECT count(country_name) FROM carmen_sandiego.countries'''
    cursor.execute(sql)
    res = cursor.fetchall()[0][0]
    return res


def get_country_by_id(country_id):
    try:
        sql = '''SELECT * FROM carmen_sandiego.countries WHERE id_countries='%s' ''' % (country_id)
        cursor.execute(sql)
        res = cursor.fetchall()[0]
    except Exception:
        res=None
    return res


# def get_cities_by_countryid(country_id):
#     sql = '''SELECT id_cities,city
#             FROM carmen_sandiego.cities,carmen_sandiego.countries
#             WHERE country=country_name AND id_countries='%s' ''' % (country_id)
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     return res


def get_locations_by_city_id(city_id):
    sql = '''SELECT * FROM carmen_sandiego.locations WHERE cityid='%s' ''' % (city_id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


# def get_locations_by_city_name_and_type(city_name, type):
#     # Type= around/buy/diplomatic-representation/do/drink/eat/other/see/sleep/vicinity
#     sql = '''SELECT * FROM carmen_sandiego.locations WHERE city='%s' AND type='%s' ''' % (city_name, type)
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     return res


def add_favorite_location(player_id, location_id):
    try:
        sql = "INSERT INTO carmen_sandiego.favorite_locations (id_players,id_locations) VALUES (%s,%s)"
        cursor.execute(sql, (player_id, location_id))
        commit_connection()
    except:
        pass
    return


def remove_favorite_location(player_id, location_id):
    try:
        sql = "DELETE FROM carmen_sandiego.favorite_locations WHERE id_players='%s' AND id_locations='%s'"
        cursor.execute(sql, (player_id, location_id))
        commit_connection()
    except:
        pass
    return


# def get_location_by_id(location_id):
#     sql = '''SELECT * FROM carmen_sandiego.locations WHERE id_locations='%s' ''' % (location_id)
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     return res

def get_questions_by_type(type):
    sql = '''SELECT description FROM carmen_sandiego.questions WHERE question_type='%s' ''' % (type)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res

# def get_comments_by_type(type):
#     sql = '''SELECT * FROM carmen_sandiego.comments WHERE comment_type='%s' ''' % (type)
#     cursor.execute(sql)
#     res = cursor.fetchall()
#     return res

def get_cities_by_country_id(id):
    sql = '''SELECT id_cities,city FROM carmen_sandiego.cities Where id_country='%s'; ''' % (id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res

def get_favorite_locations_by_user_id(id):
    sql = '''Select * from locations where id_locations in (SELECT id_locations FROM carmen_sandiego.favorite_locations where id_players='%s') ''' % (id)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res