"""
EmployeeView class
employeeView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from users

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from datetime import datetime, date


class EmployeeView:

    def __init__ (self, id, controller):
        self.id = id
        self.controller = controller

    def user_insertion(self):
        first_name = input("Enter first name:\n ")
        last_name = input("Enter last name:\n ")
        dob_str = input("Enter date of birth (YYYY-MM-DD):\n ")
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format for date of birth. Please use YYYY-MM-DD.\n")
            return

        address = input("Enter address:\n ")
        phone_number = input("Enter phone number:\n ")
        date_joined_input = input("Enter date of account creation (YYYY-MM-DD) [leave blank for today]:\n ")
        if not date_joined_input:
            date_joined = date.today()
        else:
            try:
                date_joined = datetime.strptime(date_joined_input, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

        total_charge_input = input("Enter total charges due on account:\n ")
        try:
            total_charge = float(total_charge_input) if total_charge_input else 0.0
        except ValueError:
            print("Invalid total charge. Please enter a valid number.")
            return
        self.controller.insert_user(first_name, last_name, dob,
                               address, phone_number, date_joined, total_charge)
    
    def library_search(self):
        title = input("Please enter the title you prefer to search:\n")
        results = self.controller.search_library_database_by_title(title)
        print("Search results:", results)

    def item_return(self):
        pass

    def item_insertion(self):
        object_holder = []
        item = input("Please enter the item type:\n")
        object_holder.append(item)
        tit = input("Please enter the item title:\n")
        object_holder.append(tit)
        pub_date = input("Please enter the publication date (YYYY-MM-DD):\n")
        try:
            pub_date = datetime.strptime(pub_date, "%Y-%m-%d").date()
            object_holder.append(pub_date)
        except ValueError:
            print("Invalid date format for date of publication. Please use YYYY-MM-DD.")
            return
        art_name = input("Please enter the artist name:\n")
        object_holder.append(art_name)
        pub_name = input("Please enter the name of the publisher:\n")
        object_holder.append(pub_name)
        self.controller.insert_library_database(object_holder)


    def show_employee_interface(self, controller):
        input_table = {
            '1' : self.user_insertion,
            '2' : self.library_search,
            '3' : self.item_return,
            '4' : self.item_insertion,
            '0' : lambda: (print("Exiting..."), exit(0)[-1])
        }

        while True:
            prompt = input(
                "\n\n1. Sign up a new user to the library\n"
                "2. Find an item in library database\n"
                "3. Return a borrowed item\n"
                "4. Add an item to the library\n"
                "0. Exit\n\n"
            )
            action = input_table.get(prompt, lambda: print("Invalid input, please try again.\n"))
            action()
