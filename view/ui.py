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
        

    def user_login(self):
        id = input("Please enter your User ID: ")
        print("Hello world.")

    def employee_login(self):
        id = input("Please enter your Employee ID: ")
        UserView.show_user_interface(self.controller)


    def print_ui(self):
        input_table = {
        '1' : self.user_login,
        '2' : self.employee_login,
        '0' : lambda: (print("Exiting..."), exit(0)[-1])
        }
        while True:
            prompt = input(
                "\n\nSelect among the following items:\n"
                "1. User Login\n"
                "2. Employee Login\n"
                "0. Exit\n\n"
            )
            action = input_table.get(prompt, lambda: print("Invalid input, please try again.\n"))
            action()
    
    
