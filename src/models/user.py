from flask_login import UserMixin

class user(UserMixin):
    def __init__(self, username):
        self.id = username