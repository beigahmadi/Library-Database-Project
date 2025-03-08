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
        prompt = ""
        while prompt != "0":
            prompt = input(
                "\n\nSelect among the following items:\n"
                "1. User Login\n"
                "2. Employee Login\n"
                "0. Exit\n\n"
            )

            if prompt == "1":
                UserView.show_user_interface(self.controller)
            elif prompt == "2":
                EmployeeView.show_employee_interface(self.controller)
            elif prompt == "0":
                print("Exiting...")
                exit(0)
            else:
                print("Invalid input, please try again.\n")
