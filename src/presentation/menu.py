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
        self.prey_service.load_rows()
    
    def clear_screen(self): # Function to clear the console screen
        """
        Clears the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    
    def display_menu(self): # Function to display the menu
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
            choice = input("\nEnter your choice(1-8): ")

            if choice == '1': #Reloads the dataset from a CSV file
                self.prey_service.load_rows()
                print("Loaded data from original CSV file.")
                
            elif choice == '2':
                self.prey_service.save_rows()
                
            elif choice == '3':
                #TODO Display single record
                pass
            elif choice == '4':
                print_rows = self.prey_service.get_all_rows()
                count = 1
                for prey in print_rows:
                    print("Row", count, prey)

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