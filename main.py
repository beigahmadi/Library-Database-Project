"""
main.py

Class Description:
Class Invariant:

Author(s): Mahdi Beigahmadi, Cole Scott Robertson
Last modified: March. 2025
"""
from controller import DatabaseController

if __name__ == "__main__":
    db_controller = DatabaseController("library.db")


    # Close when done
    db_controller.close_connection()
