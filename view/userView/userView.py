"""
UserView class
userView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from Employee

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
import csv
from datetime import date


class UserView:

    def __init__ (self, id, controller):
        self.id = id
        self.controller = controller

    def library_search(self):
        search_menu = (
            "Please choose the search option among the following:\n"
            "1. Search by title\n"
            "2. Search by author\n"
            "3. Search by item type\n"
            "4. Search before a specific date\n"
            "5. Search after a specific date\n"
            "6. Back to main menu\n"
        )

        while True:
            choice = input(search_menu).strip()
            if choice == '1':
                title = input("Enter the title of the item: ").strip()
                results = self.controller.search_library_database_by_title(title)
                break
            elif choice == '2':
                author = input("Enter the author of the item: ").strip()
                results = self.controller.search_by_author_name(author)
                break
            elif choice == '3':
                item_type = input("Enter the item type (e.g., Book, DVD): ").strip()
                results = self.controller.search_by_item_type(item_type)
                break
            elif choice == '4':
                target_date = input("Enter the target date (e.g., 1990-12-01): ").strip()
                results = self.controller.search_before_target_date(target_date)
                break
            elif choice == '5':
                target_date = input("Enter the target date (e.g., 1990-12-01): ").strip()
                results = self.controller.search_after_target_date(target_date)
                break
            elif choice == '6':
                self.show_user_interface()
                return
            else:
                print("Invalid input. Please try again.\n")

        print("\nSearch results (ID, Type, Name, Publication Date, Author/Artist, Publisher, Available/Total Copies):")
        headers = ["ID", "Type", "Name", "Publication Date", "Author/Artist", "Publisher", "Available/Total Copies"]

        with open("output.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(results)
        if results:
            for record in results:
                print(record)
        else:
            print("No results found.")

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
        obj_holder = [str(date.today()), 0.0]

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

    
