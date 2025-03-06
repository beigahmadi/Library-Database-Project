"""
Loan class
loan.py

Class Description: the model create simulation of loaning from db of a library
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Loan(db.Model):
    __tablename__ = 'Loan'
    loan_id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer, nullable=False, foreign_key=True)
    user_id = db.Column(db.Integer, nullable=False, foreign_key=True)
    loan_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=False)
    fine_charged = db.Column(db.Integer, nullable=False)

    def __init__(self, loan_id, record_id, user_id,
                 loan_date, due_date, return_date, fine_charged):
        self.loan_id = loan_id
        self.record_id = record_id
        self.user_id = user_id
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine_charged = fine_charged
