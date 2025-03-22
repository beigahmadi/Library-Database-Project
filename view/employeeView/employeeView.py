"""
EmployeeView class
employeeView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from users

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from datetime import datetime, date
import csv

class EmployeeView:
    def __init__(self, id, controller):
        self.id = id
        self.controller = controller

    def user_insertion(self):
        obj_holder = []
        obj_holder.append(input("Enter first name: "))
        obj_holder.append(input("Enter last name: "))

        dob_input = input("Enter date of birth (YYYY-MM-DD): ")
        if not dob_input:
            dob_input = date.today()
        else:
            while True:
                try:
                    dob_input = datetime.strptime(dob_input, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.\n")
                    dob_input = input("Enter date of birth (YYYY-MM-DD): ")
        obj_holder.append(dob_input)

        obj_holder.append(input("Enter address: "))
        obj_holder.append(input("Enter phone number: "))

        date_joined_input = input("Enter date of account creation (YYYY-MM-DD) [leave blank for today]: ")
        if not date_joined_input:
            date_joined = date.today()
        else:
            while True:
                try:
                    date_joined = datetime.strptime(date_joined_input, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.\n")
                    date_joined_input = input("Enter date of account creation (YYYY-MM-DD) [leave blank for today]: ")
        obj_holder.append(date_joined)

        while True:
            total_charge = input("Enter total charges due on account: ")
            try:
                total_charge = float(total_charge) if total_charge else 0.0
                obj_holder.append(total_charge)
                break
            except ValueError:
                print("Invalid total charge. Please enter a valid number.\n")

        self.controller.insert_user(obj_holder)

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
                self.show_employee_interface()
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

    def item_return(self):
        pass

    def item_insertion(self):
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
        self.controller.insert_library_database(object_holder)

    def show_list_event_participants(self):
        print("\nEvent participants: (Event ID, Registered User ID)")
        print(self.controller.print_list_of_event_participants())
        print('\n')

    def record_insertion(self):
        while True:
            id = input("Please enter the item ID: ")
            if self.controller.search_library_database_by_id(id) is not None:
                break
            print("Invalid ID. Please enter a valid item ID.")

        while True:
            num = input("Please enter the number of copies to insert: ")
            try:
                num = int(num)
                break
            except ValueError:
                print("Invalid number of copies. Please enter an integer.\n")

        for _ in range(num):
            self.controller.insert_library_record(id)

    def fetch_requests(self):
        print("Request ID, Message")
        for value in self.controller.fetch_employee_requests():
            print(value)

    def request_reply(self):
        while True:
            request_id = input("Please enter the ID of the request you wish to reply to: ")
            if self.controller.validate_request_id(request_id):
                break
            print("Invalid ID. Please enter a valid request ID.")
        reply = input("Please enter your reply: ")
        self.controller.request_reply_update(reply, request_id)

    def show_employee_interface(self):
        employee_info = self.controller.fetch_employee_info(self.id)
        print("Welcome employee", employee_info[0])
        input_table = {
            '1': self.user_insertion,
            '2': self.library_search,
            '3': self.item_return,
            '4': self.item_insertion,
            '5': self.record_insertion,
            '6': self.show_list_event_participants,
            '7': self.fetch_requests,
            '8': self.request_reply,
            '0': lambda: (print("Exiting..."), exit(0)[-1])
        }

        while True:
            prompt = input(
                "\n1. Sign up a new user to the library\n"
                "2. Find an item in library database\n"
                "3. Return a borrowed item\n"
                "4. Add an item to the library\n"
                "5. Add a record to the library\n"
                "6. View list of event participants\n"
                "7. View unresolved help requests\n"
                "8. Reply to a help request\n"
                "0. Exit\n\n"
            )
            action = input_table.get(prompt, lambda: print("Invalid input, please try again."))
            action()