"""
LibraryCatalog class
libraryCatalog.py

Class Description:
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LibraryCatalog(db.Model):
    __tablename__ = 'libraryCatalog'

