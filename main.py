"""
main.py

Class Description: the main file that the program begins
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from controller.controller import DatabaseController
from view.ui import UI
if __name__ == "__main__":
    db_controller = DatabaseController("/Users/mahdibeigahmadi/Documents/GitHub/Library-Database-Project/library.db")
    ui = UI()
    ui.print_ui()

    db_controller.close_connection()
