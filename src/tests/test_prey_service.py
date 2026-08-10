"""
Unit test for the Prey_Service class.

Description:
Tests the method create_row()

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
from src.business.prey_service import Prey_Service
from src.model.dto_prey import Prey

def test_create_row():
    """
    Verifies that create_row() adds a Prey object to the list.
    """
    service = Prey_Service()
    prey = Prey(
        "Test Year",
        "Test species",
        "Test common name",
        "Test site",
        "Test community",
        "42 is the answer",
        "Test longi",
        "Test delta13C",
        "Test delta13Cc",
        "Test delta15N",
        "Test delta15Nc",
        "Test TP",
        "Test C:N",
        "Test Astax",
        "Test Canthax",
        "Test Retinol"
    )
    service.create_row(prey)
    result = service.get_row(0)
    assert result.lat == "42 is the answer"