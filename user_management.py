import json

def register_user(username, password):
    try:
        with open('users.json', 'r+') as file:
            users = json.load(file)
            if username in users:
                return False  # Username already exists
            users[username] = password
            file.seek(0)
            json.dump(users, file)
            return True
    except FileNotFoundError:
        with open('users.json', 'w') as file:
            json.dump({username: password}, file)
            return True

def login_user(username, password):
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
            if username in users and users[username] == password:
                return True
            return False
    except FileNotFoundError:
        return False

# Example usage
# register_user('newuser', 'password123')
# login_user('newuser', 'password123')
