import json
import os
from SRC.USER import User
from SRC.COLORS import Colors

USERS_FILE = os.path.join('database', 'users.json')

class AuthenticationSystem:
    def __init__(self):
        self.users = self.load_users()
        self.admin_username = self.find_admin()

    def load_users(self):
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as file:
                return json.load(file)
        return {}

    def save_users(self):
        # Ensure the database directory exists
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)  # Create the directory if it doesn't exist
        with open(USERS_FILE, "w") as file:
            json.dump(self.users, file, indent=4)


    def find_admin(self):
        for username, user_data in self.users.items():
            if user_data["role"] == "Admin":
                return username
        return None

    def signup(self, first_name, last_name, username, password, role):
        if role == 'Admin':
            if self.admin_username:
                print(Colors.FAIL + "Admin already exists. Only one admin can be registered." + Colors.ENDC)
                return

        if username in self.users:
            print(Colors.FAIL + "Username already exists. Please choose another username." + Colors.ENDC)
            return
        elif len(password) < 7:
            print(Colors.FAIL + "Password must be at least 7 characters long." + Colors.ENDC)
            return
        else:
            user = User(first_name, last_name, username, password, role)
            self.users[username] = user.to_dict()
            self.save_users()
            print(Colors.OKGREEN + f"User {first_name} {last_name} ({role}) signed up successfully!" + Colors.ENDC)

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            user_data = self.users[username]
            print(Colors.OKGREEN + f"Login successful! Welcome, {user_data['first_name']} {user_data['last_name']}!" + Colors.ENDC)
            return User(**user_data)
        else:
            print(Colors.FAIL + "Invalid username or password." + Colors.ENDC)
            return None

    def count_normal_users(self):
        return sum(1 for user in self.users.values() if user['role'] == 'User')
