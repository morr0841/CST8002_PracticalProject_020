"""
Business layer for Practical Project 3.

Description:
This contains the service layer for the application. It manages the in-memory list of Prey objects and provides methods for:
    - loading
    - retrieving
    - creating
    - updating 
    - deleting
    - saving records
    - sorting records based on species
The service layer acts as an intermediary between the presentation layer and the persistence layer.

Author: Elairis Morrow
Date: 08-09-2026
Programmed for Algonquin College CST8002-020 S26 semester. 
Professor: Daniel Cormier
Practical Project 04 
Due: 08-09-2026

References used:
[1] Python Software Foundation. (n.d.). Sorting Techniques. Python Documentation. [Online]. Available at: https://docs.python.org/3/howto/sorting.html. [Accessed: Aug 09, 2026].
[2] GeeksforGeeks. (Jul 23, 2025). Sort a list of objects by multiple attributes in Python. GeeksforGeeks. [Online]. Available at: https://www.geeksforgeeks.org/python/sort-a-list-of-objects-by-multiple-attributes-in-python/. [Accessed: Aug 09, 2026].
[3] GeeksforGeeks. (Dec 12, 2025). Sorting Algorithms in Python. GeeksforGeeks. [Online]. Available at: https://www.geeksforgeeks.org/python/sorting-algorithms-in-python/. [Accessed: July 10, 2026].
[4] Fisheries and Oceans Canada. (Nov 29, 2024). Spatiotemporal variation in anadromous Arctic char (Salvelinus alpinus) foraging ecology and its influence on muscle pigmentation along western Hudson Bay, Nunavut, Canada. open.canada.ca. [online] Available at https://open.canada.ca/data/en/dataset/9cbcf710-a2a1-11ef-8ccf-55cc7f028297 [Accessed: Aug 09, 2026]
"Contains information licensed under the Open Government Licence – Canada."
https://open.canada.ca/en/open-government-licence-canada
"""
import operator
from src.persistence.csv_rw import CsvRW

class Prey_Service:
    """Business layer responsible for managing Prey objects."""
    def __init__(self):
        """Creates the service and initializes CSV handler."""
        
        self.all_rows = []
        self.csv_rw = CsvRW("src/data/Prey collection & analysis - raw data.csv")

    def load_rows(self):
        """Loads records from the CSV file into memory."""
        self.all_rows = self.csv_rw.read_csv()

    def get_all_rows(self):
        """Returns all records currently stored in memory."""
        return self.all_rows
    
    def get_row(self, row_number):
        """Returns a single record from the specified row."""
        return self.all_rows[row_number]

    def save_rows(self):
        """Saves the current records to a new CSV file."""
        self.csv_rw.write_csv(self.all_rows)

    def create_row(self, prey):
        """Adds a new record to the in-memory list."""
        self.all_rows.append(prey)

    def update_row(self, row_number, updated_prey):
        """Replaces an existing record with updated data."""
        self.all_rows[row_number] = updated_prey

    def sort_rows(self, sort_columns):
        """Sorts the rows according to user selections."""
        self.all_rows.sort(key=operator.attrgetter(*sort_columns))

    def delete_row(self, row_number):
        """Removes a record from the in-memory list."""
        del self.all_rows[row_number]