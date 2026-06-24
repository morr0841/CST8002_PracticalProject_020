"""
Unit test for the Prey_Service class.

Description:
Tests the method create_row()

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