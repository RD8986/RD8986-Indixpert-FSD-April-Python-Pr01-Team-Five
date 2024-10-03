import json

# File to store users' data
USER_FILE = 'users.json'

def load_users():
    try:
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Sign Up
def signup(username, password, role):
    users = load_users()
    if username in users:
        return "Username already exists."
    
    users[username] = {'password': password, 'role': role}
    save_users(users)
    return "User signed up successfully!"

# Login
def login(username, password):
    users = load_users()
    if username in users and users[username]['password'] == password:
        return users[username]['role']
    return None