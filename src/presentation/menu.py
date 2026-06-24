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
from model.dto_prey import Prey
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
                    
            elif choice == '5': #Create new record
                print("Creating new record:")
                year = input("\nEnter Year: ")
                species = input("\nEnter Species: ")
                common_name = input("vEnter Common Name: ")
                study_site = input("\nEnter Study Site: ")
                ass_community = input("\nEnter Associate Community: ")
                lat = input("vEnter Latitude: ")
                longi = input("\nEneter Longitude: ")
                delta13c = input("\nEnter Delta13C value: ")
                delta13c_c = input("\nEnter Delta13Cc value: ")
                delta15n = input("\nEnter Delta15N value: ")
                delta15Nc = input("\nEnter Delta15Nc value: ")
                tp = input("\nEnter TP value: ")
                c_n = input("\nEnter C:N value: ")
                astax = input("\nEnter Astaxanthin(mg/kg) value: ")
                canthax = input("\nEnter Canthaxanthin(mg/kg) value: ")
                retinol = input("\nEnter Retinol(mg/kg) value: ")
                
                new_prey = Prey(year, species, common_name, study_site, ass_community, lat, longi, delta13c, delta13c_c, 
                                delta15n, delta15Nc, tp, c_n, astax, canthax, retinol)
                self.prey_service.create_row(new_prey)
                print("Program created by: Elairis Morrow")
            
            elif choice == '6':#Edit a record
                #TODO 
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
            elif choice == '8': #Exit the program
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select 1-8.")
            input("\nPress enter to return to menu.")