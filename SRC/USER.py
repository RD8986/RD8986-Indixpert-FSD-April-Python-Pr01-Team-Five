import json

class User:
    def __init__(self, first_name, last_name, username, password, role):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }
