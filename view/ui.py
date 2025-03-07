"""
UI class
ui.py

Class Description: it shows the UI for the db
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from view.employeeView.employeeView import EmployeeView
from view.userView.userView import UserView


class UI:
    def __init__(self, controller):
        self.controller = controller

    def print_ui(self):
        while prompt is not "0":
            prompt = input(
                "Select among the following items:\n"
                "1. User Login\n"
                "2. Employee Login\n"
                "0. Exit\n"
            )
            if prompt is "1":
                EmployeeView.show_employee_interface(self)
            elif prompt is "2":
                UserView.show_user_interface(self)
            elif prompt is "0":
                exit(0)
