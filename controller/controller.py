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
        query = "SELECT * FROM Catalog WHERE title = ?"
        self.cursor.execute(query, (title,))
        results = self.cursor.fetchall()
        return results

    def insert_library_database(self, object_holder):
        self.cursor.execute(
            "INSERT INTO Catalog (item_type, title, publication_date, author_or_artist, publisher) VALUES(?, ?, ?, ?, ?)",
            (object_holder[0], object_holder[1], object_holder[2], object_holder[3], object_holder[4]))
        self.connection.commit()
        print("data inserted successfully.")

    def insert_user(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        dob_str = input("Enter date of birth (YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format for date of birth. Please use YYYY-MM-DD.")
            return

        address = input("Enter address: ")
        phone_number = input("Enter phone number: ")
        date_joined_input = input("Enter date of account creation (YYYY-MM-DD) [leave blank for today]: ")
        if not date_joined_input:
            date_joined = date.today()
        else:
            try:
                date_joined = datetime.strptime(date_joined_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

        total_charge_input = input("Enter total charges due on account: ")
        try:
            total_charge = float(total_charge_input) if total_charge_input else 0.0
        except ValueError:
            print("Invalid total charge. Please enter a valid number.")
            return

        self.cursor.execute(
            "INSERT INTO User (first_name, last_name, date_of_birth, address, phone_number, date_joined, "
            "total_charge) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (first_name, last_name, dob, address, phone_number, date_joined, total_charge)
        )
        self.connection.commit()
        print("User inserted successfully.")

    def insert_volunteer_employee(self , emp_obj_holder):
        self.cursor.execute(
            "INSERT INTO Employee (employee_name, employee_dob, phone_number, address, employement_date, salary)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (emp_obj_holder[0], emp_obj_holder[1],
             emp_obj_holder[2], emp_obj_holder[3], emp_obj_holder[4], emp_obj_holder[5])
        )
        self.connection.commit()
        print("Employee added successfully.")