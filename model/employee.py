"""
Employee class
employee.py

Class Description: the staff of the library
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    __tablename__ = 'Employee'

    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_name = db.Column(db.Text, nullable=False)
    empmloyee_dob = db.Column(db.Text, nullable=False)
    employee_number = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    employment_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Double, nullable=False)

    def __init__(self, employee_name, employee_dob, employee_number, address, employment_date, salary):
        self.employee_name = employee_name
        self.employee_dob = employee_dob
        self.employee_number = employee_number
        self.address = address
        self.employment_date = employment_date
        self.salary = salary
