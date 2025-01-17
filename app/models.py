from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    # posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username=username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     item = db.Column(db.String(150), nullable=False, unique=True)
#     price = db.Column(db.Numeric(6,2), nullable=False, unique=True) 

#     def __init__(self, item, total):
#         self.item=item
#         self.total=total




# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title= db.Column(db.String(200))
#     content = db.Column(db.String(300))
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self, title, content, user_id):
#         self.title = title
#         self.content = content
#         self.user_id = user_id


# class Phonebook(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(150))
#     last_name =  db.Column(db.String(150))
#     phone_number = db.Column(db.String(150))
#     address = db.Column(db.String(300))

#     def __init__(self, first_name, last_name, phone_number, address):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone_number = phone_number
#         self.address = address

        