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
        return self.fetch_item_availability(self.cursor.fetchall())

    def search_library_database_by_id(self, id):
        query = "SELECT * FROM Catalog WHERE item_id = ?"
        self.cursor.execute(query, (id,))
        return self.fetch_item_availability(self.cursor.fetchall())

    def search_by_author_name(self, author_name):
        query = "SELECT * FROM Catalog WHERE author_or_artist LIKE ?"
        self.cursor.execute(query, ('%' + author_name + '%',))
        return self.fetch_item_availability(self.cursor.fetchall())

    def search_by_title_and_author_name(self, title, author_name):
        query = "SELECT * FROM Catalog WHERE author_or_artist LIKE ? AND title LIKE ?"
        self.cursor.execute(query, ('%' + author_name + '%', '%' + title + '%'))
        return self.fetch_item_availability(self.cursor.fetchall())

    def search_by_item_type(self, item_type):
        query = "SELECT * FROM Catalog WHERE item_type = ?"
        self.cursor.execute(query, (item_type,))
        return self.fetch_item_availability(self.cursor.fetchall())

    def search_before_target_date(self, target_date):
        query = "SELECT * FROM Catalog WHERE publication_date <= ?"
        self.cursor.execute(query, (target_date,))
        return self.fetch_item_availability(self.cursor.fetchall())

    def search_after_target_date(self, target_date):
        query = "SELECT * FROM Catalog WHERE publication_date >= ?"
        self.cursor.execute(query, (target_date,))
        return self.fetch_item_availability(self.cursor.fetchall())
        
    def fetch_item_availability(self, items):
        results = []
        for item in items:
            query = "SELECT COUNT(*) FROM Record WHERE item_id = ? AND available = 1"
            self.cursor.execute(query, (item[0],))
            total = str(self.cursor.fetchone()[0]) + '/'
            query = "SELECT COUNT(*) FROM Record WHERE item_id = ?"
            self.cursor.execute(query, (item[0],))
            totalCopies = self.cursor.fetchone()[0]
            if totalCopies > 0:
                total += str(totalCopies)
            else:
                total = "Unavailable"
            item = item + (total,)
            results.append(item)
        return results
    
    def fetch_user_info(self, id):
        query = "SELECT first_name, last_name, total_charge FROM User WHERE user_id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def fetch_employee_info(self, id):
        query = "SELECT employee_name, salary FROM Employee WHERE employee_id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()
    
    def fetch_user_requests(self, id):
        query = "SELECT request_id, message, response FROM Request WHERE user_id = ?"
        self.cursor.execute(query, (id,))
        results = []
        for value in self.cursor.fetchall():
            results.append((value[0], value[1], (value[2] if value[2] is not None else "Pending")))
        return results
    
    def fetch_employee_requests(self):
        self.cursor.execute("SELECT request_id, message FROM Request WHERE response IS NULL")
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
