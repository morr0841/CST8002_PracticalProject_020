""" 
Author: Elairis Morrow

Practical Project 2 for Algonquin College CST8002 S26. 

This program allows a user to: 
    - Reload dataset from CSV
    - Write current data to CSV
    - Display single record
    - Display all records
    - Create new record
    - Edit a record
    - Delete a record
    - Exit the application.
"""

from business.prey_service import Prey_Service
import os

class Menu:
    def __init__(self):
        self.prey_service = Prey_Service()
        
    # Function to clear the console screen
    def clear_screen(self):
        """
        Clears the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    # Function to display the menu
    def display_menu(self):
        """
        Prints the menu to the console.

        Allows choices for #TODO update choices
        """
        print("Program by Elairis Morrow")
        print("-------------------------")
        print("Menu:")
        print("1 Reload dataset from CSV")
        print("2 Write data to CSV")
        print("3 Display single record")
        print("4 Display all records")
        print("5 Create new record")
        print("6 Edit a record")
        print("7 Delete a record")
        print("8 Exit program")



    def run(self):
        """
        Runs the menu.

        This runs until the user quits the program.
        """
        while True:
            self.clear_screen()
            self.display_menu()
            choice = input("\nEnter your choice(1-3): ")

            if choice == '1':
                #TODO Reload dataset from CSV
                pass
            elif choice == '2':
                #TODO Write current data to CSV
                pass
            elif choice == '3':
                #TODO Display single record
                pass
            elif choice == '4':
                #TODO Display all records
                pass
            elif choice == '5':
                #TODO Create new record
                pass
            elif choice == '6':
                #TODO Edit a record
                pass
            elif choice == '7':
                #TODO Delete a record
                pass
            elif choice == '8':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select 1-8.")
            input("\nPress enter to return to menu.")