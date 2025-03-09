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
from datetime import date, datetime


class DatabaseController:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def search_library_database_by_title(self, title):
        query = "SELECT * FROM Catalog WHERE title LIKE ?"
        self.cursor.execute(query, ('%' + title + '%',))
        return self.cursor.fetchall()
    
    def fetch_user_info(self, id):
        query = "SELECT first_name, last_name, total_charge FROM User WHERE user_id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()
    
    def fetch_employee_info(self, id):
        query = "SELECT employee_name, salary FROM Employee WHERE employee_id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def insert_library_database(self, object_holder):
        self.cursor.execute(
            "INSERT INTO Catalog (item_type, title, publication_date, author_or_artist, publisher) VALUES(?, ?, ?, ?, ?)",
            (object_holder[0], object_holder[1], object_holder[2], object_holder[3], object_holder[4]))
        self.connection.commit()
        print("data inserted successfully.")

    def insert_user(self, obj_holder):
        self.cursor.execute(
            "INSERT INTO User (first_name, last_name, date_of_birth, address, phone_number, date_joined, "
            "total_charge) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (obj_holder)
        )
        self.connection.commit()
        print("User inserted successfully.")

    def insert_volunteer_employee(self, obj_holder, id):
        self.cursor.execute("SELECT first_name, last_name, date_of_birth, phone_number, address FROM User WHERE user_id = ?", (id,))
        results = self.cursor.fetchone()

        employee_name = results[0] + ' ' + results[1]
        self.cursor.execute(
            "INSERT INTO Employee (employee_name, employee_dob, phone_number, address, employement_date, salary)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (employee_name, results[2], results[3], results[4], obj_holder[0], obj_holder[1],)
        )
        self.connection.commit()
        print("Employee added successfully.")

    def validate_id(self, id, user):
        if user:
            query = "SELECT 1 FROM User WHERE user_id = ?"
        else:
            query = "SELECT 1 FROM Employee WHERE employee_id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone() is not None