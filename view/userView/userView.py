"""
UserView class
userView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from Employee

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
import csv
from datetime import datetime, date


class UserView:

    def __init__(self, id, controller):
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
            "0. Return to the main menu\n"
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
            elif choice == '0':
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
        user_info = self.controller.fetch_user_info(self.id)
        while float(user_info[2]) != 0:
            print("You cannot request an item when you have outstanding charges.")
            self.make_payment()
            user_info = self.controller.fetch_user_info(self.id)

        while True:
            item_id = input("Please input the ID of the item you wish to borrow: ")
            if self.controller.search_library_database_by_id(item_id) is not None:
                break
            print("Invalid ID. Please enter a valid item ID.")

        self.controller.borrow_library_record(self.id, item_id)

    def library_return(self):
        while True:
            item_id = input("Please input the ID of the item you wish to return: ")
            if self.controller.search_library_database_by_id(item_id) is not None:
                break
            print("Invalid ID. Please enter a valid item ID.")
        self.controller.return_library_record(self.id, item_id)

    def library_donate(self):
        object_holder = []
        object_holder.append(input("Please enter the item type: "))
        object_holder.append(input("Please enter the item title: "))
        while True:
            pub_date = input("Please enter the publication date (YYYY-MM-DD): ")
            try:
                pub_date = datetime.strptime(pub_date, "%Y-%m-%d").date()
                object_holder.append(pub_date)
                break
            except ValueError:
                print("Invalid date format for date of publication. Please use YYYY-MM-DD.")
        art_name = input("Please enter the artist's name: ")
        object_holder.append(art_name)
        pub_name = input("Please enter the publisher's name: ")
        object_holder.append(pub_name)
        item_id = self.controller.insert_library_database(object_holder)
        self.controller.insert_library_record(item_id)

    def event_register(self):
        results = self.controller.get_list_of_events()
        print("\nA list of all current events has been saved, please enter the ID of the event you wish to register for.\n")
        print("\nSearch results (ID, Name, Type, Location, Age Range, Event Time):")
        headers = ["ID", "Name", "Type", "Location", "Age Range", "Event Time"]

        with open("list_of_events.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(results)
        if results:
            for record in results:
                print(record)
        else:
            print("No results found.")
        while True:
            event_id = input("Please input the ID of the event you wish to return: ")
            if self.controller.check_validity_of_event_id(event_id):
                self.controller.register_for_event(event_id, self.id)
                break
            else:
                print("\nInvalid ID. Please enter a valid event ID.\n")


    def register_for_volunteer(self):
        obj_holder = [str(date.today()), 0.0]

        self.controller.insert_volunteer_employee(obj_holder, self.id)

    def request_help(self):
        message = input("Please enter your request: ")
        self.controller.insert_request(message, self.id)

    def fetch_loans(self):
        results = self.controller.fetch_library_loans(self.id)
        if not results:
            print("You have no loans at this time.")
            return
        print("Loan ID, Item ID, Type, Name, Days Remaining")
        for result in results:
            print(result)

    def make_payment(self):
        user_info = self.controller.fetch_user_info(self.id)
        while True:
            try:
                amount = float(input("\nPlease enter the payment amount: "))
                if amount <= float(user_info[2]) and amount >= 0:
                    break
                print("Payments must be equal to or less than your outstanding balance. Please enter a valid amount.")
            except ValueError:
                print("Invalid format. Please enter a dollar amount.")
        self.controller.make_charge_payment(self.id, amount)

    def fetch_requests(self):
        results = self.controller.fetch_user_requests(self.id)
        if not results:
            print("You have no requests at this time.")
            return
        print("Request ID, Message, Response")
        for result in results:
            print(result)

    def show_user_interface(self):
        user_info = self.controller.fetch_user_info(self.id)
        print("Welcome user", user_info[0] + ' ' + user_info[1], "\nYou currently have $", user_info[2],
              "in outstanding charges.")
        input_table = {
            '1': self.library_search,
            '2': self.library_borrow,
            '3': self.library_return,
            '4': self.library_donate,
            '5': self.event_register,
            '6': self.register_for_volunteer,
            '7': self.request_help,
            '8': self.fetch_loans,
            '9': self.make_payment,
            '10': self.fetch_requests,
            '0': lambda: (print("Exiting..."), exit(0)[-1])
        }

        while True:
            prompt = input(
                "\n1. Find an item in the library\n"
                "2. Borrow an item from the library\n"
                "3. Return an item to the library\n"
                "4. Donate an item to the library\n"
                "5. Register for an event in the library\n"
                "6. Volunteer for the library\n"
                "7. Ask for help from a librarian\n"
                "8. View existing library loans\n"
                "9. Pay outstanding charges\n"
                "10. View existing help requests\n"
                "0. Exit\n\n"
            )
            action = input_table.get(prompt, lambda: print("Invalid input, please try again."))
            action()
