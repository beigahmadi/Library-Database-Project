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
      pass
   
   def insert_user(self):
      first_name = input("Enter first name: ")
      last_name = input("Enter last name: ")
      #add input validation for dob
      dob = input("Enter date of birth (YYYY-MM-DD): ")
      address = input("Enter address: ")
      phone_number = input("Enter phone number: ")
      date_joined = input("Enter date of account creation (YYYY-MM-DD): ")
      if not date_joined:
         date_joined = date.today()
      else:
         try:
            date_joined = datetime.strptime(date_joined, "%Y-%m-%d").date()
         except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

      total_charge = input("Enter total charges due on account: ")
      if not total_charge:
         total_charge = 0.0

      self.cursor.execute("INSERT INTO User (first_name, last_name, date_of_birth, address, phone_number, date_joined, total_charge) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (first_name, last_name, dob, address, phone_number, date_joined, total_charge))
      self.connection.commit()
       

       


