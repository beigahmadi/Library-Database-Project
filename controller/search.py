"""
SearchController class
search.py

Class Description: a class professionally searches the db
Class Invariant: is a super class of DatabaseController

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
import sqlite3


class SearchController:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def search_library_database_by_title(self, title):
        query = "SELECT * FROM Catalog WHERE title LIKE ?"
        self.cursor.execute(query, ('%' + title + '%',))

        results = []
        for tuple in self.cursor.fetchall():
            query = "SELECT COUNT(*) FROM Record WHERE item_id = ? AND available = True"
            self.cursor.execute(query, (tuple[0],))
            total = str(self.cursor.fetchone()[0]) + '/'
            query = "SELECT COUNT(*) FROM Record WHERE item_id = ?"
            self.cursor.execute(query, (tuple[0],))
            total += str(self.cursor.fetchone()[0])
            tuple = tuple + (total,)
            results.append(tuple)
        return results

    def search_library_database_by_id(self, id):
        query = "SELECT * FROM Catalog WHERE item_id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def search_by_author_name(self, author_name):
        query = "SELECT * FROM Catalog WHERE author_or_artist LIKE ?"
        self.cursor.execute(query, ('%' + author_name + '%',))
        return self.cursor.fetchall()

    def search_by_title_and_author_name(self, title, author_name):
        query = "SELECT * FROM Catalog WHERE author_or_artist LIKE ? AND title LIKE ?"
        self.cursor.execute(query, ('%' + author_name + '%', '%' + title + '%'))
        return self.cursor.fetchall()

    def search_by_item_type(self, item_type):
        query = "SELECT * FROM Catalog WHERE item_type = ?"
        self.cursor.execute(query, (item_type,))
        return self.cursor.fetchall()

    def search_before_target_date(self, target_date):
        query = "SELECT * FROM Catalog WHERE publication_date <= ?"
        self.cursor.execute(query, (target_date,))
        return self.cursor.fetchall()

    def search_after_target_date(self, target_date):
        query = "SELECT * FROM Catalog WHERE publication_date >= ?"
        self.cursor.execute(query, (target_date,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
