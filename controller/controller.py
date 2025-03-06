"""
DatabaseController class
DatabaseController.py
 
Class Description: a class controls the connection between 
library model and library database
Class Invariant:
 
Author(s): Mahdi Beigahmadi, Cole Scott Robertson 
Last modified: March. 2025
"""
import sqlite3

class DatabaseController:
    def __init__(self, db_path):
      self.connection = sqlite3.connect(db_path)
      self.cursor = self.connection.cursor()

    def search_library_database_by_title(self, title):
        pass
