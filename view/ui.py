"""
UI class
ui.py

Class Description: it shows the UI for the db
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""

class UI:
    def __init__(self, controller):
        self.controller = controller
        pass

    def print_ui(self):
        prompt = input(
            "Select among the following items:\n"
            "1. Find an item in the library\n"
            "2. Request a loan from the library\n"
            "3. Return a borrowed item\n"
            "4. Donate an item to the library\n"
            "5. Find an event in the library\n"
            "6. Register for an event in the library\n"
            "7. Volunteer for the library\n"
            "8. Ask for help from a librarian\n"
            "Enter your choice: "
        )
        if prompt == "1":
            item_name = input("Enter item name:\n ")
        elif prompt == "9":
            self.controller.insert_user()

