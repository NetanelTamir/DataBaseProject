import Database_Interaction


def add_player(user_name, password, first_name, last_name):
    if len(first_name) < 2 or len(first_name) > 20:
        return -1, "first name must contain at least 2 characters and at most 20 characters!"
    if len(last_name) < 2 or len(last_name) > 20:
        return -1, "Last name must contain at least 2 characters and at most 20 characters!"
    if len(user_name) < 2 or len(user_name) > 20:
        return -1, "User name must contain at least 2 characters and at most 20 characters!"
    if len(password) < 2 or len(password) > 20:
        return -1, "password must contain at least 2 characters and at most 20 characters!"

    response = Database_Interaction.add_player((user_name, password, first_name, last_name))
    if response == -1:
        return -1, "user-name already exist"
    if response == -2:
        return -1, "sign up failed"
    if response == 0:
        return 0, "welcome " + first_name + " " + last_name


def log_in(user_name, password):
    if len(user_name) == 0 or len(password) == 0:
        return -1, "missing username and/or password!"
    id = Database_Interaction.log_in(user_name, password)
    if id <= -1:
        return -1, "Authentication failed"
    player = Database_Interaction.get_player_by_id(id)[0]
    if not player:
        return -1, "Authentication failed"
    return id, player


def remove_favorite_location(player_id, current_LocationId):
    if (current_LocationId == -1):
        return -1
    Database_Interaction.remove_favorite_location(player_id, current_LocationId)
    return 1


def remove_friend(player, friend_to_remove):
    if not player or not friend_to_remove:
        return -1, "Choose a friend to remove"
    Database_Interaction.remove_friendship_by_username(player, friend_to_remove)
    return 1, "Good"


def add_friend(player_id, player_name, friend_to_add):
    if not player_id or not friend_to_add:
        return -1, "Choose a friend to add"
    if player_name == friend_to_add:
        return -2, "Can't add yourself as a friend"
    result = Database_Interaction.add_friendship_by_username(player_id, friend_to_add)
    if result == -1:
        return -2, "Friendship already exists"
    if result == -2:
        return -2, "There is no such user"
    return 1, "GOOD"
