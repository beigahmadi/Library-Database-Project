"""
UserView class
userView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from Employee

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from datetime import date, datetime


class UserView:

    def __init__ (self, id, controller):
        self.id = id
        self.controller = controller
    
    def library_search(self):
        title = input("Please enter the title you prefer to search:\n")
        results = self.controller.search_library_database_by_title(title)
        print("Search results:", results)

    def library_borrow(self):
        pass

    def event_register(self):
        pass

    def register_for_volunteer(self):
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
        self.controller.insert_volunteer_employee(emp_obj_holder)

    def request_help():
        pass

    def show_user_interface(self):
        input_table = {
            '1' : self.library_search,
            '2' : self.library_borrow,
            '3' : self.event_register,
            '4' : self.register_for_volunteer,
            '5' : self.request_help,
            '0' : lambda: (print("Exiting..."), exit(0)[-1])
        }

        while True:
            prompt = input(
                "\n\n1. Find an item in the library\n"
                "2. Borrow an item from the library\n"
                "3. Register for an event in the library\n"
                "4. Volunteer for the library\n"
                "5. Ask for help from a librarian\n"
                "0. Exit\n\n"
            )
            action = input_table.get(prompt, lambda: print("Invalid input, please try again.\n"))
            action()

    
