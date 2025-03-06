"""
Event class
event.py

Class Description: creates events and manges the event are being held at the library
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = 'Event'
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.Text, nullable=False)
    event_type = db.Column(db.Text, nullable=False)
    event_location = db.Column(db.Text, nullable=False)
    event_range = db.Column(db.Text, nullable=False)
    event_time = db.Column(db.Date, nullable=False)


def __init__(self, event_name, event_type, event_location, event_range, event_time):
    self.event_name = event_name
    self.event_type = event_type
    self.event_location = event_location
    self.event_range = event_range
    self.event_time = event_time
