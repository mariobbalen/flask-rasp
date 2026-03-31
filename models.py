from flask_login import UserMixin

user_db = {}

class User(UserMixin):
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
    @staticmethod
    def create_user(email, password):
        new_user = User(email, email, password)
        user_db[email] = new_user
        return new_user