"""
User class
user.py

Class Description: this model is a user which interacts with the library
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    date_joined = db.Column(db.Date, nullable=False)
    total_charge = db.Column(db.Integer, nullable=False)

    def __init__(self, first_name, last_name,
                 date_of_birth, address, phone_number, date_joined):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.date_joined = date_joined
        self.total_charge = 0
