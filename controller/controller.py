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
from datetime import date, timedelta

from controller.search import SearchController


class DatabaseController(SearchController):
    def __init__(self, db_path):
        super().__init__(db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def fetch_library_loans(self, id):
        self.cursor.execute(
            "SELECT loan_id, record_id, julianday(due_date) - julianday(loan_date) AS date_diff FROM Loan WHERE user_id = ?",
            (id,)
        )
        results = []
        for tuple in self.cursor.fetchall():
            self.cursor.execute(
                "SELECT C.item_id, C.item_type, C.title FROM Catalog C JOIN Record R ON C.item_id = R.item_id WHERE R.record_id = ?",
                (tuple[1],)
            )
            item = self.cursor.fetchone()
            result = (tuple[0], item[0], item[1], item[2], tuple[2])
            results.append(result)

        return results

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
        print("Data inserted successfully.")

    def insert_library_record(self, id):
        self.cursor.execute(
            "INSERT INTO Record (item_id, available) VALUES (?, ?)",
            (id, True)
        )
        self.connection.commit()
        print("Record inserted successfully.")

    def insert_user(self, obj_holder):
        self.cursor.execute(
            "INSERT INTO User (first_name, last_name, date_of_birth, address, phone_number, date_joined, "
            "total_charge) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (obj_holder)
        )
        self.connection.commit()
        print("User inserted successfully.")

    def insert_volunteer_employee(self, obj_holder, id):
        self.cursor.execute(
            "SELECT first_name, last_name, date_of_birth, phone_number, address FROM User WHERE user_id = ?", (id,))
        results = self.cursor.fetchone()

        employee_name = results[0] + ' ' + results[1]
        self.cursor.execute(
            "INSERT INTO Employee (employee_name, employee_dob, phone_number, address, employement_date, salary)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (employee_name, results[2], results[3], results[4], obj_holder[0], obj_holder[1],)
        )
        self.connection.commit()
        print("Employee added successfully.")

    def borrow_library_record(self, user_id, item_id):
        self.cursor.execute("SELECT record_id FROM Record WHERE item_id = ? AND available = True", (item_id,))
        record_id = self.cursor.fetchone()[0]

        if record_id:
            self.cursor.execute("UPDATE Record SET available = False WHERE record_id = ?", (record_id,))
            self.connection.commit()

            self.cursor.execute(
                "INSERT INTO Loan (record_id, user_id, loan_date, due_date) VALUES (?, ?, ?, ?)",
                (record_id, user_id, str(date.today()), str(date.today() + timedelta(days=21)))
            )
            self.connection.commit()
            print("Item borrowed successfully.")
        else:
            print("No copies available.")

    def validate_id(self, id, user):
        if user:
            query = "SELECT 1 FROM User WHERE user_id = ?"
        else:
            query = "SELECT 1 FROM Employee WHERE employee_id = ?"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone() is not None
