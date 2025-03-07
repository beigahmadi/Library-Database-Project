"""
UserView class
userView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from Employee

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""


class UserView:
    def __init__(self):
        pass

    @staticmethod
    def show_user_interface(self):
        comm = input(
            "1. Find an item in the library\n"
            "2. Borrow an item from the library\n"
            "3. Register for an event in the library\n "
            "4. Volunteer for the library\n"
            "5. Ask for help from a librarian\n"
            "0. Exit\n"
        )
