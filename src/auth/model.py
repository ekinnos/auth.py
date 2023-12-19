# model.py | Auth.py

class UserModel:
    def __init__(self, username, role, password):
        self.username = username
        self.password = password
        self.role = role