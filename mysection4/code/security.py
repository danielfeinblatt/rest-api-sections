from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'Bob', 'asdf')
]

username_mapping = { u.username: u for u in users}
userid_mapping = { u.id : u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None) # default value is None if the key does not exist

    if user and safe_str_cmp(user.password, password): # safer way of comparing strings
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
