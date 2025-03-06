"""
main.py

Class Description: the main file that the program begins
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from controller.controller import DatabaseController
from pathlib import Path
from view.ui import UI
import os
if __name__ == "__main__":
    db_controller = DatabaseController("library.db")
    ui = UI(db_controller)
    ui.print_ui()

    db_controller.close_connection()
