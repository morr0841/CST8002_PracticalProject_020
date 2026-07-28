"""
A DTO class for csv_rw.py to use for making a Data Transfer Object out of a row from the CSV dataset.

Description:
This class stores the data from each column in a single row from the CSV dataset. 

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

class Prey:
    """ Represents a single prey record. """
    
    def __init__(self, year, species, common_name, study_site, ass_community, lat, longi, 
                 delta13c, delta13c_c, delta15n, delta15nc, tp, c_n, astax, canthax, retinol):
        """ Creates a Prey object from a single CSV record. """
        self.year = year
        self.species = species
        self.common_name = common_name
        self.study_site = study_site
        self.ass_community = ass_community
        self.lat = lat
        self.longi = longi
        self.delta13c = delta13c
        self.delta13c_c = delta13c_c
        self.delta15n = delta15n
        self.delta15nc = delta15nc
        self.tp = tp
        self.c_n = c_n
        self.astax = astax
        self.canthax = canthax
        self.retinol = retinol
        
    def __str__(self):
        """ Returns a formatted string representation of the object. """
        return f"\tYear: {self.year}, Species: {self.species}, Common name: {self.common_name}, Study site: {self.study_site}, Associated Community: {self.ass_community}\n\t\tLatitude: {self.lat}, Longitude: {self.longi}, delta13C: {self.delta13c}, delta13Cc: {self.delta13c_c}, delta15N: {self.delta15n}, delta15Nc: {self.delta15nc}\n\t\tTP: {self.tp}, C:N :{self.c_n}, Astaxanthin: {self.astax}, Canthaxanthin: {self.canthax}, Retinol: {self.retinol}"