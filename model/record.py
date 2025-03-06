"""
Record class
record.py

Class Description: keeps the record of the item
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Record(db.Model):
    __tablename__ = 'Record'

    record_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False, foreign_key=True)
    status = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=False)

    def __init__(self, item_id, status, notes):
        self.item_id = item_id
        self.status = status
        self.notes = notes
