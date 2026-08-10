"""
A program that demonstrates a simple N-Layer architecture using CSV file persistence, DTO objects, CRUD operations, 
UUID file naming, record sorting, and unit testing.

Description:
This program reads data from a CSV file into Prey DTO objects and stores them in an in-memory list. The user may view, 
create, update, delete, sort, and save records through a console menu interface.

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
from src.presentation.menu import Menu

class Main:
  """ Program entry point. """
  def main(self):
    """ Creates the menu object and starts the application. """
    menu = Menu()
    menu.run()

if __name__ == "__main__":
  program = Main()
  program.main()