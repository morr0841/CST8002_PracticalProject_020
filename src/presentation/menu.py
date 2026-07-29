""" 
Presentation layer for Practical Project 2, offering a user menu for interactivity. 

Description: This file contains the console menu for the program. 
This program allows a user to: 
    - Reload dataset from CSV
    - Write current data to CSV
    - Display single record
    - Display all records
    - Create new record
    - Edit a record
    - Delete a record
    - Exit the application. 
The menu calls the business layer to handle CSV operations.

Author: Elairis Morrow
Date: 06-23-2026
Programmed for Algonquin College CST8002-020 S26 semester. 

References used:
[1] Pytest Development Team. (n.d.) How to use unittest-based tests with pytest. docs.pytest.org. [Online]. Available at: https://docs.pytest.org/en/stable/how-to/unittest.html. [Accessed: Jun. 13, 2026].
[2] GeeksForGeeks. (n.d.) How to Use Pytest for Unit Testing. geeksforgeeks.org. [Online]. Available at: https://www.geeksforgeeks.org/python/how-to-use-pytest-for-unit-testing/. [Accessed: Jun. 13, 2026].
[3] PythonForAll. (n.d.) Best Practices for pytest. pythonforall.com. [Online]. Available at: https://www.pythonforall.com/modules/pytest/tsbest. [Accessed: Jun. 13, 2026].
[4] Microsoft. (n.d.) Python testing in Visual Studio Code. code.visualstudio.com. [Online]. Available at: https://code.visualstudio.com/docs/python/testing. [Accessed: Jun. 14, 2026].
[5] W3Schools. (n.d.) Python UUID Module. W3Schools. [Online]. Available at: https://www.w3schools.com/python/ref_module_uuid.asp. [Accessed: Jun. 18, 2026].
[6] Python Software Foundation. (n.d.) uuid — UUID objects according to RFC 9562. Python Documentation. [Online]. Available at: https://docs.python.org/3/library/uuid.html. [Accessed: Jun. 18, 2026].
[7] Bro Code. Python Full Course for Beginners #8. (May 25, 2020). Accessed: Jun. 20, 2026. [Online Video]. Available: https://youtu.be/VnAslzyDitM?si=oKAflXJcT5mRo8dj
[8] GeeksforGeeks. (n.d.) Python – Update in Array. GeeksforGeeks. [Online]. Available at: https://www.geeksforgeeks.org/python/python-update-in-array/. [Accessed: Jun. 21, 2026].
[9] DataCamp. (Aug 1, 2024). Python Remove Item from List. DataCamp. [Online]. Available at: https://www.datacamp.com/tutorial/python-remove-item-from-list. [Accessed: Jun. 22, 2026].
[10] W3Schools. (n.d.) Python String Formatting. W3Schools. [Online]. Available at: https://www.w3schools.com/python/python_string_formatting.asp. [Accessed: Jun. 23, 2026].
[11] Fisheries and Oceans Canada. (Nov 29, 2024). Spatiotemporal variation in anadromous Arctic char (Salvelinus alpinus) foraging ecology and its influence on muscle pigmentation along western Hudson Bay, Nunavut, Canada. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/9cbcf710-a2a1-11ef-8ccf-55cc7f028297 [Accessed: June 23, 2026]
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
        print("8 Sort list by species")
        print("9 Exit program")



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
            elif choice == '8': #Sort rows by species
                    self.prey_service.sort_rows()
                    print("Sorted rows by species.")
            elif choice == '9': #Exit the program
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select 1-9.")
            input("\nPress enter to return to menu.")