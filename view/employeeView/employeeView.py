"""
EmployeeView class
employeeView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from users

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from datetime import datetime


class EmployeeView:

    @staticmethod
    def get_data_for_insertion(controller):
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
        controller.insert_library_database(object_holder)

    @staticmethod
    def show_employee_interface(controller):
        prompt = input(
            "\n\n1. Sign up a new user to the library\n"
            "2. Find an item in library database\n"
            "3. Return a borrowed item\n"
            "4. Add an item to the library\n"
            "0. Exit\n\n"
        )

        if prompt == "1":
            controller.insert_user()
        elif prompt == "2":
            title_for_search = input("Please enter the title you prefer to search:\n")
            results = controller.search_library_database_by_title(title_for_search)
            print("Search results:", results)
        elif prompt == "3":
            pass
        elif prompt == "4":
            EmployeeView.get_data_for_insertion(controller)
        elif prompt == "0":
            print("Exiting employee interface...")
            exit(0)
        else:
            print("Invalid input, please try again.\n")
        EmployeeView.show_employee_interface(controller)
