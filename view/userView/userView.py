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
        title = input("Please enter the title of the item you are searching for: ")
        results = self.controller.search_library_database_by_title(title)
        print("Search results (ID, Type, Name, Publication Date, Author/Artist, Publisher, Available/Total Copies):")
        for tuple in results:
            print(tuple)

    def library_borrow(self):
        while True:
            item_id = input("Please input the ID of the item you wish to borrow: ")
            if self.controller.search_library_database_by_id(item_id) is not None:
                break
            print("Invalid ID. Please enter a valid item ID.")
        self.controller.borrow_library_record(self.id, item_id)

    def event_register(self):
        pass

    def register_for_volunteer(self):
        obj_holder = []
        obj_holder.append(str(date.today()))

        obj_holder.append(0.0)
        self.controller.insert_volunteer_employee(obj_holder, self.id)

    def request_help(self):
        pass

    def fetch_loans(self):
        print("Loan ID, Item ID, Type, Name, Days Remaining")
        for tuple in self.controller.fetch_library_loans(self.id):
            print(tuple)

    def show_user_interface(self):
        user_info = self.controller.fetch_user_info(self.id)
        print("Welcome user", user_info[0] + ' ' + user_info[1], "\nYou currently have $", user_info[2], "in outstanding charges.")
        input_table = {
            '1' : self.library_search,
            '2' : self.library_borrow,
            '3' : self.event_register,
            '4' : self.register_for_volunteer,
            '5' : self.request_help,
            '6' : self.fetch_loans,
            '0' : lambda: (print("Exiting..."), exit(0)[-1])
        }

        while True:
            prompt = input(
                "\n1. Find an item in the library\n"
                "2. Borrow an item from the library\n"
                "3. Register for an event in the library\n"
                "4. Volunteer for the library\n"
                "5. Ask for help from a librarian\n"
                "6. View existing library loans\n"
                "0. Exit\n\n"
            )
            action = input_table.get(prompt, lambda: print("Invalid input, please try again."))
            action()

    
