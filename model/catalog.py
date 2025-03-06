"""
Catalog class
catalog.py

Class Description: the class is a model for the items that a library database holds
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Catalog(db.Model):
    __tablename__ = 'Catalog'

    item_id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    author_or_artist = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.Text, nullable=False)

    def __init__(self, item_id, item_type, title,
                 publication_date, author_or_artist, publisher):
        self.item_id = item_id
        self.item_type = item_type
        self.title = title
        self.publication_date = publication_date
        self.author_or_artist = author_or_artist
        self.publisher = publisher





