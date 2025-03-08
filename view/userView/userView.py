"""
UserView class
userView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from Employee

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from datetime import date, datetime

from view.employeeView.employeeView import EmployeeView


class UserView:

    @staticmethod
    def register_for_volunteer(controller):
        emp_obj_holder = []
        emp_name = input("Please enter your full name:\n")
        emp_obj_holder.append(emp_name)
        dob_input = input("Enter your date of birth (YYYY-MM-DD):\n")
        if not dob_input:
            dob_input = date.today()
        else:
            try:
                dob_input = datetime.strptime(dob_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
        emp_obj_holder.append(dob_input)
        emp_phone = input("Please enter your phone number:\n")
        emp_obj_holder.append(emp_phone)
        emp_address = input("Please enter your address:\n")
        emp_obj_holder.append(emp_address)
        date_joined_input = input("Enter date of account creation (YYYY-MM-DD) [leave blank for today]: ")
        if not date_joined_input:
            date_joined = date.today()
            emp_obj_holder.append(date_joined)
        else:
            try:
                date_joined = datetime.strptime(date_joined_input, "%Y-%m-%d").date()
                emp_obj_holder.append(date_joined)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
        emp_obj_holder.append(0.0)
        controller.insert_volunteer_employee(emp_obj_holder)

    @staticmethod
    def show_user_interface(controller):
        comm = input(
            "\n\n1. Find an item in the library\n"
            "2. Borrow an item from the library\n"
            "3. Register for an event in the library\n"
            "4. Volunteer for the library\n"
            "5. Ask for help from a librarian\n"
            "0. Exit\n\n"
        )
        if comm == "1":
            EmployeeView.get_data_for_insertion(controller)
        if comm == "2":
            pass
        if comm == "3":
            pass
        if comm == "4":
            UserView.register_for_volunteer(controller)
        if comm == "5":
            pass
        if comm == "0":
            print("Exiting user interface...")
        UserView.show_user_interface(controller)
