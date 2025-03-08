"""
EmployeeView class
employeeView.py

Class Description: it shows the end-poit for the employee
Class Invariant: Must be hidden from users

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""


class EmployeeView:
    @staticmethod
    def show_employee_interface(controller):
        while True:
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
                pass
            elif prompt == "0":
                print("Exiting employee interface...")
                exit(0)
            else:
                print("Invalid input, please try again.\n")
