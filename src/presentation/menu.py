""" 
Presentation layer for Practical Project 4, offering a user menu for interactivity. 

Description: This file contains the console menu for the program. 
This program allows a user to: 
    - Reload dataset from CSV
    - Write current data to CSV
    - Display single record
    - Display all records
    - Create new record
    - Edit a record
    - Delete a record
    - Sort records based on species
    - Exit the application. 
The menu calls the business layer to handle CSV and sorting operations.

Author: Elairis Morrow
Date: 07-28-2026
Programmed for Algonquin College CST8002-020 S26 semester. 

References used:
[1] Python Software Foundation. (n.d.). Sorting Techniques. Python Documentation. [Online]. Available at: https://docs.python.org/3/howto/sorting.html. [Accessed: July 10, 2026].
[2] S. Valdarrama. (Apr 15, 2020). Sorting Algorithms in Python. Real Python. [Online]. Available at: https://realpython.com/sorting-algorithms-python/. [Accessed: July 10, 2026].
[3] GeeksforGeeks. (Dec 12, 2025). Sorting Algorithms in Python. GeeksforGeeks. [Online]. Available at: https://www.geeksforgeeks.org/python/sorting-algorithms-in-python/. [Accessed: July 10, 2026].
[4] Fisheries and Oceans Canada. (Nov 29, 2024). Spatiotemporal variation in anadromous Arctic char (Salvelinus alpinus) foraging ecology and its influence on muscle pigmentation along western Hudson Bay, Nunavut, Canada. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/9cbcf710-a2a1-11ef-8ccf-55cc7f028297 [Accessed: June 23, 2026]
"Contains information licensed under the Open Government Licence – Canada."
https://open.canada.ca/en/open-government-licence-canada
"""

from src.business.prey_service import Prey_Service
from src.model.dto_prey import Prey
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

        Allows choices for 
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
        print("8 Sort records")
        print("9 Exit program")

    def column_choices(self, sort_columns):
        """Helper function for printing out column names and allowing user to select a column based on a dictionary lookup."""
        columns = {
            "1": "year",
            "2": "species",
            "3": "common_name",
            "4": "study_site",
            "5": "ass_community",
            "6": "lat",
            "7": "longi",
            "8": "delta13c",
            "9": "delta13c_c",
            "10": "delta15n",
            "11": "delta15nc",
            "12": "tp",
            "13": "c_n",
            "14": "astax",
            "15": "canthax",
            "16": "retinol"
        }
        
        column_names = {
            "year": "Year",
            "species": "Species",
            "common_name": "Common Name",
            "study_site": "Study Site",
            "ass_community": "Associated Community",
            "lat": "Latitude",
            "longi": "Longitude",
            "delta13c": "Delta13C",
            "delta13c_c": "Delta13Cc",
            "delta15n": "Delta15N",
            "delta15nc": "Delta15Nc",
            "tp": "TP",
            "c_n": "C:N",
            "astax": "Astaxanthin",
            "canthax": "Canthaxanthin",
            "retinol": "Retinol"
        }
        
        while True:
            self.clear_screen()
            print("Choose column number to sort on:")
            print(" 1 - Year")
            print(" 2 - Species")
            print(" 3 - Common Name")
            print(" 4 - Study Site")
            print(" 5 - Associated Community")
            print(" 6 - Latitude")
            print(" 7 - Longitude")
            print(" 8 - Delta13C")
            print(" 9 - Delta13Cc")
            print("10 - Delta15N")
            print("11 - Delta15Nc")
            print("12 - TP")
            print("13 - C:N")
            print("14 - Astaxanthin")
            print("15 - Canthaxanthin")
            print("16 - Retinol")
            
            if sort_columns:
                print("\nColumns already chosen:")
                for column in sort_columns:
                    print(column_names[column])

            choice = input("\nEnter selection: ")
            
            if choice in columns:
                selected_column = columns[choice]
                if selected_column in sort_columns:
                    input("You have already selected that column. Press enter to make a different selection.")
                else:
                    return selected_column
            else:
                input("Invalid selection. Press enter and input a number between 1-16.")

    def continue_choice(self, message):
        """Helper function. Gets y/n from user to continue column choice selection."""
        while True:
            choice = input(message).lower()
            
            if choice == "y":
                return True
            if choice == "n":
                return False
            
            print("Please try again. Enter \"y\" for YES and \"n\" for NO")
    
    def run(self):
        """
        Runs the menu.

        This runs until the user quits the program.
        """
        while True:
            self.clear_screen()
            self.display_menu()
            choice = input("\nEnter your choice(1-9): ")

            if choice == '1': #Reloads the dataset from a CSV file
                self.prey_service.load_rows()
                print("Loaded data from original CSV file.")
                
            elif choice == '2': #Write data to CSV
                self.prey_service.save_rows() #success message is in save_rows method
                
            elif choice == '3': #Display single record
                select_row = int(input("Enter row to display: "))
                actual_row = int(select_row) - 1
                try:
                    print_row = self.prey_service.get_row(actual_row)
                    print("Row", select_row, print_row)
                except Exception as e:
                    input("Invalid row number. Press enter to return to menu.")
                    continue
            elif choice == '4': #Display all records
                print_rows = self.prey_service.get_all_rows()
                count = 1
                for prey in print_rows:
                    print("Row", count, prey)
                    count += 1
                print("Program created by: Elairis Morrow")
            elif choice == '5': #Create new record
                print("Creating new record:")
                year = input("Enter Year: ")
                species = input("Enter Species: ")
                common_name = input("Enter Common Name: ")
                study_site = input("Enter Study Site: ")
                ass_community = input("Enter Associate Community: ")
                lat = input("Enter Latitude: ")
                longi = input("Eneter Longitude: ")
                delta13c = input("Enter Delta13C value: ")
                delta13c_c = input("Enter Delta13Cc value: ")
                delta15n = input("Enter Delta15N value: ")
                delta15Nc = input("Enter Delta15Nc value: ")
                tp = input("Enter TP value: ")
                c_n = input("Enter C:N value: ")
                astax = input("Enter Astaxanthin(mg/kg) value: ")
                canthax = input("Enter Canthaxanthin(mg/kg) value: ")
                retinol = input("Enter Retinol(mg/kg) value: ")
                
                new_prey = Prey(year, species, common_name, study_site, ass_community, lat, longi, delta13c, delta13c_c, 
                                delta15n, delta15Nc, tp, c_n, astax, canthax, retinol)
                self.prey_service.create_row(new_prey)
            
            elif choice == '6':#Edit a record
                select_row = input("Enter row to update: ")
                actual_row = int(select_row) - 1
                try:
                    print(f"Updating record {select_row}: ")
                    year = input("Enter Year: ")
                    species = input("Enter Species: ")
                    common_name = input("Enter Common Name: ")
                    study_site = input("Enter Study Site: ")
                    ass_community = input("Enter Associate Community: ")
                    lat = input("Enter Latitude: ")
                    longi = input("Eneter Longitude: ")
                    delta13c = input("Enter Delta13C value: ")
                    delta13c_c = input("Enter Delta13Cc value: ")
                    delta15n = input("Enter Delta15N value: ")
                    delta15Nc = input("Enter Delta15Nc value: ")
                    tp = input("Enter TP value: ")
                    c_n = input("Enter C:N value: ")
                    astax = input("Enter Astaxanthin(mg/kg) value: ")
                    canthax = input("Enter Canthaxanthin(mg/kg) value: ")
                    retinol = input("Enter Retinol(mg/kg) value: ")
                    
                    updated_prey = Prey(year, species, common_name, study_site, ass_community, lat, longi, delta13c, delta13c_c, 
                                    delta15n, delta15Nc, tp, c_n, astax, canthax, retinol)
                    self.prey_service.update_row(actual_row, updated_prey)
                    print("Record updated. Press enter to continue.")
                    
                except Exception as e:
                    input("Invalid row number. Press enter to return to menu.")
                    continue
                
            elif choice == '7': #Delete a record
                select_row = int(input("Enter row to delete: "))
                actual_row = int(select_row) - 1
                try:
                    self.prey_service.delete_row(actual_row)
                except Exception as e:
                    input("Invalid row number. Press enter to return to menu.")
                    continue
            elif choice == '8': #Sort rows by user choice
                sort_columns = []
                sort_column1 = self.column_choices(sort_columns)
                sort_columns.append(sort_column1)
                if self.continue_choice("Would you like to add a second sort column? (y/n): "):
                    sort_column2 = self.column_choices(sort_columns)
                    sort_columns.append(sort_column2)
                    if self.continue_choice("Would you like to add a third sort column? (y/n): "):
                        sort_column3 = self.column_choices(sort_columns)
                        sort_columns.append(sort_column3)
                self.prey_service.sort_rows(sort_columns)
            elif choice == '9': #Exit the program
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select 1-9.")
            input("\nPress enter to return to menu.")