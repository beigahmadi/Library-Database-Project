"""
EmployeeView class
employeeView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from users

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""


class EmployeeView:
    def __init__(self):
        pass

    @staticmethod
    def show_employee_interface(self):
        prom = input(
            "1. Sign up a new user to the library\n"
            "2. Find an item in library database\n"
            "3. Return a borrowed item\n"
            "4. Add an item to the library\n"
            "0. Exit\n"
        )

        if prom == "1":
            self.controller.insert_user()
